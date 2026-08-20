import streamlit as st

# ------------------------------------------------------------------------------
# 1. SETUP
# ------------------------------------------------------------------------------
st.set_page_config(page_title="Koranische Normen-Inferenz", layout="wide")
st.title("🏛️ Koranische Normen-Inferenz")
st.write("Native Modus-Ponens-Auswertung in reinem Python (ohne fehleranfälliges SWI-Prolog).")

# ------------------------------------------------------------------------------
# 2. REGEL-KATALOG (Deterministische Logik)
# ------------------------------------------------------------------------------
# Hier definieren wir die Regeln als reine Datenstruktur. 
# Keine C-Bindings, keine Parser-Probleme.
REGELN = {
    "K-004: Zinsverbot (Ribā)": {
        "ziel": "untersagt(zaid, vollzug_transaktion(geschaeft1))",
        "praemissen": {
            "taetigt_transaktion(zaid, geschaeft1)": "Tätigt Zaid das Geschäft 'geschaeft1'?",
            "beinhaltet_riba(geschaeft1)": "Enthält 'geschaeft1' Zinsen (Ribā)?"
        }
    },
    "K-003: Fastenpflicht (Ramadan)": {
        "ziel": "gebietet(zaid, fasten_ramadan)",
        "praemissen": {
            "ist_glaeubig(zaid)": "Ist Zaid gläubig?",
            "nicht_krank(zaid)": "Ist Zaid gesund (nicht krank)?",
            "nicht_auf_reisen(zaid)": "Befindet sich Zaid am Heimatort (nicht auf Reisen)?"
        }
    },
    "K-015: Ausweisungsverbot in der Wartezeit ('Iddah)": {
        "ziel": "untersagt(zaid, ausweisung_aus_ehewohnung(amina))",
        "praemissen": {
            "in_iddah_frist(amina, zaid)": "Befindet sich Amina in der 'Iddah-Frist von Zaid?"
        }
    },
    "K-006: Eheverbot (Maḥram)": {
        "ziel": "untersagt(zaid, eheschliessung(fathima))",
        "praemissen": {
            "ist_mahram(zaid, fathima)": "Ist Fathima ein Maḥram-Verwandtenstatus für Zaid?"
        }
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

# Die Liste speichert alle vom Nutzer aktivierten Prämissen
aktivierte_praemissen = set()

# Dynamisch die Checkboxen für die geforderten Prämissen generieren
for fakt_code, label in regel_data["praemissen"].items():
    if st.checkbox(f"{label}  👉  `{fakt_code}`", value=True):
        aktivierte_praemissen.add(fakt_code)

st.markdown("---")
st.subheader("3. Aktivierte Faktenmenge A")
if aktivierte_praemissen:
    st.code("\n".join([f"{f}." for f in aktivierte_praemissen]), language="prolog")
else:
    st.code("% Keine Fakten aktiviert", language="prolog")

# ------------------------------------------------------------------------------
# 4. NATIVE INFERENZ-LOGIK (MODUS PONENS)
# ------------------------------------------------------------------------------
if st.button("⚖️ Modus Ponens berechnen", type="primary"):
    ziel_term = regel_data["ziel"]
    geforderte_praemissen = set(regel_data["praemissen"].keys())
    
    st.subheader("4. Ergebnis der logischen Auswertung")
    
    # Der Modus Ponens ist mathematisch erfüllt, wenn alle geforderten 
    # Prämissen der Regel eine Teilmenge der aktivierten Prämissen sind.
    if geforderte_praemissen.issubset(aktivierte_praemissen):
        st.error(f"⛔ **MODUS PONENS ERFÜLLT:** `{ziel_term}` ist aus den Prämissen logisch bewiesen.")
    else:
        # Finde heraus, welche Prämissen noch fehlen, um dem Nutzer didaktisches Feedback zu geben
        fehlend = geforderte_praemissen - aktivierte_praemissen
        fehlend_str = "\n".join([f"- {f}" for f in fehlend])
        
        st.info(f"ℹ️ **MODUS PONENS NICHT ERFÜLLT:** `{ziel_term}` lässt sich nicht ableiten.\n\nEs fehlen noch folgende Bedingungen:\n{fehlend_str}")
