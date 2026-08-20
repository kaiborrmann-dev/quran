import os
import streamlit as st
from pyswip import Prolog

# ------------------------------------------------------------------------------
# 1. SETUP
# ------------------------------------------------------------------------------
st.set_page_config(page_title="Koranische Normen-Inferenz", layout="wide")
st.title("Koranische Normen-Inferenz")
st.write("Direkte Abfrage der Regel-Prämissen aus der Wissensbasis.")

pl_file = "Koran_ethische_PROLOG_Regeln_bereinigt.pl"

if not os.path.exists(pl_file):
    st.error(f"Prolog-Datei '{pl_file}' wurde nicht gefunden!")
    st.stop()

# ------------------------------------------------------------------------------
# 2. DEFINITION DER REGELN (1:1 VORLAGE AUS DER .PL-DATEI)
# ------------------------------------------------------------------------------
# Hier werden die Ziel-Regeln und ihre exakten Prämissen direkt gespiegelt.

REGELN = {
    "Vielehe-Schranke (Sure 4:3)": {
        "ziel": "untersagt(zaid, eheschliessung)",
        "praemissen": [
            ("ist_glaeubig(zaid)", "Ist Zaid gläubig?"),
            ("anzahl_ehefrauen(zaid, 4)", "Hat Zaid aktuell bereits 4 Ehefrauen?"),
            ("beabsichtigt(zaid, eheschliessung)", "Beabsichtigt Zaid eine weitere Eheschließung?"),
            ("beabsichtigt_eheschliessung(zaid)", "Liegt die Absicht zur Eheschließung vor?")
        ]
    },
    "Zinsverbot / Ribā (Sure 2:275)": {
        "ziel": "untersagt(zaid, geschaeft1)",
        "praemissen": [
            ("ist_glaeubig(zaid)", "Ist Zaid gläubig?"),
            ("taetigt_transaktion(zaid, geschaeft1)", "Tätigt Zaid das Geschäft 'geschaeft1'?"),
            ("beinhaltet_riba(geschaeft1)", "Beinhaltet 'geschaeft1' Zinsen (Ribā)?")
        ]
    },
    "Wartezeit / 'Iddah (Sure 65:1)": {
        "ziel": "untersagt(zaid, evakuierung(amina))",
        "praemissen": [
            ("in_iddah_frist(amina, zaid)", "Befindet sich Amina in der 'Iddah-Wartezeit von Zaid?")
        ]
    }
}

# ------------------------------------------------------------------------------
# 3. INTERACTION & INFERENZ
# ------------------------------------------------------------------------------
ausgewaehlte_regel = st.selectbox("Wähle die zu prüfende Regel:", list(REGELN.keys()))

regel_data = REGELN[ausgewaehlte_regel]

st.markdown("---")
st.subheader("1. Gesuchte Konklusion (Ziel-Regel)")
st.code(f"Kopf: {regel_data['ziel']}", language="prolog")

st.subheader("2. Prämissen-Abfrage für den Modus Ponens")

gesetzte_fakten = []

# Erzeugt 1:1 Kontrollkästchen für jede geforderte Prämisse im Rumpf
for fakt_code, label in regel_data["praemissen"]:
    is_true = st.checkbox(f"{label}  👉  `{fakt_code}`", value=True)
    if is_true:
        gesetzte_fakten.append(fakt_code + ".")

st.markdown("---")
st.subheader("3. Aktivierte Faktenmenge A")
st.code("\n".join(gesetzte_fakten), language="prolog")

if st.button("⚖️ Modus Ponens auswerten", type="primary"):
    # Schreibt genau die aktivierten Fakten in eine temporäre Datei
    temp_file = "temp_direct_facts.pl"
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(":- dynamic ist_glaeubig/1.\n")
        f.write(":- dynamic anzahl_ehefrauen/2.\n")
        f.write(":- dynamic beabsichtigt/2.\n")
        f.write(":- dynamic beabsichtigt_eheschliessung/1.\n")
        f.write(":- dynamic in_iddah_frist/2.\n")
        f.write(":- dynamic taetigt_transaktion/2.\n")
        f.write(":- dynamic beinhaltet_riba/1.\n\n")
        for fkt in gesetzte_fakten:
            f.write(f"{fkt}\n")

    prolog = Prolog()
    prolog.consult(temp_file)
    prolog.consult(pl_file)

    st.subheader("4. Auswertung des Prolog-Kernels")
    
    # Exakte Ziel-Abfrage
    ziel_term = regel_data["ziel"]
    try:
        ergebnisse = list(prolog.query(ziel_term))
        if ergebnisse or (isinstance(ergebnisse, list) and len(ergebnisse) > 0):
            st.error(f"⛔ **MODUS PONENS ERFÜLLT:** `{ziel_term}` gilt als erwiesen.")
        else:
            st.info(f"ℹ️ **MODUS PONENS NICHT ERFÜLLT:** `{ziel_term}` lässt sich aus den gewählten Prämissen nicht ableiten.")
    except Exception as e:
        st.error(f"Fehler bei der Abfrage: {e}")
