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
        st.error("Kein OPENAI_API_KEY in den Streamlit Secrets gefunden!")
        return None
    return OpenAI(api_key=api_key)

@st.cache_resource
def init_prolog():
    prolog = Prolog()
    pl_file = "Koran_ethische_PROLOG_Regeln_bereinigt.pl"
    
    if os.path.exists(pl_file):
        prolog.consult(pl_file)
    else:
        st.error(f"Prolog-Datei '{pl_file}' wurde im Repository nicht gefunden!")
    return prolog

prolog = init_prolog()

# ------------------------------------------------------------------------------
# 2. DYNAMISCHE NLU-PIPELINE (OPENAI GPT)
# ------------------------------------------------------------------------------
def extract_prolog_facts(client, user_text):
    system_prompt = """
Du bist ein NLU-Parser für ein koranisches Logiksystem in SWI-Prolog.
Übersetze Freitext streng in einstellige und zweistellige Prädikate über den Akteuren 'zaid' (Subjekt X) und 'amr' (Objekt/Partner Y).

REGELN FÜR DIE ABBILDUNG:
1. Subjekt X: 'zaid' (bei "ich", anonymen Anfragen oder explizit Zaid).
2. Objekt/Partner Y: 'amr'.
3. Standard-Axiom: Setze stets 'ist_glaeubig(zaid)'.
4. Handlungen & Zustände als Prädikate für X:
   - "fünfte Frau heiraten" -> 
     ist_glaeubig(zaid)
     anzahl_ehefrauen(zaid, 4)
     beabsichtigt_eheschliessung(zaid)

Gib STRIKT ein JSON-Array von Strings zurück:
[
  "ist_glaeubig(zaid)",
  "anzahl_ehefrauen(zaid, 4)",
  "beabsichtigt_eheschliessung(zaid)"
]
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_text}
            ],
            response_format={"type": "json_object"},
            temperature=0.0
        )
        content = response.choices[0].message.content
        parsed = json.loads(content)
        
        if isinstance(parsed, dict):
            for key in parsed:
                if isinstance(parsed[key], list):
                    return parsed[key]
            return []
        elif isinstance(parsed, list):
            return parsed
        return []
    except Exception as e:
        st.error(f"Fehler bei NLU-Anfrage: {e}")
        return []

# ------------------------------------------------------------------------------
# 3. BENUTZEROBERFLÄCHE & INFERENZ
# ------------------------------------------------------------------------------
st.title("🏛️ Koran-Normativität: KI-NLU & Logik-Inferenz")
st.caption("Ein hybrides System aus Natural Language Understanding (OpenAI GPT) und formaler Logik (SWI-Prolog)")

user_input = st.text_area(
    "Geben Sie einen beliebigen Sachverhalt in eigener Sprache ein:",
    height=100,
    placeholder="Darf Zaid eine fünfte Frau heiraten?"
)

if st.button("⚖️ Sachverhalt via NLU & Prolog auswerten", type="primary"):
    if not user_input.strip():
        st.warning("Bitte geben Sie zuerst einen Text ein.")
    else:
        client = init_openai()
        if client:
            with st.spinner("1. NLU analysiert Fließtext und extrahiert formale Fakten..."):
                extracted_facts = extract_prolog_facts(client, user_input)
                
            st.subheader("1. Extrahierter NLU-Kontext (Prolog-Fakten)")
            if extracted_facts:
                st.json(extracted_facts)
                
                with st.spinner("2. SWI-Prolog rechnet deontische Inferenz durch..."):
                    # Fakten einspeisen
                    for fact in extracted_facts:
                        try:
                            prolog.assertz(fact)
                        except Exception:
                            pass
                    
                    verbote, gebote, erlaubnisse = [], [], []
                    
                    # Abfragen für den Hauptakteur zaid und amr
                    for akteur in ["zaid", "amr"]:
                        try:
                            res_v = list(prolog.query(f"untersagt({akteur}, Action)"))
                            for item in res_v:
                                verbote.append({"X": akteur, "Action": str(item["Action"])})
                        except Exception:
                            pass

                        try:
                            res_g = list(prolog.query(f"gebietet({akteur}, Action)"))
                            for item in res_g:
                                gebote.append({"X": akteur, "Action": str(item["Action"])})
                        except Exception:
                            pass

                        try:
                            res_e = list(prolog.query(f"gestattet({akteur}, Action)"))
                            for item in res_e:
                                erlaubnisse.append({"X": akteur, "Action": str(item["Action"])})
                        except Exception:
                            pass
                    
                st.subheader("2. Berechnete Inferenz-Ergebnisse (Prolog Kernel)")
                
                if not (verbote or gebote or erlaubnisse):
                    st.info("Keine spezifischen normativen Verbote oder Gebote für die erkannten Fakten in der Wissensbasis definiert.")
                
                if verbote:
                    for v in verbote:
                        st.error(f"⛔ **Untersagt für '{v['X']}':** {v['Action']}")
                if gebote:
                    for g in gebote:
                        st.warning(f"⚠️ **Geboten für '{g['X']}':** {g['Action']}")
                if erlaubnisse:
                    for e in erlaubnisse:
                        st.success(f"✅ **Gestattet für '{e['X']}':** {e['Action']}")
            else:
                st.warning("Die NLU konnte aus dem eingegebenen Text keine passenden Logik-Fakten derivieren.")
