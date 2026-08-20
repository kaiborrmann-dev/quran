import os
import streamlit as st
from pyswip import Prolog

# ------------------------------------------------------------------------------
# 1. INITIALISIERUNG & SEITEN-EINSTELLUNG
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Koranische Normen-Inferenz", 
    layout="wide"
)

def evaluiere_prufung(fakten_liste):
    """
    Schreibt die eingegebenen Merkmale in eine temporäre Datei 
    und berechnet die Rechtsfolge im Prolog-Kernel.
    """
    temp_file = "temp_fakten.pl"
    pl_file = "Koran_ethische_PROLOG_Regeln_bereinigt.pl"
    
    with open(temp_file, "w", encoding="utf-8") as f:
        f.write(":- dynamic ist_glaeubig/1.\n")
        f.write(":- dynamic anzahl_ehefrauen/2.\n")
        f.write(":- dynamic beabsichtigt/2.\n")
        f.write(":- dynamic beabsichtigt_eheschliessung/1.\n")
        f.write(":- dynamic in_iddah_frist/2.\n")
        f.write(":- dynamic taetigt_transaktion/2.\n")
        f.write(":- dynamic beinhaltet_riba/1.\n\n")
        for fakt in fakten_liste:
            f.write(f"{fakt}\n")
            
    prolog = Prolog()
    prolog.consult(temp_file)
    
    if os.path.exists(pl_file):
        prolog.consult(pl_file)
    else:
        st.error(f"Die Regel-Datei '{pl_file}' wurde nicht im Ordner gefunden.")
        return [], [], []

    verbote, gebote, erlaubnisse = [], [], []
    
    for person in ["zaid", "amr"]:
        try:
            res_v = list(prolog.query(f"untersagt({person}, Handlung)"))
            for eintrag in res_v:
                verbote.append({"Person": person, "Handlung": str(eintrag["Handlung"])})
        except Exception:
            pass

        try:
            res_g = list(prolog.query(f"gebietet({person}, Handlung)"))
            for eintrag in res_g:
                gebote.append({"Person": person, "Handlung": str(eintrag["Handlung"])})
        except Exception:
            pass

        try:
            res_e = list(prolog.query(f"gestattet({person}, Handlung)"))
            for eintrag in res_e:
                erlaubnisse.append({"Person": person, "Handlung": str(eintrag["Handlung"])})
        except Exception:
            pass
            
    return verbote, gebote, erlaubnisse

# ------------------------------------------------------------------------------
# 2. BENUTZEROBERFLÄCHE (FORMULAR)
# ------------------------------------------------------------------------------
st.title("Koranische Normen-Inferenz")
st.write("Wählen Sie den Themenbereich und stellen Sie die konkreten Merkmale ein.")

st.markdown("---")

# Themen-Auswahl
thema = st.selectbox(
    "Themenbereich wählen:",
    [
        "Eherecht: Schranken der Vielehe",
        "Wirtschaftsrecht: Zinsverbot (Ribā)",
        "Familienrecht: Wartezeit ('Iddah)"
    ]
)

st.markdown("---")

fakten_liste = []

# Formularfelder je nach Thema
if thema == "Eherecht: Schranken der Vielehe":
    st.subheader("Merkmale für das Eherecht")
    
    col1, col2 = st.columns(2)
    with col1:
        person = st.selectbox("Betroffene Person:", ["zaid", "amr"])
        glaeubig = st.radio("Ist die Person gläubig?", ["Ja", "Nein"], index=0)
    
    with col2:
        bestehende_ehen = st.number_input("Bestehende Ehen (Anzahl):", min_value=0, max_value=10, value=4)
        absicht_heirat = st.radio("Beabsichtigt eine weitere Eheschließung?", ["Ja", "Nein"], index=0)
    
    # Fakten zusammensetzen
    if glaeubig == "Ja":
        fakten_liste.append(f"ist_glaeubig({person}).")
    fakten_liste.append(f"anzahl_ehefrauen({person}, {bestehende_ehen}).")
    if absicht_heirat == "Ja":
        fakten_liste.append(f"beabsichtigt({person}, eheschliessung).")
        fakten_liste.append(f"beabsichtigt_eheschliessung({person}).")

elif thema == "Wirtschaftsrecht: Zinsverbot (Ribā)":
    st.subheader("Merkmale für Finanzgeschäfte")
    
    person = st.selectbox("Betroffene Person:", ["zaid", "amr"])
    glaeubig = st.radio("Ist die Person gläubig?", ["Ja", "Nein"], index=0)
    zins_enthalten = st.radio("Enthält das Geschäft Zinsen (Ribā)?", ["Ja", "Nein"], index=0)
    
    if glaeubig == "Ja":
        fakten_liste.append(f"ist_glaeubig({person}).")
    if zins_enthalten == "Ja":
        fakten_liste.append(f"taetigt_transaktion({person}, geschaeft1).")
        fakten_liste.append("beinhaltet_riba(geschaeft1).")

elif thema == "Familienrecht: Wartezeit ('Iddah)":
    st.subheader("Merkmale für die Wartezeit")
    
    person = st.selectbox("Betroffene Person:", ["zaid", "amr"])
    partnerin = "amina"
    in_wartezeit = st.radio(f"Befindet sich {partnerin.capitalize()} in der Wartezeit von {person.capitalize()}?", ["Ja", "Nein"], index=0)
    
    if in_wartezeit == "Ja":
        fakten_liste.append(f"in_iddah_frist({partnerin}, {person}).")

st.markdown("---")

# Anzeige der im Hintergrund gesetzten Fakten
st.subheader("Erfasste Merkmale (Eingabe)")
st.code("\n".join(fakten_liste), language="prolog")

# Auswertung
if st.button("Rechtsfolge auswerten", type="primary"):
    verbote, gebote, erlaubnisse = evaluiere_prufung(fakten_liste)
    
    st.subheader("Ergebnis der Auswertung")
    
    if not (verbote or gebote or erlaubnisse):
        st.info("Die eingegebenen Merkmale lösen keine direkte Rechtsfolge nach den hinterlegten Regeln aus.")
    
    if verbote:
        for v in verbote:
            st.error(f"Untersagt für {v['Person'].capitalize()}: {v['Handlung']}")
    if gebote:
        for g in gebote:
            st.warning(f"Geboten für {g['Person'].capitalize()}: {g['Handlung']}")
    if erlaubnisse:
        for e in erlaubnisse:
            st.success(f"Gestattet für {e['Person'].capitalize()}: {e['Handlung']}")
