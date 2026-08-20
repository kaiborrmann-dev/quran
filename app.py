import os
import json
import streamlit as st
from google import genai
from google.genai import types
from pyswip import Prolog

# ------------------------------------------------------------------------------
# 1. SETUP & INITIALISIERUNG
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Koran-Normativität: Dynamische NLU & Inferenz", 
    layout="wide", 
    page_icon="🏛️"
)

# Gemini Client initialisieren (Greift automatisch auf GEMINI_API_KEY in Secrets zu)
@st.cache_resource
def init_gemini():
    api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if not api_key:
        st.error("Kein GEMINI_API_KEY in den Streamlit Secrets hinterlegt!")
        return None
    return genai.Client(api_key=api_key)

# Prolog-Engine laden
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
# 2. NLU-PARSER PROMPT (TEXT-ZU-PROLOG-FAKTEN)
# ------------------------------------------------------------------------------
def extract_prolog_facts(client, user_text):
    system_prompt = """
Du bist ein NLU-Parser für ein koranisches Rechts- und Ethik-Logiksystem in Prolog.
Deine Aufgabe ist es, freien Fließtext zu analysieren und in exakte Prolog-Fakten unseres Vokabulars zu übersetzen.

Nutze ausschließlich folgende Prädikats-Strukturen, falls sie auf den Sachverhalt zutreffen:
- ist_glaeubig(Person)
- ehemann_verstorben(Person)
- in_iddah_frist(Frau, Mann)
- spricht_talaq_aus(Mann, Frau)
- taetigt_transaktion(Person, TransaktionId)
- ist_wirtschaftstransaktion(TransaktionId)
- beinhaltet_riba(TransaktionId)
- beinhaltet_tatfif(TransaktionId)
- im_zustand_ihram(Person)
- toetet_landtier(Person, Tier)
- anvertraut_vermoegen(Person)

Gib das Ergebnis STRIKT als JSON-Array von Strings zurück, ohne Markdown-Formatierung außerhalb des JSON.
Beispiel-Antwort:
[
  "ist_glaeubig(zaid)",
  "in_iddah_frist(amina, zaid)"
]
"""
    
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=user_text,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            response_mime_type="application/json",
            temperature=0.1
        )
    )
    
    try:
        facts = json.loads(response.text)
        return facts
    except Exception as e:
        st.error(f"Fehler beim Parsen der NLU-Antwort: {e}")
        return []

# ------------------------------------------------------------------------------
# 3. BENUTZEROBERFLÄCHE
# ------------------------------------------------------------------------------
st.title("🏛️ Koran-Normativität: KI-NLU & Logik-Inferenz")
st.caption("Ein hybrides System aus Natural Language Understanding (Gemini API) und formaler Logik (SWI-Prolog)")

user_input = st.text_area(
    "Geben Sie einen beliebigen Sachverhalt in eigener Sprache ein:",
    height=100,
    placeholder="Zaid ist Gläubiger und hat sich von Amina getrennt. Sie ist aktuell in der Wartezeit. Er überlegt, sie aus der Wohnung zu weisen..."
)

if st.button("⚖️ Sachverhalt via NLU & Prolog auswerten", type="primary"):
    if not user_input.strip():
        st.warning("Bitte geben Sie zuerst einen Text ein.")
    else:
        client = init_gemini()
        if client:
            with st.spinner("1. NLU analysiert Fließtext und extrahiert formale Fakten..."):
                extracted_facts = extract_prolog_facts(client, user_input)
                
            st.subheader("1. Extrahierter NLU-Kontext (Fakten)")
            if extracted_facts:
                st.json(extracted_facts)
                
                # Fakten dynamisch in die Prolog-Engine laden
                with st.spinner("2. SWI-Prolog rechnet deontische Inferenz durch..."):
                    prolog.retractall("in_iddah_frist(_, _)")
                    prolog.retractall("taetigt_transaktion(_, _)")
                    prolog.retractall("beinhaltet_riba(_)")
                    
                    for fact in extracted_facts:
                        prolog.assertz(fact)
                    
                    verbote = list(prolog.query("untersagt(X, Action)"))
                    gebote = list(prolog.query("gebietet(X, Action)"))
                    erlaubnisse = list(prolog.query("gestattet(X, Action)"))
                    
                st.subheader("2. Berechnete Inferenz-Ergebnisse (Prolog Kernel)")
                
                if not (verbote or gebote or erlaubnisse):
                    st.info("Keine spezifischen normativen Verbote oder Gebote für die erkannten Fakten in der Wissensbasis gefunden.")
                
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
                st.warning("Die NLU konnte aus dem eingegebenen Text keine passenden Logik-Fakten ableiten.")