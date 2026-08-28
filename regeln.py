# app.py - Streamlit Benutzeroberfläche für den koranischen Normen-Apparat

import streamlit as st
from regeln import KANON, evaluiere_norm

st.set_page_config(page_title="Koranischer Normen-Apparat", layout="centered")

st.title("Koranischer Normen-Apparat")
st.markdown("Systemische Analyse nach deontischer Reduktion und logischer Struktur.")

st.markdown("---")

# Auswahl der Norm aus dem Kanon
norm_optionen = {v["titel"]: k for k, v in KANON.items()}
auswahl_titel = st.selectbox("Normenkomplex wählen:", list(norm_optionen.keys()))
norm_id = norm_optionen[auswahl_titel]
regel = KANON[norm_id]

# Anzeige des Quelltextes und der Metadaten
st.markdown(f"**Offenbarungsquelle:** {regel.get('quelle', 'Koran')}")
st.markdown(f"> *{regel.get('text', '')}*")

st.subheader("Normen-Profil")
st.markdown(f"**Deontischer Vektor:** {regel['deontik']} (`{regel['operator_formel']}`)")
st.markdown(f"**Struktur-Typ:** {regel['struktur_typ']} — *{regel['beschreibung_struktur']}*")

st.markdown("---")

# Interaktive Eingabe für den Sachverhalt
st.subheader("Sachverhalt prüfen")

sachverhalt_fakten = []
sachverhalt_sperren = []

if regel["praemissen"]:
    st.markdown("##### Vorliegende Tatbestände (Prämissen):")
    for p in regel["praemissen"]:
        if st.checkbox(f"Tatbestand erfüllt: **{p}**", key=f"p_{p}"):
            sachverhalt_fakten.append(p)

if regel["sperren"]:
    st.markdown("##### Greifende Sperrtatbestände (Ausnahmen):")
    for s in regel["sperren"]:
        if st.checkbox(f"Sperre aktiv: **{s}**", key=f"s_{s}"):
            sachverhalt_sperren.append(s)

st.markdown("---")

# Auswertung starten
if st.button("Norm evaluieren"):
    ergebnis = evaluiere_norm(norm_id, sachverhalt_fakten, sachverhalt_sperren)
    
    st.subheader("Ergebnis der Evaluation")
    st.write(f"**Status:** {ergebnis['status']}")
    
    if ergebnis["ergebnis"]:
        st.success("Das Gebot/Verbot ist im aktuellen Sachverhalt bindend.")
    else:
        st.error("Die Norm greift im aktuellen Sachverhalt nicht (oder ist blockiert).")
