import streamlit as st
from regeln import KANON

# ------------------------------------------------------------------------------
# 1. ARCHITEKTUR & SEITEN-SETUP
# ------------------------------------------------------------------------------
st.set_page_config(page_title="Koranische Normen-Inferenz (Core Engine)", layout="wide")
st.title("🏛️ Koranischer Normen-Apparat (Minimal Core Engine)")
st.write("Deterministischer Modus-Ponens-Evaluator mit modularem 108-Regeln-Kanon und echter NAF-Semantik.")

# ------------------------------------------------------------------------------
# 2. BENUTZEROBERFLÄCHE (DETERMINISTISCHES FORMULAR)
# ------------------------------------------------------------------------------
# Sortierte Auswahl der Normen nach ID
sortierte_ids = sorted(KANON.keys())
auswahl_id = st.selectbox("Normenkomplex auswählen:", sortierte_ids, format_func=lambda x: KANON[x]["titel"])
regel = KANON[auswahl_id]

# Offenbarungsquelle prominent ausgeben
st.info(f"📖 **Koranische Offenbarungsquelle:** {regel['quelle']}")

st.markdown("---")
st.subheader("1. Zu prüfender Regelkopf (Konklusion B)")
st.code(regel["ziel"], language="prolog")

st.subheader("2. Sachverhalts-Erfassung (Fakten & Sperren)")

aktive_fakten = set()

# Positive Bedingungen abfragen
if regel["positive"]:
    st.markdown("**Erforderliche Tatbestandsmerkmale (Positive Bedingungen):**")
    for code, label in regel["positive"]:
        if st.checkbox(f"✅ {label}  👉  `{code}`", value=True):
            aktive_fakten.add(code)

# Sperrtatbestände (Negation as Failure) abfragen
if regel["sperren"]:
    st.markdown("**Mögliche Ausnahmen / Sperrtatbestände (NAF):**")
    for code, label in regel["sperren"]:
        if st.checkbox(f"⚠️ [Sperre] {label}  👉  `{code}`", value=False):
            aktive_fakten.add(code)

st.markdown("---")
st.subheader("3. Aktive Faktenmenge im Arbeitsspeicher")
if aktive_fakten:
    st.code("\n".join([f"{f}." for f in aktive_fakten]), language="prolog")
else:
    st.code("% Keine Fakten aktiv", language="prolog")

# ------------------------------------------------------------------------------
# 4. DIE INFERENZ-KERNFUNKTION (MODUS PONENS MIT NAF)
# ------------------------------------------------------------------------------
if st.button("⚖️ Modus Ponens ausführen", type="primary"):
    ziel_term = regel["ziel"]
    
    st.subheader("4. Inferenz-Ergebnis")
    
    erfuellt = True
    protokoll = []
    
    # 1. Alle positiven Bedingungen prüfen (Müssen in aktive_fakten sein)
    for code, _ in regel["positive"]:
        if code not in aktive_fakten:
            erfuellt = False
            protokoll.append(f"❌ Fehlende positive Bedingung: `{code}`")
            
    # 2. Alle Sperren prüfen (NAF: Dürfen NICHT in aktive_fakten sein)
    for code, _ in regel["sperren"]:
        if code in aktive_fakten:
            erfuellt = False
            protokoll.append(f"⛔ Sperrtatbestand greift (blockiert Norm): `{code}`")
            
    if erfuellt:
        st.error(f"⛔ **MODUS PONENS ERFÜLLT:** `{ziel_term}` ist aus den Prämissen logisch bewiesen.")
    else:
        gruende_formatted = "\n".join(protokoll)
        st.info(f"ℹ️ **MODUS PONENS NICHT ERFÜLLT:** `{ziel_term}` lässt sich nicht ableiten.\n\n**Ursachen:**\n{gruende_formatted}")
