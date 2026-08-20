import os
import re
import streamlit as st

# ------------------------------------------------------------------------------
# 1. SETUP
# ------------------------------------------------------------------------------
st.set_page_config(page_title="Koranische Normen-Inferenz", layout="wide")
st.title("🏛️ Koranische Normen-Inferenz")
st.write("Automatischer Parser: Liest die Regeln direkt aus der `.pl`-Datei und generiert native Modus-Ponens-Abfragen.")

pl_file = "Koran_ethische_PROLOG_Regeln_bereinigt.pl"

if not os.path.exists(pl_file):
    st.error(f"Die Datei '{pl_file}' wurde nicht gefunden!")
    st.stop()

# ------------------------------------------------------------------------------
# 2. PROLOG PARSER (Liest die .pl-Datei)
# ------------------------------------------------------------------------------
def konretisiere_variablen(text):
    """Ersetzt abstrakte Prolog-Variablen durch anschauliche Bezeichner für die UI."""
    replacements = {
        r'\bX\b': 'zaid',
        r'\bY\b': 'amr',
        r'\bT\b': 'geschaeft1',
        r'\bF\b': 'amina',
        r'\bM\b': 'zaid',
        r'\bH\b': 'zaid',
        r'\bG\b': 'staat',
        r'\bV\b': 'vertrag1',
        r'\bD\b': 'delikt1',
        r'\bW\b': 'waisenkind1',
        r'\bE\b': 'erbe1',
        r'\bK\b': 'kind1',
        r'\bU\b': 'unfreier1',
        r'\bS\b': 'speise1',
        r'\bP1\b': 'partei_a',
        r'\bP2\b': 'partei_b',
        r'\bN\b': 'nachricht1',
        r'\bTaelter\b': 'taeter_amr',
        r'\bOpfer\b': 'opfer_zaid',
        r'\bVormund\b': 'vormund_zaid',
        r'\bErblasser\b': 'erblasser_amr',
        r'\bPerson\b': 'person1'
    }
    for pattern, repl in replacements.items():
        text = re.sub(pattern, repl, text)
    return text

@st.cache_data
def lade_regel_katalog(filepath):
    rules_dict = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Zerteilt die Datei genau vor jedem neuen Normenkomplex (Titel)
    blocks = re.split(r'(?=% K-\d{3}:)', content)
    
    for block in blocks:
        # 1. Titel extrahieren
        title_match = re.search(r'% (K-\d{3}:\s*.*?)\n', block)
        if not title_match: 
            continue
        thema = title_match.group(1).strip()
        
        # 2. Regeln extrahieren (Erfasst alles bis zum ersten Punkt)
        rule_matches = re.finditer(
            r'^(gebietet|untersagt|gestattet)\((.*)\)\s*:-\s*([\s\S]*?)\.', 
            block, 
            re.MULTILINE
        )
        
        for i, rm in enumerate(rule_matches):
            kopf_typ = rm.group(1)
            kopf_args = konretisiere_variablen(rm.group(2))
            rumpf_raw = rm.group(3)
            
            ziel = f"{kopf_typ}({kopf_args})"
            
            # Rumpf bereinigen (Zeilenumbrüche entfernen) und Variablen übersetzen
            rumpf_clean = re.sub(r'\s+', ' ', rumpf_raw).strip()
            rumpf_clean = konretisiere_variablen(rumpf_clean)
            
            # Prämissen trennen (splittet bei Komma, sofern es nicht innerhalb von Klammern steht)
            praemissen_raw = re.split(r',\s*(?![^()]*\))', rumpf_clean)
            
            praemissen = {}
            for p in praemissen_raw:
                p = p.strip()
                if not p: continue
                
                # UI-Texte je nach Prolog-Syntax anpassen
                if p.startswith(r'\+'):
                    p_clean = p.replace(r'\+', '').strip()
                    label = f"Gilt NICHT: `{p_clean}`?"
                elif ';' in p:
                    label = f"Trifft MINDESTENS EINES zu: `{p}`?"
                else:
                    label = f"Gilt: `{p}`?"
                    
                praemissen[p] = label
            
            # Regel-Namen für das Dropdown-Menü generieren
            regel_name = f"{thema} ({kopf_typ.capitalize()})"
            if regel_name in rules_dict:
                regel_name = f"{regel_name} #{i+1}"
                
            rules_dict[regel_name] = {
                "ziel": ziel,
                "praemissen": praemissen
            }
            
    return rules_dict

# Katalog laden
REGELN = lade_regel_katalog(pl_file)

if not REGELN:
    st.warning("Keine gültigen Regeln in der Datei gefunden.")
    st.stop()

# ------------------------------------------------------------------------------
# 3. BENUTZEROBERFLÄCHE
# ------------------------------------------------------------------------------
ausgewaehlte_regel = st.selectbox("Normenkomplex aus der .pl-Datei wählen:", list(REGELN.keys()))
regel_data = REGELN[ausgewaehlte_regel]

st.markdown("---")
st.subheader("1. Zu prüfender Regelkopf (Konklusion B)")
st.code(regel_data["ziel"], language="prolog")

st.subheader("2. Prämissenbelegung für den Modus Ponens (A)")

aktivierte_praemissen = set()

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
    
    # Mengenlehre: Sind alle zwingenden Vorgaben angekreuzt?
    if geforderte_praemissen.issubset(aktivierte_praemissen):
        st.error(f"⛔ **MODUS PONENS ERFÜLLT:** `{ziel_term}` ist aus den Prämissen logisch bewiesen.")
    else:
        fehlend = geforderte_praemissen - aktivierte_praemissen
        fehlend_str = "\n".join([f"- {f}" for f in fehlend])
        st.info(f"ℹ️ **MODUS PONENS NICHT ERFÜLLT:** `{ziel_term}` lässt sich nicht ableiten.\n\nEs fehlen noch:\n{fehlend_str}")
