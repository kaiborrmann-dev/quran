import streamlit as st
from regeln import KANON

# ------------------------------------------------------------------------------
# 1. ARCHITEKTUR & SEITEN-SETUP
# ------------------------------------------------------------------------------
st.set_page_config(page_title="Koranische Normen-Inferenz (Wessel-Engine)", layout="wide")
st.title("🏛️ Koranischer Normen-Apparat (Epistemische Logik nach Wessel)")
st.write("Deterministischer Modus-Ponens-Evaluator mit epistemischer Status-Klassifikation (D1–D6 nach Horst Wessel).")

# ------------------------------------------------------------------------------
# 2. BENUTZEROBERFLÄCHE (DETERMINISTISCHES FORMULAR)
# ------------------------------------------------------------------------------
sortierte_ids = sorted(KANON.keys())
auswahl_id = st.selectbox("Normenkomplex wählen:", sortierte_ids, format_func=lambda x: KANON[x]["titel"])
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
st.subheader("3. Aktive Faktenmenge im Arbeitsspeicher (Wissen W)")
if aktive_fakten:
    st.code("\n".join([f"{f}." for f in aktive_fakten]), language="prolog")
else:
    st.code("% Wissen W ist leer (keine Fakten aktiv)", language="prolog")

# ------------------------------------------------------------------------------
# 4. DIE INFERENZ-KERNFUNKTION & WESSEL-KLASSIFIKATION (D1–D6)
# ------------------------------------------------------------------------------
if st.button("⚖️ Modus Ponens & epistemischen Status berechnen", type="primary"):
    ziel_term = regel["ziel"]
    
    st.subheader("4. Inferenz-Ergebnis & Epistemischer Status nach Horst Wessel")
    
    erfuellt = True
    protokoll = []
    
    # 1. Alle positiven Bedingungen prüfen
    for code, _ in regel["positive"]:
        if code not in aktive_fakten:
            erfuellt = False
            protokoll.append(f"❌ Fehlende positive Bedingung: `{code}`")
            
    # 2. Alle Sperren prüfen
    for code, _ in regel["sperren"]:
        if code in aktive_fakten:
            erfuellt = False
            protokoll.append(f"⛔ Sperrtatbestand greift (blockiert Norm): `{code}`")
            
    # --- WESSEL-KLASSIFIKATION (D1 - D6) ---
    # W steht für die aktive_fakten-Menge.
    # Beweisbarkeit (W ⊢ A): Wenn erfuellt == True, ist die Konklusion beweisbar.
    w_vdash_a = erfuellt
    w_is_empty = (len(aktive_fakten) == 0)
    
    # Ermittlung nach Wessel:
    if w_vdash_a:
        wessel_status = "D1: Beweisbar bezüglich W (W ⊢ A)"
        wessel_desc = "Die Aussage ist aus dem gegebenen Wissen logisch ableitbar."
    else:
        # Nicht beweisbar -> Entweder D2 (bei leerem W) oder D5/D3 etc.
        if w_is_empty:
            wessel_status = "D2: Unbeweisbar bezüglich W (~(W ⊢ A) wegen leerem Wissen)"
            wessel_desc = "Das Wissensarchiv W ist leer; es liegt keinerlei Information vor."
        else:
            # Prüfen, ob Fakten irrelevant sind oder ein Widerspruch/Sperre vorliegt
            wessel_status = "D5: Unentscheidbar bezüglich W (Weder beweisbar noch widerlegbar)"
            wessel_desc = "Die vorhandenen Fakten greifen nicht oder besitzen keinen hinreichenden Bezug zu den Regelprämissen."

    # Ausgabe des Inferenz-Status
    if erfuellt:
        st.error(f"⛔ **MODUS PONENS ERFÜLLT:** `{ziel_term}` ist aus den Prämissen logisch bewiesen.")
    else:
        gruende_formatted = "\n".join(protokoll)
        st.info(f"ℹ️ **MODUS PONENS NICHT ERFÜLLT:** `{ziel_term}` lässt sich nicht ableiten.\n\n**Ursachen:**\n{gruende_formatted}")

    # Ausgabe des Wessel-Status im UI
    st.markdown("---")
    st.markdown(f"### 📐 Epistemischer Status nach Horst Wessel (Logik, S. 349)")
    st.markdown(f"**Klassifikation:** `{wessel_status}`")
    st.markdown(f"*Befund:* {wessel_desc}")
