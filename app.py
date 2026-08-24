import streamlit as st
from regeln import KANON

# ------------------------------------------------------------------------------
# 1. ARCHITEKTUR & SEITEN-SETUP
# ------------------------------------------------------------------------------
st.set_page_config(page_title="Koranischer Normen-Apparat", layout="centered")

st.title("Koranischer Normen-Apparat")
st.write("Modus-Ponens-Evaluator mit epistemischer Status-Klassifikation.")

st.markdown("---")

# ------------------------------------------------------------------------------
# 2. BENUTZEROBERFLÄCHE
# ------------------------------------------------------------------------------
sortierte_ids = sorted(KANON.keys())
auswahl_id = st.selectbox("Normenkomplex wählen:", sortierte_ids, format_func=lambda x: KANON[x]["titel"])
regel = KANON[auswahl_id]

st.markdown(f"**Offenbarungsquelle:** {regel['quelle']}")

st.markdown("---")
st.subheader("Normativer Gegenstand")
st.code(regel["ziel"], language="prolog")

st.subheader("Sachverhalt (Fakten & Sperren)")

aktive_fakten = set()

if regel["positive"]:
    st.markdown("Erforderliche Tatbestandsmerkmale:")
    for code, label in regel["positive"]:
        if st.checkbox(f"{label} (`{code}`)", value=True):
            aktive_fakten.add(code)

if regel["sperren"]:
    st.markdown("Ausnahmen / Sperrtatbestände:")
    for code, label in regel["sperren"]:
        if st.checkbox(f"[Sperre] {label} (`{code}`)", value=False):
            aktive_fakten.add(code)

st.markdown("---")
st.subheader("Aktiver Arbeitsspeicher (Wissen W)")
if aktive_fakten:
    st.code("\n".join([f"{f}." for f in aktive_fakten]), language="prolog")
else:
    st.code("% Wissen W ist leer", language="prolog")

# ------------------------------------------------------------------------------
# 3. INFERENZ & WESSEL-KLASSIFIKATION
# ------------------------------------------------------------------------------
if st.button("Auswertung starten", type="primary"):
    ziel_term = regel["ziel"]
    
    st.subheader("Auswertung & Epistemischer Status")
    
    erfuellt = True
    protokoll = []
    
    for code, _ in regel["positive"]:
        if code not in aktive_fakten:
            erfuellt = False
            protokoll.append(f"Fehlende Prämisse: {code}")
            
    for code, _ in regel["sperren"]:
        if code in aktive_fakten:
            erfuellt = False
            protokoll.append(f"Sperrtatbestand aktiv: {code}")
            
    # Wessel-Klassifikation
    w_vdash_a = erfuellt
    w_is_empty = (len(aktive_fakten) == 0)
    
    # Textliche Ableitung des normativen Inhalts aus dem Ziel-Term (z.B. gebietet/untersagt)
    norm_titel = regel["titel"]
    if "gebietet" in ziel_term:
        norm_text = f"Das Gebot ({norm_titel})"
    elif "untersagt" in ziel_term:
        norm_text = f"Das Verbot ({norm_titel})"
    else:
        norm_text = f"Die Normregelung ({norm_titel})"

    if w_vdash_a:
        status_text = "D1: Beweisbar bezüglich W (W ⊢ A)"
        befund = f"{norm_text} ist aus der obigen Regel und dem entsprechenden Sachverhalt ableitbar."
    else:
        if w_is_empty:
            status_text = "D2: Unbeweisbar bezüglich W (~(W ⊢ A))"
            befund = f"{norm_text} ist nicht ableitbar, da das Wissensarchiv W leer ist."
        else:
            status_text = "D5: Unentscheidbar bezüglich W"
            befund = f"{norm_text} ist unentscheidbar; die vorhandenen Fakten greifen nicht oder besitzen keinen Bezug zur Regel."

    if erfuellt:
        st.markdown(f"**Ergebnis:** Der Modus Ponens ist **erfüllt**. `{ziel_term}` ist bewiesen.")
    else:
        gruende = "\n".join([f"- {p}" for p in protokoll])
        st.markdown(f"**Ergebnis:** Der Modus Ponens ist **nicht erfüllt**.\n\nUrsachen:\n{gruende}")

    st.markdown("---")
    st.markdown(f"**Epistemischer Status:** `{status_text}`")
    st.markdown(f"*Befund:* {befund}")
