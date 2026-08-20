import streamlit as st

# ------------------------------------------------------------------------------
# 1. SETUP & SEITENKONFIGURATION
# ------------------------------------------------------------------------------
st.set_page_config(page_title="Koranische Normen-Inferenz", layout="wide")
st.title("🏛️ Koranische Normen-Inferenz & Offenbarungs-Matrix")
st.write("Deterministischer Modus-Ponens-Evaluator mit echter Negation-as-Failure (NAF)-Semantik.")

# ------------------------------------------------------------------------------
# 2. STRUKTURIERTE WISSENSBASIS (MIT KORANISCHEN QUELLEN & EXPLICITEN AUSNAHMEN)
# ------------------------------------------------------------------------------
REGELN = {
    "K-001: Kisaṣ (Vergeltung & Blutgeld) - Untersagung": {
        "quelle": "Sure 2: Verse 178–179; Sure 5: Vers 45; Sure 17: Vers 33[cite: 1]",
        "ziel": "gebietet(staat, kisas_vergeltung(delikt1))",
        "praemissen": {
            "ist_delikt(delikt1, taeter_amr, opfer_zaid)": ("positive", "Liegt ein offizielles Delikt zwischen Täter und Opfer vor?"),
            "delikttyp(delikt1, vorsaetzliche_toetung)": ("positive", "Handelt es sich um eine vorsätzliche Tötung?"),
            r"\+gewaehrt_verzeihung(opfer_zaid, taeter_amr, delikt1)": ("einwand", "Wurde vom Opfer eine formelle Verzeihung gewährt?")
        }
    },
    "K-002: Testament (Wasiyyah) - Änderungssperre": {
        "quelle": "Sure 2: Verse 180–182; Sure 5: Verse 106–108[cite: 1]",
        "ziel": "untersagt(zaid, aenderung_testament(vertrag1))",
        "praemissen": {
            "ist_testament(vertrag1)": ("positive", "Handelt es sich um ein gültiges Testament?"),
            "erblasser_verstorben(zaid)": ("positive", "Ist der Erblasser verstorben?")
        }
    },
    "K-003: Fastenordnung & Dispense (Ṣiyām)": {
        "quelle": "Sure 2: Verse 183–185, 187[cite: 1]",
        "ziel": "gebietet(zaid, fasten_ramadan)",
        "praemissen": {
            "ist_glaeubig(zaid)": ("positive", "Ist die Person gläubig?"),
            r"\+krank(zaid)": ("einwand", "Ist die Person akut erkrankt?"),
            r"\+auf_reisen(zaid)": ("einwand", "Befindet sich die Person auf Reisen?")
        }
    },
    "K-004: Wirtschaftsethik & Zinsverbot (Ribā)": {
        "quelle": "Sure 2: Verse 275–279; Sure 3: Vers 130; Sure 30: Vers 39[cite: 1]",
        "ziel": "untersagt(zaid, vollzug_transaktion(geschaeft1))",
        "praemissen": {
            "taetigt_transaktion(zaid, geschaeft1)": ("positive", "Tätigt die Person eine Handelstransaktion?"),
            "beinhaltet_riba(geschaeft1)": ("positive", "Beinhaltet die Transaktion Zinsen (Ribā)?")
        }
    },
    "K-005: Dokumentation & Schuldenvertrag": {
        "quelle": "Sure 2: Verse 282–283[cite: 1]",
        "ziel": "gebietet(zaid, schriftform_dokumentation(vertrag1))",
        "praemissen": {
            "taetigt_transaktion(zaid, vertrag1)": ("positive", "Tätigt die Person eine Transaktion?"),
            "ist_befristete_schuld(vertrag1, schreiber1, gewaehrer1, vertrag1)": ("positive", "Handelt es sich um eine befristete Schuldvereinbarung?")
        }
    },
    "K-006: Eheverbote (Maḥram)": {
        "quelle": "Sure 4: Verse 22–24; Sure 2: Vers 221; Sure 60: Vers 10[cite: 1]",
        "ziel": "untersagt(zaid, eheschliessung(amina))",
        "praemissen": {
            "ist_mahram(zaid, amina)": ("positive", "Besteht ein unzulässiges Maḥram-Verwandtschaftsverhältnis?")
        }
    },
    "K-007: Ehekonflikte & Schlichtung": {
        "quelle": "Sure 4: Verse 34–35, 128[cite: 1]",
        "ziel": "gebietet(staat, schlichtungsverfahren(zaid, amina))",
        "praemissen": {
            "ist_ehepartner(zaid, amina)": ("positive", "Sind die Personen rechtlich Ehepartner?"),
            "ehekonflikt_unueberbrueckbar(zaid, amina)": ("positive", "Liegt ein unüberbrückbarer ehelicher Konflikt vor?")
        }
    },
    "K-008: Statut der Prophetengattinnen (Weiche Intonation)": {
        "quelle": "Sure 33: Verse 32–33, 28–30; Sure 66: Verse 1–5[cite: 1]",
        "ziel": "untersagt(zaid, weiche_intonation)",
        "praemissen": {
            "prophetengattin(zaid)": ("positive", "Gehört die Person zum Kreis der Prophetengattinnen?"),
            "in_gespraechsfuehrung(zaid)": ("positive", "Findet gerade eine direkte Gesprächsführung statt?")
        }
    },
    "K-009: Bekleidung & Jilbāb": {
        "quelle": "Sure 33: Vers 59; Sure 24: Vers 31[cite: 1]",
        "ziel": "gebietet(zaid, ueberziehen_jilbab)",
        "praemissen": {
            "adresse_jilbab_gebot(zaid)": ("positive", "Gehört die Person zum adressierten Personenkreis?"),
            "in_oeffentlichkeit(zaid)": ("positive", "Hält sich die Person in der Öffentlichkeit auf?")
        }
    },
    "K-014: Außenverhältnis zu Nicht-Muslimen": {
        "quelle": "Sure 60: Verse 8–9; Sure 2: Vers 190[cite: 1]",
        "ziel": "gebietet(zaid, guete_und_gerechtigkeit(amr))",
        "praemissen": {
            "ist_glaeubig(zaid)": ("positive", "Ist die Person gläubig?"),
            r"\+ist_delikt(delikt1, amr, zaid)": ("einwand", "Hat die Gegenpartei ein feindseliges Delikt gegen die Muslime begangen?")
        }
    },
    "K-015: Scheidung (Ṭalāq) & Ausweisungsverbot": {
        "quelle": "Sure 2: Verse 228–232; Sure 65: Verse 1–2, 6–7[cite: 1]",
        "ziel": "untersagt(zaid, ausweisung_aus_ehewohnung(amina))",
        "praemissen": {
            "in_iddah_frist(amina, zaid)": ("positive", "Befindet sich die Frau in der 'Iddah-Wartezeit?"),
            r"\+ist_delikt(delikt1, amina, zaid)": ("einwand", "Liegt eine offenkundige Schändlichkeit (Fahishah) seitens der Frau vor?")
        }
    }
}

