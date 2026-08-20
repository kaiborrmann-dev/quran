import os
import json
import streamlit as st
from openai import OpenAI
from pyswip import Prolog

# ------------------------------------------------------------------------------
# 1. SETUP & INITIALISIERUNG
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Koran-Normativität: Dynamische NLU & Inferenz", 
    layout="wide", 
    page_icon="🏛️"
)

# OpenAI Client initialisieren
@st.cache_resource
def init_openai():
    api_key = st.secrets.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        st.error("Kein OPENAI_API_KEY in den Streamlit Secrets gefunden!")
        return None
    return OpenAI(api_key=api_key)

# SWI-Prolog Engine laden
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
# 2. GENERATIVE NLU-PIPELINE (UNIVERSELLER TEXT-ZU-PROLOG PARSER)
# ------------------------------------------------------------------------------
def extract_prolog_facts(client, user_text):
    system_prompt = """
Du bist ein universeller NLU-Parser für ein koranisches Rechts- und Ethik-Logiksystem in Prolog.
Deine Aufgabe ist es, beliebigen deutschen Freitext präzise zu analysieren und in valide Prolog-Fakten zu übersetzen.

Regeln zur Fakten-Generierung:
1. Verwende ausschließlich Kleinschreibung und Snake_Case für Prädikate und Konstanten (z.B. zaid, ehefrau, eheschliessung).
2. Extrahiere Akteure und Status (z.B. ist_glaeubig(zaid), status(zaid, verheiratet)).
3. Extrahiere Quantitäten & Zählwerte (z.B. anzahl_ehefrauen(zaid, 4)).
4. Extrahiere Absichten & Handlungen (z.B. beabsichtigt(zaid, eheschliessung), spricht_talaq_aus(zaid, amina)).
5. Extrahiere Kontext-, Frist- & Raumkonditionen (z.B. in_iddah_frist(amina, zaid), im_zustand_ihram(zaid)).

Gib das Ergebnis STRIKT als JSON-Array von Prolog-Fakten-Strings zurück.
Beispiel-Antwort:
[
  "ist_glaeubig(zaid)",
  "anzahl_ehefrauen(zaid, 4)",
  "beabsichtigt(zaid, eheschliessung)"
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
            temperature=0.1
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
        st.error(f"Fehler bei der NLU-Extraktion: {e}")
        return []

# ------------------------------------------------------------------------------
# 3. BENUTZEROBERFLÄCHE & LOGIK-EVALUATION
# ------------------------------------------------------------------------------
st.title("🏛️ Koran-Normativität: KI-NLU & Logik-Inferenz")
st.caption("Generatives Natural Language Understanding (OpenAI GPT) gekoppelt mit formaler SWI-Prolog Inferenz")

user_input = st.text_area(
    "Geben Sie einen beliebigen Sachverhalt in eigener Sprache ein:",
    height=100,
    placeholder="Beispiel: Zaid ist Gläubiger, hat bereits 4 Frauen und möchte eine weitere Ehe schließen..."
)

if st.button("⚖️ Sachverhalt via NLU & Prolog auswerten", type="primary"):
    if not user_input.strip():
        st.warning("Bitte geben Sie zuerst einen Text ein.")
    else:
        client = init_openai()
        if client:
            with st.spinner("1. Generative NLU extrahiert logische Fakten..."):
                extracted_facts = extract_prolog_facts(client, user_input)
                
            st.subheader("1. Extrahierter NLU-Kontext (Prolog-Fakten)")
            if extracted_facts:
                st.json(extracted_facts)
                
                with st.spinner("2. SWI-Prolog rechnet deontische Inferenz durch..."):
                    # Dynamischen Arbeitsspeicher vor Inferenz bereinigen
                    for predicate in [
                        "in_iddah_frist/2", "taetigt_transaktion/2", "beinhaltet_riba/1", 
                        "ist_glaeubig/1", "anzahl_ehefrauen/2", "beabsichtigt/2"
                    ]:
                        try:
                            prolog.retractall(f"{predicate.split('/')[0]}(_)")
                        except Exception:
                            pass
                    
                    # Extrahierte Fakten in den Arbeitsbereich laden
                    for fact in extracted_facts:
                        try:
                            prolog.assertz(fact)
                        except Exception as pe:
                            st.caption(f"Hinweis zu Fakt `{fact}`: {pe}")
                    
                    # Deontische Abfragen ausführen
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
