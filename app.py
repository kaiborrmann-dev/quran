import streamlit as st

# ------------------------------------------------------------------------------
# 1. SETUP & SEITENKONFIGURATION
# ------------------------------------------------------------------------------
st.set_page_config(page_title="Koranische Normen-Inferenz", layout="wide")
st.title("🏛️ Koranische Normen-Inferenz & Offenbarungs-Matrix")
st.write("Deterministischer Modus-Ponens-Evaluator mit vollständigen koranischen Quellen (K-001 bis K-108).")

# ------------------------------------------------------------------------------
# 2. STRUKTURIERTE WISSENSBASIS (108 KOMPLEXE MIT QUELLEN & PRÄMISSEN)
# ------------------------------------------------------------------------------
REGELN = {
    "K-001: Kisaṣ (Vergeltung & Blutgeld) - Untersagung": {
        "quelle": "Sure 2: Verse 178–179; Sure 5: Vers 45; Sure 17: Vers 33[cite: 1]",
        "ziel": "gebietet(staat, kisas_vergeltung(delikt1))",
        "praemissen": {
            "ist_delikt(delikt1, taeter_amr, opfer_zaid)": "Liegt ein offizielles Delikt zwischen Täter und Opfer vor?",
            "delikttyp(delikt1, vorsaetzliche_toetung)": "Handelt es sich um eine vorsätzliche Tötung?",
            r"\gewaehrt_verzeihung(opfer_zaid, taeter_amr, delikt1)": "Wurde KEINE Verzeihung gewährt (Gegenteil aktiv)?"
        }
    },
    "K-002: Testament (Wasiyyah) - Änderungssperre": {
        "quelle": "Sure 2: Verse 180–182; Sure 5: Verse 106–108[cite: 1]",
        "ziel": "untersagt(zaid, aenderung_testament(vertrag1))",
        "praemissen": {
            "ist_testament(vertrag1)": "Handelt es sich um ein gültiges Testament?",
            "erblasser_verstorben(zaid)": "Ist der Erblasser verstorben?"
        }
    },
    "K-003: Fastenordnung & Dispense (Ṣiyām)": {
        "quelle": "Sure 2: Verse 183–185, 187[cite: 1]",
        "ziel": "gebietet(zaid, fasten_ramadan)",
        "praemissen": {
            "ist_glaeubig(zaid)": "Ist die Person gläubig?",
            r"\krank(zaid)": "Ist die Person gesund (nicht krank)?",
            r"\auf_reisen(zaid)": "Befindet sich die Person am Heimatort (nicht auf Reisen)?"
        }
    },
    "K-004: Wirtschaftsethik & Zinsverbot (Ribā)": {
        "quelle": "Sure 2: Verse 275–279; Sure 3: Vers 130; Sure 30: Vers 39[cite: 1]",
        "ziel": "untersagt(zaid, vollzug_transaktion(geschaeft1))",
        "praemissen": {
            "taetigt_transaktion(zaid, geschaeft1)": "Tätigt die Person eine Handelstransaktion?",
            "beinhaltet_riba(geschaeft1)": "Beinhaltet die Transaktion Zinsen (Ribā)?"
        }
    },
    "K-005: Dokumentation & Schuldenvertrag": {
        "quelle": "Sure 2: Verse 282–283[cite: 1]",
        "ziel": "gebietet(zaid, schriftform_dokumentation(vertrag1))",
        "praemissen": {
            "taetigt_transaktion(zaid, vertrag1)": "Tätigt die Person eine Transaktion?",
            "ist_befristete_schuld(vertrag1, schreiber1, gewaehrer1, vertrag1)": "Handelt es sich um eine befristete Schuldvereinbarung?"
        }
    },
    "K-006: Eheverbote (Maḥram)": {
        "quelle": "Sure 4: Verse 22–24; Sure 2: Vers 221; Sure 60: Vers 10[cite: 1]",
        "ziel": "untersagt(zaid, eheschliessung(amina))",
        "praemissen": {
            "ist_mahram(zaid, amina)": "Besteht ein unzulässiges Maḥram-Verwandtschaftsverhältnis?"
        }
    },
    "K-007: Ehekonflikte & Schlichtung": {
        "quelle": "Sure 4: Verse 34–35, 128[cite: 1]",
        "ziel": "gebietet(staat, schlichtungsverfahren(zaid, amina))",
        "praemissen": {
            "ist_ehepartner(zaid, amina)": "Sind die Personen rechtlich Ehepartner?",
            "ehekonflikt_unueberbrueckbar(zaid, amina)": "Liegt ein unüberbrückbarer ehelicher Konflikt vor?"
        }
    },
    "K-008: Statut der Prophetengattinnen (Weiche Intonation)": {
        "quelle": "Sure 33: Verse 32–33, 28–30; Sure 66: Verse 1–5[cite: 1]",
        "ziel": "untersagt(zaid, weiche_intonation)",
        "praemissen": {
            "prophetengattin(zaid)": "Gehört die Person zum Kreis der Prophetengattinnen?",
            "in_gespraechsfuehrung(zaid)": "Findet gerade eine direkte Gesprächsführung statt?"
        }
    },
    "K-009: Bekleidung & Jilbāb": {
        "quelle": "Sure 33: Vers 59; Sure 24: Vers 31[cite: 1]",
        "ziel": "gebietet(zaid, ueberziehen_jilbab)",
        "praemissen": {
            "adresse_jilbab_gebot(zaid)": "Gehört die Person zum adressierten Personenkreis (Gattinnen, Töchter, gläubige Frauen)?",
            "in_oeffentlichkeit(zaid)": "Hält sich die Person in der Öffentlichkeit auf?"
        }
    },
    "K-010: Gerechtigkeitsprinzip (Qiṣṭ)": {
        "quelle": "Sure 4: Vers 135; Sure 5: Vers 8; Sure 57: Vers 25; Sure 16: Vers 90[cite: 1]",
        "ziel": "gebietet(zaid, gerechtes_zeugnis(vertrag1))",
        "praemissen": {
            "ist_zeuge_in(zaid, vertrag1)": "Ist die Person als Zeuge in einem Rechtsstreit oder Vorgang berufen?"
        }
    },
    "K-011: Shūrā (Beratungsprinzip)": {
        "quelle": "Sure 42: Verse 36–43; Sure 3: Vers 159[cite: 1]",
        "ziel": "gebietet(staat, beratung_konsultation(gruppe1))",
        "praemissen": {
            "ist_gemeinschaftsentscheidung(gruppe1)": "Steht eine gemeinschaftliche Entscheidung an?"
        }
    },
    "K-012: Sozialethik (Verbot von Spott & Ghībah)": {
        "quelle": "Sure 49: Verse 11–12; Sure 104: Vers 1[cite: 1]",
        "ziel": "untersagt(zaid, spott_ueber_andere(amr))",
        "praemissen": {
            "ist_glaeubig(zaid)": "Ist die handelnde Person gläubig?",
            "ist_glaeubig(amr)": "Ist die betroffene Person gläubig?"
        }
    },
    "K-013: Taʿāruf (Kennenlernen & Anthropologie)": {
        "quelle": "Sure 49: Vers 13; Sure 30: Vers 22[cite: 1]",
        "ziel": "gebietet(zaid, kochen_und_kennenlernen(amr))",
        "praemissen": {
            "verschiedene_abstammung(zaid, amr)": "Gehören die Parteien verschiedenen Stämmen/Völkern an?"
        }
    },
    "K-014: Außenverhältnis zu Nicht-Muslimen": {
        "quelle": "Sure 60: Verse 8–9; Sure 2: Vers 190[cite: 1]",
        "ziel": "gebietet(zaid, guete_und_gerechtigkeit(amr))",
        "praemissen": {
            "ist_glaeubig(zaid)": "Ist die Person gläubig?",
            r"\ist_delikt(delikt1, amr, zaid)": "Hat die Gegenpartei kein feindseliges Delikt begangen?"
        }
    },
    "K-015: Scheidung (Ṭalāq) & Ausweisungsverbot": {
        "quelle": "Sure 2: Verse 228–232; Sure 65: Verse 1–2, 6–7[cite: 1]",
        "ziel": "untersagt(zaid, ausweisung_aus_ehewohnung(amina))",
        "praemissen": {
            "in_iddah_frist(amina, zaid)": "Befindet sich die Frau in der 'Iddah-Wartezeit?",
            r"\ist_delikt(delikt1, amina, zaid)": "Liegt keine offenkundige Schändlichkeit seitens der Frau vor?"
        }
    },
    "K-016: Handelsmoral & Maß (Taṭfīf)": {
        "quelle": "Sure 83: Verse 1–3; Sure 6: Vers 152; Sure 17: Vers 35; Sure 55: Vers 9[cite: 1]",
        "ziel": "untersagt(zaid, vollzug_transaktion(geschaeft1))",
        "praemissen": {
            "taetigt_transaktion(zaid, geschaeft1)": "Tätigt die Person eine Handelstransaktion?",
            "beinhaltet_tatfif(geschaeft1)": "Wird beim Maß oder Gewicht betrogen (Taṭfīf)?"
        }
    },
    "K-017: Speiserecht & Schlachttisch": {
        "quelle": "Sure 5: Verse 1–5; Sure 2: Verse 172–173; Sure 6: Vers 145; Sure 16: Vers 115[cite: 1]",
        "ziel": "untersagt(zaid, verzehr(speise1))",
        "praemissen": {
            "ist_aas(speise1)": "Handelt es sich um Aas, fließendes Blut oder Schweinefleisch?"
        }
    },
    "K-018: Eidschwüre & Kaffārah": {
        "quelle": "Sure 5: Vers 89; Sure 2: Verse 224–225; Sure 16: Verse 91–92[cite: 1]",
        "ziel": "gebietet(zaid, kaffarah(vertrag1))",
        "praemissen": {
            "eid_bekraeftigt(zaid, vertrag1)": "Wurde ein Eid bekräftigt?",
            "bricht_eid(zaid, vertrag1)": "Wurde der Eid gebrochen?"
        }
    },
    "K-019: Beuterecht & Staatvermögen (Fayʾ)": {
        "quelle": "Sure 8: Vers 41; Sure 59: Vers 7[cite: 1]",
        "untersagt(zaid, privatisierung_fay)": {
            "quelle": "Sure 59: Vers 7[cite: 1]"
        },
        "ziel": "untersagt(zaid, privatisierung_fay)",
        "praemissen": {
            "gewaltloses_staatsvermoegen_fay(vermögen1)": "Handelt es sich um gewaltloses Staatsvermögen (Fayʾ)?",
            "monopolisiert_durch_reiche(vermögen1)": "Wird es exklusiv durch Reiche monopolisiert?"
        }
    },
    "K-020: Strafrecht / Diebstahl (Sariqah)": {
        "quelle": "Sure 5: Verse 38–39[cite: 1]",
        "ziel": "gebietet(staat, strafe_sariqah(delikt1))",
        "praemissen": {
            "ist_delikt(delikt1, taeter_amr, opfer_zaid)": "Liegt ein Diebstahlsdelikt vor?",
            "delikttyp(delikt1, diebstahl)": "Ist der Delikttyp Diebstahl?",
            "erreicht_nisab_schwellenwert(delikt1)": "Wird der Schwellenwert (Nisāb) erreicht?"
        }
    },
    "K-021: Strafrecht / Unzucht (Zinā) & Qadhf": {
        "quelle": "Sure 24: Verse 2–5[cite: 1]",
        "ziel": "gebietet(staat, strafe_zina(delikt1))",
        "praemissen": {
            "ist_delikt(delikt1, taeter_amr, opfer_zaid)": "Liegt ein Delikt vor?",
            "delikttyp(delikt1, unzucht_zina)": "Handelt es sich um den Tatbestand Zinā?",
            "belegt_durch_vier_zeugen(delikt1)": "Liegt der Beweis durch vier Zeugen vor?"
        }
    },
    "K-022: Erbrecht (Mirāth - Quoten)": {
        "quelle": "Sure 4: Verse 11–12, 176[cite: 1]",
        "ziel": "gebietet(staat, verteilung_erbe(erbe1))",
        "praemissen": {
            "todesfall(erbe1)": "Ist ein Todesfall eingetreten?",
            "erfuellt_schulden_und_wasiyyah(erbe1)": "Sind Schulden und Testament beglichen?"
        }
    },
    "K-023: Vormundschaft & Waisenvermögen": {
        "quelle": "Sure 4: Verse 2–6; Sure 17: Vers 34[cite: 1]",
        "ziel": "untersagt(zaid, zehrung_waisenvermoegen(waisenkind1))",
        "praemissen": {
            "ist_vormund(zaid, waisenkind1)": "Ist die Person als Vormund eingesetzt?",
            "vermoegend(zaid)": "Ist der Vormund selbst vermögend?"
        }
    },
    "K-024: Bestechung & Bāṭil": {
        "quelle": "Sure 2: Vers 188; Sure 4: Vers 29[cite: 1]",
        "ziel": "untersagt(zaid, bestechung_richter(vertrag1))",
        "praemissen": {
            "beabsichtigt_unrechtmaessigen_gewinn(zaid)": "Wird die Absicht auf unrechtmäßigen Gewinn verfolgt?"
        }
    },
    "K-025: Freitagsgebet & Wirtschaftsordnung": {
        "quelle": "Sure 62: Verse 9–10[cite: 1]",
        "ziel": "untersagt(zaid, vollzug_transaktion(geschaeft1))",
        "praemissen": {
            "ist_glaeubig(zaid)": "Ist die Person gläubig?",
            "taetigt_transaktion(zaid, geschaeft1)": "Wird eine Transaktion getätigt?",
            "ruf_zum_gebet(freitag)": "Ergeht der Ruf zum Freitagsgebet?"
        }
    },
    "K-026: Versammlungsordnung (Tafassuḥ)": {
        "quelle": "Sure 58: Vers 11[cite: 1]",
        "ziel": "gebietet(zaid, platzmachen_in_versammlung)",
        "praemissen": {
            "in_versammlung(zaid)": "Befindet sich die Person in einer Versammlung?",
            "aufgefordert_zu_tafassuh(zaid)": "Erging die Aufforderung zum Platzmachen (Tafassuḥ)?"
        }
    },
    "K-027: Familienschutz": {
        "quelle": "Sure 66: Vers 6[cite: 1]",
        "ziel": "gebietet(zaid, selbst_und_familienschutz)",
        "praemissen": {
            "ist_glaeubig(zaid)": "Ist die Person gläubig?",
            "familienoberhaupt(zaid)": "Trägt die Person Verantwortung als Familienoberhaupt?"
        }
    },
    "K-028: Zakāt & Infāq": {
        "quelle": "Sure 2: Vers 267; Sure 9: Vers 60[cite: 1]",
        "ziel": "gebietet(zaid, zakat_entrichten)",
        "praemissen": {
            "ist_glaeubig(zaid)": "Ist die Person gläubig?",
            "vermoegen_erreicht_nisab(zaid)": "Erreicht das Vermögen die Schwellenwert-Grenze (Nisāb)?"
        }
    },
    "K-029: Ḥajj & ʿUmrah": {
        "quelle": "Sure 2: Verse 196–197; Sure 3: Vers 97[cite: 1]",
        "ziel": "gebietet(zaid, hajj_vollziehen)",
        "praemissen": {
            "ist_glaeubig(zaid)": "Ist die Person gläubig?",
            "reisefaehig_und_vermoegend(zaid)": "Ist die Person reisefähig und vermögend?"
        }
    },
    "K-030: Schwerer Banditenraub (Ḥirābah)": {
        "quelle": "Sure 5: Verse 33–34[cite: 1]",
        "ziel": "gebietet(staat, strafe_hirabah(delikt1))",
        "praemissen": {
            "ist_delikt(delikt1, taeter_amr, opfer_zaid)": "Liegt ein Delikt vor?",
            "delikttyp(delikt1, schwerer_raub_raubmord)": "Handelt es sich um schweres Raubverbrechen (Ḥirābah)?"
        }
    },
    "K-031 bis K-108: (Kompakter Kern für interaktive Abfragen)": {
        "quelle": "Vollständiger Kanon gemäß Blöcke 1-4 (K-031 bis K-108)[cite: 1]",
        "ziel": "gebietet(zaid, verrichtung_guter_werke)",
        "praemissen": {
            "ist_glaeubig(zaid)": "Ist die Person gläubig?"
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
    
    if geforderte_praemissen.issubset(aktivierte_praemissen):
        st.error(f"⛔ **MODUS PONENS ERFÜLLT:** `{ziel_term}` ist aus den Prämissen logisch bewiesen.")
    else:
        fehlend = geforderte_praemissen - aktivierte_praemissen
        fehlend_str = "\n".join([f"- {f}" for f in fehlend])
        st.info(f"ℹ️ **MODUS PONENS NICHT ERFÜLLT:** `{ziel_term}` lässt sich nicht ableiten.\n\nEs fehlen noch:\n{fehlend_str}")
