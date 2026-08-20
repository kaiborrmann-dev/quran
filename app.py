import os
import streamlit as st
from pyswip import Prolog

# ------------------------------------------------------------------------------
# 1. SETUP & CONFIGURATION
# ------------------------------------------------------------------------------
st.set_page_config(page_title="Koranische Normen-Inferenz", layout="wide")
st.title("Koranische Normen-Inferenz")
st.write("Direkte Abfrage der Regel-Prämissen aus der Wissensbasis.")

pl_file = "Koran_ethische_PROLOG_Regeln_bereinigt.pl"

if not os.path.exists(pl_file):
    st.error(f"Prolog-Datei '{pl_file}' wurde im Repository nicht gefunden!")
    st.stop()

# ------------------------------------------------------------------------------
# 2. DEFINITION DER REGELN & PRÄMISSEN
# ------------------------------------------------------------------------------
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
# 3. INTERAKTION & EVALUATION
# ------------------------------------------------------------------------------
ausgewaehlte_regel = st.selectbox("Wähle die zu prüfende Regel:", list(REGELN.keys()))
regel_data = REGELN[ausgewaehlte_regel]

st.markdown("---")
st.subheader("1. Gesuchte Konklusion (Ziel-Regel)")
st.code(f"Kopf: {regel_data['ziel']}", language="prolog")

st.subheader("2. Prämissen-Abfrage für den Modus Ponens")

gesetzte_fakten = []

for fakt_code, label in regel_data["praemissen"]:
    is_true = st.checkbox(f"{label}  👉  `{fakt_code}`", value=True)
    if is_true:
        gesetzte_fakten.append(fakt_code)

st.markdown("---")
st.subheader("3. Aktivierte Faktenmenge A")
st.code("\n".join(gesetzte_fakten), language="prolog")

if st.button("⚖️ Modus Ponens auswerten", type="primary"):
    prolog = Prolog()
    
    try:
        # Zuerst die Wissensbasis laden
        prolog.consult(pl_file)
        
        # Ausgewählte Fakten via assertz einspeisen
        for fkt in gesetzte_fakten:
            prolog.assertz(fkt)
            
        ziel_term = regel_data["ziel"]
        res = list(prolog.query(ziel_term))
        
        st.subheader("4. Auswertung des Prolog-Kernels")
        
        # PySWIP liefert bei erfüllter grundierter Aussage [{}] (Länge > 0)
        if len(res) > 0:
            st.error(f"⛔ **MODUS PONENS ERFÜLLT:** `{ziel_term}` gilt als erwiesen.")
        else:
            st.info(f"ℹ️ **MODUS PONENS NICHT ERFÜLLT:** `{ziel_term}` lässt sich aus den gewählten Prämissen nicht ableiten.")
            
    except Exception as e:
        st.error(f"Fehler bei der Prolog-Ausführung: {e}")
