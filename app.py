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
# 2. DYNAMISCHE NLU-PIPELINE (OPENAI GPT) WITH CLOSED WORLD (ZAID / AMR)
# ------------------------------------------------------------------------------
def extract_prolog_facts(client, user_text):
    system_prompt = """
Du bist ein hochpräziser NLU-Parser für ein koranisches Rechts- und Ethik-Logiksystem in SWI-Prolog.
Deine Aufgabe ist es, beliebigen Freitext in valide Prolog-Fakten (nur Kleinschreibung, snake_case) zu übersetzen.

DISKURS-UNIVERSUM (FESTE AKTEURE):
1. Es existieren ausschließlich zwei primäre männliche Akteure: 'zaid' und 'amr'.
2. Wenn der Text in der 1. Person ("ich"), ohne explizite Namensnennung oder mit unbestimmten Subjekten verfasst ist, wähle IMMER 'zaid' als Primärakteur.
3. Ergänze für den aktiven Hauptakteur stets das Grund-Axiom: ist_glaeubig(Akteur).

TRANSLATIONS-REGELN:
- "fünfte Frau heiraten" / "weitere Ehe" ->
  - ist_glaeubig(zaid)
  - anzahl_ehefrauen(zaid, 4)
  - beabsichtigt(zaid, eheschliessung)
- Relationale Handlungen zwischen zwei Personen nutzen 'zaid' (Akteur) und 'amr' (Gegenüber).

Gib das Ergebnis STRIKT als JSON-Array von Strings zurück.
Beispiel für "Kann Zaid eine 5. Frau heiraten?":
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
        st.error(f"Fehler bei der NLU-Anfrage: {e}")
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
                    dynamic_predicates = [
                        "beabsichtigt_eheschliessung/1", "beabsichtigt/2", 
                        "anzahl_ehefrauen/2", "ist_glaeubig/1", 
                        "in_iddah_frist/2", "taetigt_transaktion/2", "beinhaltet_riba/1"
                    ]
                    for pred in dynamic_predicates:
                        try:
                            list(prolog.query(f"dynamic({pred})"))
                        except Exception:
                            pass
                    
                    # Altdaten bereinigen
                    prolog.retractall("beabsichtigt_eheschliessung(_)")
                    prolog.retractall("beabsichtigt(_, _)")
                    prolog.retractall("anzahl_ehefrauen(_, _)")
                    prolog.retractall("in_iddah_frist(_, _)")
                    prolog.retractall("ist_glaeubig(_)")
                    
                    # Fakten einspeisen
                    for fact in extracted_facts:
                        try:
                            prolog.assertz(fact)
                        except Exception as e:
                            st.caption(f"Lade-Hinweis ({fact}): {e}")
                    
                    # Inferenz-Abfragen explizit für zaid und amr
                    verbote, gebote, erlaubnisse = [], [], []
                    akteure = ["zaid", "amr"]
                    
                    for akteur in akteure:
                        try:
                            res_v = list(prolog.query(f"untersagt({akteur}, Action)"))
                            for item in res_v:
                                verbote.append({"X": akteur, "Action": item["Action"]})
                        except Exception:
                            pass
                            
                        try:
                            res_g = list(prolog.query(f"gebietet({akteur}, Action)"))
                            for item in res_g:
                                gebote.append({"X": akteur, "Action": item["Action"]})
                        except Exception:
                            pass
                            
                        try:
                            res_e = list(prolog.query(f"gestattet({akteur}, Action)"))
                            for item in res_e:
                                erlaubnisse.append({"X": akteur, "Action": item["Action"]})
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
                st.warning("Die NLU konnte aus dem eingegebenen Text keine passenden Logik-Fakten ableiten.")
