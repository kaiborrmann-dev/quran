import os
import streamlit as st
from pyswip import Prolog

# ------------------------------------------------------------------------------
# 1. SETUP
# ------------------------------------------------------------------------------
st.set_page_config(page_title="Koranische Normen-Inferenz", layout="wide")
st.title("Koranische Normen-Inferenz")
st.write("Direkte Modus-Ponens-Auswertung auf Basis der echten Prolog-Regeln.")

pl_file = "Koran_ethische_PROLOG_Regeln_bereinigt.pl"

if not os.path.exists(pl_file):
    st.error(f"Prolog-Datei '{pl_file}' wurde im Repository nicht gefunden!")
    st.stop()

# ------------------------------------------------------------------------------
# 2. ECHTE REGELN AUS DER WISSENSBASIS
# ------------------------------------------------------------------------------
REGELN = {
    "K-004: Zinsverbot (Ribā)": {
        "ziel": "untersagt(zaid, vollzug_transaktion(geschaeft1))",
        "praemissen": [
            ("taetigt_transaktion(zaid, geschaeft1)", "Tätigt Zaid das Geschäft 'geschaeft1'?"),
            ("beinhaltet_riba(geschaeft1)", "Enthält 'geschaeft1' Zinsen (Ribā)?")
        ]
    },
    "K-003: Fastenpflicht (Ramadan)": {
        "ziel": "gebietet(zaid, fasten_ramadan)",
        "praemissen": [
            ("ist_glaeubig(zaid)", "Ist Zaid gläubig?"),
            ("krank(zaid)", "Ist Zaid krank? (Für Pflicht: Häkchen WEGLASSEN)"),
            ("auf_reisen(zaid)", "Ist Zaid auf Reisen? (Für Pflicht: Häkchen WEGLASSEN)")
        ]
    },
    "K-015: Ausweisungsverbot in der Wartezeit ('Iddah)": {
        "ziel": "untersagt(zaid, ausweisung_aus_ehewohnung(amina))",
        "praemissen": [
            ("in_iddah_frist(amina, zaid)", "Befindet sich Amina in der 'Iddah-Frist von Zaid?")
        ]
    },
    "K-006: Eheverbot (Maḥram)": {
        "ziel": "untersagt(zaid, eheschliessung(fathima))",
        "praemissen": [
            ("ist_mahram(zaid, fathima)", "Ist Fathima ein Maḥram-Verwandtenstatus für Zaid?")
        ]
    }
}

# ------------------------------------------------------------------------------
# 3. BENUTZEROBERFLÄCHE
# ------------------------------------------------------------------------------
ausgewaehlte_regel = st.selectbox("Normenkomplex wählen:", list(REGELN.keys()))
regel_data = REGELN[ausgewaehlte_regel]

st.markdown("---")
st.subheader("1. Zu prüfender Regelkopf (Konklusion B)")
st.code(regel_data["ziel"], language="prolog")

st.subheader("2. Prämissenbelegung für den Modus Ponens (A)")

gesetzte_fakten = []

for fakt_code, label in regel_data["praemissen"]:
    # Für Negations-Prämissen (\+) in Prolog muss das Häkchen weggelassen werden
    is_checked = st.checkbox(f"{label}  👉  `{fakt_code}`", value=True)
    if is_checked:
        gesetzte_fakten.append(fakt_code)

st.markdown("---")
st.subheader("3. Aktivierte Faktenmenge A")
st.code("\n".join(gesetzte_fakten), language="prolog")

if st.button("⚖️ Modus Ponens berechnen", type="primary"):
    session_file = "temp_session.pl"
    
    # Schreibvorgang mit strikter Trennung
    with open(session_file, "w", encoding="utf-8") as f:
        # 1. Dynamische Deklarationen aus der Hauptdatei sichern
        f.write(":- dynamic taetigt_transaktion/2.\n")
        f.write(":- dynamic beinhaltet_riba/1.\n")
        f.write(":- dynamic ist_glaeubig/1.\n")
        f.write(":- dynamic krank/1.\n")
        f.write(":- dynamic auf_reisen/1.\n")
        f.write(":- dynamic in_iddah_frist/2.\n")
        f.write(":- dynamic ist_mahram/2.\n\n")
        
        # 2. Fakten schreiben
        for fkt in gesetzte_fakten:
            f.write(f"{fkt}.\n")
            
        f.write("\n")
        # 3. Haupt-Wissensbasis laden
        f.write(f":- include('{pl_file}').\n")

    try:
        prolog = Prolog()
        prolog.consult(session_file)
        
        ziel_term = regel_data["ziel"]
        res = list(prolog.query(ziel_term))
        
        st.subheader("4. Ergebnis des Prolog-Kernels")
        
        if len(res) > 0:
            st.error(f"⛔ **MODUS PONENS ERFÜLLT:** `{ziel_term}` ist aus den Prämissen logisch bewiesen.")
        else:
            st.info(f"ℹ️ **MODUS PONENS NICHT ERFÜLLT:** `{ziel_term}` lässt sich aus den gewählten Prämissen nicht ableiten.")
            
    except Exception as e:
        st.error(f"Prolog-Fehler: {e}")