# ------------------------------------------------------------------------------
# 3. BENUTZEROBERFLÄCHE
# ------------------------------------------------------------------------------
ausgewaehlte_regel = st.selectbox("Normenkomplex auswählen:", list(REGELN.keys()))
regel_data = REGELN[ausgewaehlte_regel]

# Koranische Quelle direkt anzeigen
st.info(f"📖 **Koranische Offenbarungsquelle:** {regel_data['quelle']}")

st.markdown("---")
st.subheader("1. Zu prüfender Regelkopf (Konklusion B)")
st.code(regel_data["ziel"], language="prolog")

st.subheader("2. Sachverhalts-Erfassung (Fakten & Einwände)")

aktive_fakten = set()

# Differenzierte Abfrage nach Art der Prämisse (Positive Tatbestände vs. Einwände)
for fakt_code, (typ, label) in regel_data["praemissen"].items():
    if typ == "positive":
        if st.checkbox(f"✅ {label}  👉  `{fakt_code}`", value=True):
            aktive_fakten.add(fakt_code)
    elif typ == "einwand":
        clean_code = fakt_code.replace(r"\+", "")
        # Ein Einwand ist standardmäßig NICHT aktiv (Sperre greift nicht). 
        # Wenn der Nutzer das Häkchen setzt, tritt der Sperrtatbestand in Kraft!
        if st.checkbox(f"⚠️ [Einwand/Sperre] {label}  👉  `{clean_code}`", value=False):
            aktive_fakten.add(clean_code)

st.markdown("---")
st.subheader("3. Aktive Faktenmenge in der Datenbank")
if aktive_fakten:
    st.code("\n".join([f"{f}." for f in aktive_fakten]), language="prolog")
else:
    st.code("% Keine Fakten aktiv", language="prolog")

# ------------------------------------------------------------------------------
# 4. NATIVE PROLOG-INFERENZ (MODUS PONENS MIT NAF)
# ------------------------------------------------------------------------------
if st.button("⚖️ Modus Ponens berechnen", type="primary"):
    ziel_term = regel_data["ziel"]
    
    st.subheader("4. Ergebnis der logischen Auswertung (Closed-World-Assumption)")
    
    erfuellt = True
    blockierende_gruende = []
    
    for fakt_code, (typ, label) in regel_data["praemissen"].items():
        if typ == "positive":
            # Positive Prämisse muss zwingend in den aktiven Fakten sein
            if fakt_code not in aktive_fakten:
                erfuellt = False
                blockierende_gruende.append(f"Fehlende positive Bedingung: `{fakt_code}`")
        elif typ == "einwand":
            clean_code = fakt_code.replace(r"\+", "")
            # Negation as Failure (NAF): Wenn der Sperrfakt aktiv ist, blockiert er die Regel!
            if clean_code in aktive_fakten:
                erfuellt = False
                blockierende_gruende.append(f"Sperrtatbestand aktiv (blockiert Regel): `{clean_code}`")

    if erfuellt:
        st.error(f"⛔ **MODUS PONENS ERFÜLLT:** `{ziel_term}` ist aus den Prämissen logisch bewiesen.")
    else:
        gruende_str = "\n".join([f"- {g}" for g in blockierende_gruende])
        st.info(f"ℹ️ **MODUS PONENS NICHT ERFÜLLT:** `{ziel_term}` lässt sich nicht ableiten.\n\nGrunde:\n{gruende_str}")
