import os
import json
import streamlit as st
from openai import OpenAI
from pyswip import Prolog

# ------------------------------------------------------------------------------
# 1. SETUP & INITIALISIERUNG
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Koran-Normativität: KI-NLU & Logik-Inferenz", 
    layout="wide", 
    page_icon="🏛️"
)

@st.cache_resource
def init_openai():
    api_key = st.secrets.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        st.error("Kein OPENAI_API_KEY gefunden!")
        return None
    return OpenAI(api_key=api_key)

# ------------------------------------------------------------------------------
# 2. DEFINITION DER VALIDEN PROLOG-TOOLS (SCHEMATA)
# ------------------------------------------------------------------------------
# Hier wird das Inventar der zulässigen Fakten definiert.
# Das LLM kann KEINE freien Prädikate mehr erfinden.

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "set_glaeubig",
            "description": "Legt fest, ob ein Akteur gläubig ist.",
            "parameters": {
                "type": "object",
                "properties": {
                    "akteur": {"type": "string", "enum": ["zaid", "amr"]}
                },
                "required": ["akteur"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "set_anzahl_ehefrauen",
            "description": "Erfasst die aktuelle Anzahl der Ehefrauen eines Akteurs.",
            "parameters": {
                "type": "object",
                "properties": {
                    "akteur": {"type": "string", "enum": ["zaid", "amr"]},
                    "anzahl": {"type": "integer"}
                },
                "required": ["akteur", "anzahl"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "set_beabsichtigt_eheschliessung",
            "description": "Erfasst die Absicht einer erneuten Eheschließung.",
            "parameters": {
                "type": "object",
                "properties": {
                    "akteur": {"type": "string", "enum": ["zaid", "amr"]}
                },
                "required": ["akteur"]
            }
        }
    }
]

# ------------------------------------------------------------------------------
# 3. COMPILER: TOOL-CALLS -> PROLOG-FAKTEN
# ------------------------------------------------------------------------------
def compile_tool_calls_to_prolog(tool_calls):
    """
    Deterministischer Übersetzer: Wandelt die vom LLM gewählten Tools 
    in exakte, syntaktisch korrekte Prolog-Fakten um.
    """
    prolog_facts = []
    
    for call in tool_calls:
        fn_name = call.function.name
        args = json.loads(call.function.arguments)
        akteur = args.get("akteur", "zaid")
        
        if fn_name == "set_glaeubig":
            prolog_facts.append(f"ist_glaeubig({akteur}).")
        elif fn_name == "set_anzahl_ehefrauen":
            anzahl = args.get("anzahl", 0)
            prolog_facts.append(f"anzahl_ehefrauen({akteur}, {anzahl}).")
        elif fn_name == "set_beabsichtigt_eheschliessung":
            prolog_facts.append(f"beabsichtigt({akteur}, eheschliessung).")
            prolog_facts.append(f"beabsichtigt_eheschliessung({akteur}).")
            
    return prolog_facts

def parse_user_intent_with_tools(client, user_text):
    system_prompt = """
Du bist ein Präzisions-Parser für ein koranisches Rechts-Logiksystem.
Analysiere den Text und rufe die passenden Funktionen auf, um den Sachverhalt für die Akteure 'zaid' oder 'amr' zu erfassen.
Falls die Person nicht genannt ist oder in 1. Person gesprochen wird, nutze 'zaid'.
Ehefrauen-Regel: Bei 'fünfte Frau heiraten' liegt die aktuelle Anzahl bei 4.
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_text}
            ],
            tools=TOOLS,
            tool_choice="auto",
            temperature=0.0
        )
        
        tool_calls = response.choices[0].message.tool_calls
        if tool_calls:
            return compile_tool_calls_to_prolog(tool_calls)
        return []
    except Exception as e:
        st.error(f"NLU-Parsing-Fehler: {e}")
        return []

# ------------------------------------------------------------------------------
# 4. PROLOG INFERENZ-ENGINE (TEMPORÄRE KONSULTATION)
# ------------------------------------------------------------------------------
def run_prolog_inference(facts):
    facts_file = "temp_nlu_facts.pl"
    pl_file = "Koran_ethische_PROLOG_Regeln_bereinigt.pl"
    
    with open(facts_file, "w", encoding="utf-8") as f:
        f.write(":- dynamic ist_glaeubig/1.\n")
        f.write(":- dynamic anzahl_ehefrauen/2.\n")
        f.write(":- dynamic beabsichtigt/2.\n")
        f.write(":- dynamic beabsichtigt_eheschliessung/1.\n\n")
        for fact in facts:
            f.write(f"{fact}\n")
            
    prolog = Prolog()
    prolog.consult(facts_file)
    if os.path.exists(pl_file):
        prolog.consult(pl_file)
        
    verbote, gebote, erlaubnisse = [], [], []
    
    for akteur in ["zaid", "amr"]:
        try:
            res_v = list(prolog.query(f"untersagt({akteur}, Action)"))
            for item in res_v:
                verbote.append({"X": akteur, "Action": str(item["Action"])})
        except Exception:
            pass
            
    return verbote, gebote, erlaubnisse

# ------------------------------------------------------------------------------
# 5. BENUTZEROBERFLÄCHE (DIDAKTISCHER ABLAUF)
# ------------------------------------------------------------------------------
st.title("🏛️ Koran-Normativität: KI-NLU & Logik-Inferenz")
st.caption("Gesteuerte NLU über Function-Calling (Tools) mit deterministischem Prolog-Kernel")

user_input = st.text_area(
    "Geben Sie einen beliebigen Sachverhalt ein:",
    height=100,
    placeholder="Darf Zaid eine fünfte Frau heiraten?"
)

if st.button("⚖️ Sachverhalt auswerten", type="primary"):
    if not user_input.strip():
        st.warning("Bitte geben Sie einen Text ein.")
    else:
        client = init_openai()
        if client:
            with st.spinner("1. NLU wählt strukturierte Tools aus..."):
                extracted_facts = parse_user_intent_with_tools(client, user_input)
                
            st.subheader("1. Vom System erkannte Fakten (Prolog-Transformation)")
            if extracted_facts:
                st.code("\n".join(extracted_facts), language="prolog")
                
                with st.spinner("2. SWI-Prolog rechnet Inferenz durch..."):
                    verbote, gebote, erlaubnisse = run_prolog_inference(extracted_facts)
                    
                st.subheader("2. Berechnete Inferenz-Ergebnisse")
                if not (verbote or gebote or erlaubnisse):
                    st.info("Keine normativen Verbote oder Gebote für die erkannten Fakten definiert.")
                
                if verbote:
                    for v in verbote:
                        st.error(f"⛔ **Untersagt für '{v['X']}':** {v['Action']}")
            else:
                st.warning("Die NLU konnte aus dem Text keine bekannten Werkzeuge zuordnen.")
