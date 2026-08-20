import os
import streamlit as st
from pyswip import Prolog

# ------------------------------------------------------------------------------
# 1. SETUP & INITIALISIERUNG
# ------------------------------------------------------------------------------
st.set_page_config(
    page_title="Koran-Normativität: Sokratische Logik-Inferenz", 
    layout="wide", 
    page_icon="🏛️"
)

def run_prolog_evaluation(facts):
    """
    Erstellt eine isolierte Prolog-Instanz, schreibt die ausgewählten 
    Prämissen A_i in ein temporäres Modul und berechnet den Modus Ponens.
    """
    facts_file = "temp_sokrates_facts.pl"
    pl_file = "Koran_ethische_PROLOG_Regeln_bereinigt.pl"
    
    with open(facts_file, "w", encoding="utf-8") as f:
        f.write(":- dynamic ist_glaeubig/1.\n")
        f.write(":- dynamic anzahl_ehefrauen/2.\n")
        f.write(":- dynamic beabsichtigt/2.\n")
        f.write(":- dynamic beabsichtigt_eheschliessung/1.\n")
        f.write(":- dynamic in_iddah_frist/2.\n")
        f.write(":- dynamic taetigt_transaktion/2.\n")
        f.write(":- dynamic beinhaltet_riba/1.\n\n")
        for fact in facts:
            f.write(f"{fact}\n")
            
    prolog = Prolog()
    prolog.consult(facts_file)
    
    if os.path.exists(pl_file):
        prolog.consult(pl_file)
    else:
        st.error(f"Prolog-Datei '{pl_file}' wurde im Repository nicht gefunden!")
        return [], [], []

    verbote, gebote, erlaubnisse = [], [], []
    
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
            
    return verbote, gebote, erlaubnisse

# ------------------------------------------------------------------------------
# 2. BENUTZEROBERFLÄCHE (SOKRATISCHE PRÄMISSEN-ABFRAGE)
# ------------------------------------------------------------------------------
st.title("🏛️ Koran-Normativität: Sokratische Logik-Inferenz")
st.caption("Deterministische Modus-Ponens-Auswertung auf Basis koranischer Tatbestandsmerkmale ($A \\rightarrow B$)")

st.markdown("---")

# 1. Thema / Normenkomplex wählen (Ziel B)
thema = st.selectbox(
    "1. Wählen Sie den zu prüfenden Normenkomplex (Ziel-Konklusion B):",
    [
        "Eherecht: Schranken der Vielehe (Sure 4:3)",
        "Wirtschaftsethik: Zinsverbot / Ribā (Sure 2:275)",
        "Familienrecht: Evakuierungsverbot während der 'Iddah (Sure 65:1)"
    ]
)

st.markdown("---")
st.subheader("2. Tatbestandsmerkmale & Prämissen-Belegung ($A_i$)")

facts_to_assert = []

# Dynamische Formular-Maske je nach gewähltem Thema
if "Schranken der Vielehe" in thema:
    col1, col2 = st.columns(2)
    
    with col1:
        akteur = st.selectbox("Akteur (X):", ["zaid", "amr"])
        ist_glaeubig = st.radio(f"A_1: Ist {akteur.capitalize()} Gläubiger?", ["Ja", "Nein"], index=0)
        
    with col2:
        anzahl_ehen = st.number_input(f"A_2: Bestehende Ehen von {akteur.capitalize()} (N):", min_value=0, max_value=10, value=4)
        beabsichtigt = st.radio(f"A_3: Beabsichtigt {akteur.capitalize()} eine weitere Eheschließung?", ["Ja", "Nein"], index=0)

    # Konstruktion der präzisen Prämissenmenge A
    if ist_glaeubig == "Ja":
        facts_to_assert.append(f"ist_glaeubig({akteur}).")
    facts_to_assert.append(f"anzahl_ehefrauen({akteur}, {anzahl_ehen}).")
    if beabsichtigt == "Ja":
        facts_to_assert.append(f"beabsichtigt({akteur}, eheschliessung).")
        facts_to_assert.append(f"beabsichtigt_eheschliessung({akteur}).")

elif "Zinsverbot" in thema:
    akteur = st.selectbox("Akteur (X):", ["zaid", "amr"])
    ist_glaeubig = st.radio(f"A_1: Ist {akteur.capitalize()} Gläubiger?", ["Ja", "Nein"], index=0)
    beinhaltet_riba = st.radio("A_2: Beinhaltet die Finanztransaktion Zins/Ribā?", ["Ja", "Nein"], index=0)
    
    if ist_glaeubig == "Ja":
        facts_to_assert.append(f"ist_glaeubig({akteur}).")
    if beinhaltet_riba == "Ja":
        facts_to_assert.append(f"taetigt_transaktion({akteur}, t1).")
        facts_to_assert.append("beinhaltet_riba(t1).")

elif "Iddah" in thema:
    akteur = st.selectbox("Akteur (X):", ["zaid", "amr"])
    partnerin = "amina"
    in_iddah = st.radio(f"A_1: Befindet sich {partnerin.capitalize()} in der Wartezeit ('Iddah) von {akteur.capitalize()}?", ["Ja", "Nein"], index=0)
    
    if in_iddah == "Ja":
        facts_to_assert.append(f"in_iddah_frist({partnerin}, {akteur}).")

st.markdown("---")
st.subheader("3. Formale Logik-Repräsentation")

st.write("Generierte Prämissenmenge $A$ für den Prolog-Kernel:")
st.code("\n".join(facts_to_assert), language="prolog")

# 3. Inferenz per Klick
if st.button("⚖️ Modus Ponens berechnen", type="primary"):
    verbote, gebote, erlaubnisse = run_prolog_evaluation(facts_to_assert)
    
    st.subheader("4. Berechnete Rechtsfolge (Prolog Kernel)")
    
    if not (verbote or gebote or erlaubnisse):
        st.info("Prämissen unvollständig oder Tatbestand nicht erfüllt: Keine Rechtsfolge ausgelöst.")
    
    if verbote:
        for v in verbote:
            st.error(f"⛔ **Untersagt für '{v['X']}':** {v['Action']}")
    if gebote:
        for g in gebote:
            st.warning(f"⚠️ **Geboten für '{g['X']}':** {g['Action']}")
    if erlaubnisse:
        for e in erlaubnisse:
            st.success(f"✅ **Gestattet für '{e['X']}':** {e['Action']}")
