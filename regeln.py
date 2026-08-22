# ==============================================================================
# VOLLSTÄNDIGER KORANISCHER NORMEN-KANON (K-001 bis K-108)
# ==============================================================================

KANON = {
    "K-001": {
        "titel": "K-001: Kisaṣ (Vergeltung & Blutgeld)",
        "quelle": "Sure 2: Verse 178–179; Sure 5: Vers 45; Sure 17: Vers 33",
        "ziel": "gebietet(staat, kisas_vergeltung(delikt1))",
        "positive": [
            ("ist_delikt(delikt1, taeter_amr, opfer_zaid)", "Liegt ein offizielles Delikt zwischen Täter und Opfer vor?"),
            ("delikttyp(delikt1, vorsaetzliche_toetung)", "Handelt es sich um eine vorsätzliche Tötung?")
        ],
        "sperren": [
            ("gewaehrt_verzeihung(opfer_zaid, taeter_amr, delikt1)", "Wurde vom Opfer eine formelle Verzeihung gewährt?")
        ]
    },
    "K-002": {
        "titel": "K-002: Testament (Wasiyyah) - Änderungssperre",
        "quelle": "Sure 2: Verse 180–182; Sure 5: Verse 106–108",
        "ziel": "untersagt(zaid, aenderung_testament(vertrag1))",
        "positive": [
            ("ist_testament(vertrag1)", "Handelt es sich um ein gültiges Testament?"),
            ("erblasser_verstorben(zaid)", "Ist der Erblasser verstorben?")
        ],
        "sperren": []
    },
    "K-003": {
        "titel": "K-003: Fastenordnung & Dispense (Ṣiyām)",
        "quelle": "Sure 2: Verse 183–185, 187",
        "ziel": "gebietet(zaid, fasten_ramadan)",
        "positive": [
            ("ist_glaeubig(zaid)", "Ist die Person gläubig?")
        ],
        "sperren": [
            ("krank(zaid)", "Ist die Person akut erkrankt?"),
            ("auf_reisen(zaid)", "Befindet sich die Person auf Reisen?")
        ]
    },
    "K-004": {
        "titel": "K-004: Wirtschaftsethik & Zinsverbot (Ribā)",
        "quelle": "Sure 2: Verse 275–279; Sure 3: Vers 130; Sure 30: Vers 39",
        "ziel": "untersagt(zaid, vollzug_transaktion(geschaeft1))",
        "positive": [
            ("taetigt_transaktion(zaid, geschaeft1)", "Tätigt die Person eine Handelstransaktion?"),
            ("beinhaltet_riba(geschaeft1)", "Beinhaltet die Transaktion Zinsen (Ribā)?")
        ],
        "sperren": []
    },
    "K-005": {
        "titel": "K-005: Dokumentation & Schuldenvertrag",
        "quelle": "Sure 2: Verse 282–283",
        "ziel": "gebietet(zaid, schriftform_dokumentation(vertrag1))",
        "positive": [
            ("taetigt_transaktion(zaid, vertrag1)", "Tätigt die Person eine Transaktion?"),
            ("ist_befristete_schuld(vertrag1, schreiber1, gewaehrer1, vertrag1)", "Handelt es sich um eine befristete Schuldvereinbarung?")
        ],
        "sperren": []
    },
    "K-006": {
        "titel": "K-006: Eheverbote (Maḥram)",
        "quelle": "Sure 4: Verse 22–24; Sure 2: Vers 221; Sure 60: Vers 10",
        "ziel": "untersagt(zaid, eheschliessung(amina))",
        "positive": [
            ("ist_mahram(zaid, amina)", "Besteht ein unzulässiges Maḥram-Verwandtschaftsverhältnis?")
        ],
        "sperren": []
    },
    "K-007": {
        "titel": "K-007: Ehekonflikte & Schlichtung",
        "quelle": "Sure 4: Verse 34–35, 128",
        "ziel": "gebietet(staat, schlichtungsverfahren(zaid, amina))",
        "positive": [
            ("ist_ehepartner(zaid, amina)", "Sind die Personen rechtlich Ehepartner?"),
            ("ehekonflikt_unueberbrueckbar(zaid, amina)", "Liegt ein unüberbrückbarer ehelicher Konflikt vor?")
        ],
        "sperren": []
    },
    "K-008": {
        "titel": "K-008: Statut der Prophetengattinnen (Weiche Intonation)",
        "quelle": "Sure 33: Verse 32–33, 28–30; Sure 66: Verse 1–5",
        "ziel": "untersagt(zaid, weiche_intonation)",
        "positive": [
            ("prophetengattin(zaid)", "Gehört die Person zum Kreis der Prophetengattinnen?"),
            ("in_gespraechsfuehrung(zaid)", "Findet gerade eine direkte Gesprächsführung statt?")
        ],
        "sperren": []
    },
    "K-009": {
        "titel": "K-009: Bekleidung & Jilbāb",
        "quelle": "Sure 33: Vers 59; Sure 24: Vers 31",
        "ziel": "gebietet(zaid, ueberziehen_jilbab)",
        "positive": [
            ("adresse_jilbab_gebot(zaid)", "Gehört die Person zum adressierten Personenkreis?"),
            ("in_oeffentlichkeit(zaid)", "Hält sich die Person in der Öffentlichkeit auf?")
        ],
        "sperren": []
    },
    "K-010": {
        "titel": "K-010: Gerechtigkeitsprinzip (Qiṣṭ)",
        "quelle": "Sure 4: Vers 135; Sure 5: Vers 8; Sure 57: Vers 25",
        "ziel": "gebietet(zaid, gerechtes_zeugnis(vertrag1))",
        "positive": [
            ("ist_zeuge_in(zaid, vertrag1)", "Ist die Person als Zeuge in einem Rechtsstreit berufen?")
        ],
        "sperren": []
    },
    "K-011": {
        "titel": "K-011: Shūrā (Beratungsprinzip)",
        "quelle": "Sure 42: Verse 36–43; Sure 3: Vers 159",
        "ziel": "gebietet(staat, beratung_konsultation(gruppe1))",
        "positive": [
            ("ist_gemeinschaftsentscheidung(gruppe1)", "Steht eine gemeinschaftliche Entscheidung an?")
        ],
        "sperren": []
    },
    "K-012": {
        "titel": "K-012: Sozialethik (Verbot von Spott & Ghībah)",
        "quelle": "Sure 49: Verse 11–12; Sure 104: Vers 1",
        "ziel": "untersagt(zaid, spott_ueber_andere(amr))",
        "positive": [
            ("ist_glaeubig(zaid)", "Ist die handelnde Person gläubig?"),
            ("ist_glaeubig(amr)", "Ist die betroffene Person gläubig?")
        ],
        "sperren": []
    },
    "K-013": {
        "titel": "K-013: Taʿāruf (Gegenseitiges Kennenlernen & Anthropologie)",
        "quelle": "Sure 49: Vers 13; Sure 30: Vers 22",
        "ziel": "gebietet(zaid, gegenseitiges_kennenlernen(amr))",
        "positive": [
            ("verschiedene_abstammung(zaid, amr)", "Gehören die Parteien verschiedenen Stämmen oder Völkern an?")
        ],
        "sperren": []
    },
    "K-014": {
        "titel": "K-014: Außenverhältnis zu Nicht-Muslimen",
        "quelle": "Sure 60: Verse 8–9; Sure 2: Vers 190",
        "ziel": "gebietet(zaid, guete_und_gerechtigkeit(amr))",
        "positive": [
            ("ist_glaeubig(zaid)", "Ist die Person gläubig?")
        ],
        "sperren": [
            ("ist_delikt(delikt1, amr, zaid)", "Hat die Gegenpartei ein feindseliges Delikt begangen?")
        ]
    },
    "K-015": {
        "titel": "K-015: Scheidung (Ṭalāq) & Ausweisungsverbot",
        "quelle": "Sure 2: Verse 228–232; Sure 65: Verse 1–2, 6–7",
        "ziel": "untersagt(zaid, ausweisung_aus_ehewohnung(amina))",
        "positive": [
            ("in_iddah_frist(amina, zaid)", "Befindet sich die Frau in der 'Iddah-Wartezeit?")
        ],
        "sperren": [
            ("ist_delikt(delikt1, amina, zaid)", "Liegt eine offenkundige Schändlichkeit seitens der Frau vor?")
        ]
    },
    "K-016": {
        "titel": "K-016: Handelsmoral & Maß (Taṭfīf)",
        "quelle": "Sure 83: Verse 1–3; Sure 6: Vers 152",
        "ziel": "untersagt(zaid, vollzug_transaktion(geschaeft1))",
        "positive": [
            ("taetigt_transaktion(zaid, geschaeft1)", "Tätigt die Person eine Handelstransaktion?"),
            ("beinhaltet_tatfif(geschaeft1)", "Wird beim Maß oder Gewicht betrogen (Taṭfīf)?")
        ],
        "sperren": []
    },
    "K-017": {
        "titel": "K-017: Speiserecht & Schlachttisch",
        "quelle": "Sure 5: Verse 1–5; Sure 2: Verse 172–173",
        "ziel": "untersagt(zaid, verzehr(speise1))",
        "positive": [
            ("ist_aas(speise1)", "Handelt es sich um Aas, fließendes Blut oder Schweinefleisch?")
        ],
        "sperren": []
    },
    "K-018": {
        "titel": "K-018: Eidschwüre & Kaffārah",
        "quelle": "Sure 5: Vers 89; Sure 2: Verse 224–225",
        "ziel": "gebietet(zaid, kaffarah(vertrag1))",
        "positive": [
            ("eid_bekraeftigt(zaid, vertrag1)", "Wurde ein Eid bekräftigt?"),
            ("bricht_eid(zaid, vertrag1)", "Wurde der Eid gebrochen?")
        ],
        "sperren": []
    },
    "K-019": {
        "titel": "K-019: Beuterecht & Staatvermögen (Fayʾ)",
        "quelle": "Sure 8: Vers 41; Sure 59: Vers 7",
        "ziel": "untersagt(zaid, privatisierung_fay)",
        "positive": [
            ("gewaltloses_staatsvermoegen_fay(vermögen1)", "Handelt es sich um gewaltloses Staatsvermögen (Fayʾ)?"),
            ("monopolisiert_durch_reiche(vermögen1)", "Wird es exklusiv durch Reiche monopolisiert?")
        ],
        "sperren": []
    },
    "K-020": {
        "titel": "K-020: Strafrecht / Diebstahl (Sariqah)",
        "quelle": "Sure 5: Verse 38–39",
        "ziel": "gebietet(staat, strafe_sariqah(delikt1))",
        "positive": [
            ("ist_delikt(delikt1, taeter_amr, opfer_zaid)", "Liegt ein Diebstahlsdelikt vor?"),
            ("delikttyp(delikt1, diebstahl)", "Ist der Delikttyp Diebstahl?"),
            ("erreicht_nisab_schwellenwert(delikt1)", "Wird der Schwellenwert (Nisāb) erreicht?")
        ],
        "sperren": []
    },
    "K-021": {
        "titel": "K-021: Strafrecht / Unzucht (Zinā) & Qadhf",
        "quelle": "Sure 24: Verse 2–5",
        "ziel": "gebietet(staat, strafe_zina(delikt1))",
        "positive": [
            ("ist_delikt(delikt1, taeter_amr, opfer_zaid)", "Liegt ein Delikt vor?"),
            ("delikttyp(delikt1, unzucht_zina)", "Handelt es sich um den Tatbestand Zinā?"),
            ("belegt_durch_vier_zeugen(delikt1)", "Liegt der Beweis durch vier Zeugen vor?")
        ],
        "sperren": []
    },
    "K-022": {
        "titel": "K-022: Erbrecht (Mirāth - Quoten)",
        "quelle": "Sure 4: Verse 11–12, 176",
        "ziel": "gebietet(staat, verteilung_erbe(erbe1))",
        "positive": [
            ("todesfall(erbe1)", "Ist ein Todesfall eingetreten?"),
            ("erfuellt_schulden_und_wasiyyah(erbe1)", "Sind Schulden und Testament beglichen?")
        ],
        "sperren": []
    },
    "K-023": {
        "titel": "K-023: Vormundschaft & Waisenvermögen",
        "quelle": "Sure 4: Verse 2–6; Sure 17: Vers 34",
        "ziel": "untersagt(zaid, zehrung_waisenvermoegen(waisenkind1))",
        "positive": [
            ("ist_vormund(zaid, waisenkind1)", "Ist die Person als Vormund eingesetzt?"),
            ("vermoegend(zaid)", "Ist der Vormund selbst vermögend?")
        ],
        "sperren": []
    },
    "K-024": {
        "titel": "K-024: Bestechung & Bāṭil",
        "quelle": "Sure 2: Vers 188; Sure 4: Vers 29",
        "ziel": "untersagt(zaid, bestechung_richter(vertrag1))",
        "positive": [
            ("beabsichtigt_unrechtmaessigen_gewinn(zaid)", "Wird die Absicht auf unrechtmäßigen Gewinn verfolgt?")
        ],
        "sperren": []
    },
    "K-025": {
        "titel": "K-025: Freitagsgebet & Wirtschaftsordnung",
        "quelle": "Sure 62: Verse 9–10",
        "ziel": "untersagt(zaid, vollzug_transaktion(geschaeft1))",
        "positive": [
            ("ist_glaeubig(zaid)", "Ist die Person gläubig?"),
            ("taetigt_transaktion(zaid, geschaeft1)", "Wird eine Transaktion getätigt?"),
            ("ruf_zum_gebet(freitag)", "Ergeht der Ruf zum Freitagsgebet?")
        ],
        "sperren": []
    },
    "K-026": {
        "titel": "K-026: Versammlungsordnung (Tafassuḥ)",
        "quelle": "Sure 58: Vers 11",
        "ziel": "gebietet(zaid, platzmachen_in_versammlung)",
        "positive": [
            ("in_versammlung(zaid)", "Befindet sich die Person in einer Versammlung?"),
            ("aufgefordert_zu_tafassuh(zaid)", "Erging die Aufforderung zum Platzmachen?")
        ],
        "sperren": []
    },
    "K-027": {
        "titel": "K-027: Familienschutz & Prävention",
        "quelle": "Sure 66: Vers 6",
        "ziel": "gebietet(zaid, selbst_und_familienschutz)",
        "positive": [
            ("ist_glaeubig(zaid)", "Ist die Person gläubig?"),
            ("familienoberhaupt(zaid)", "Trägt die Person Verantwortung als Familienoberhaupt?")
        ],
        "sperren": []
    },
    "K-028": {
        "titel": "K-028: Zakāt & Infāq (Abgabeordnung)",
        "quelle": "Sure 2: Vers 267; Sure 9: Vers 60",
        "ziel": "gebietet(zaid, zakat_entrichten)",
        "positive": [
            ("ist_glaeubig(zaid)", "Ist die Person gläubig?"),
            ("vermoegen_erreicht_nisab(zaid)", "Erreicht das Vermögen die Schwellenwert-Grenze (Nisāb)?")
        ],
        "sperren": []
    },
    "K-029": {
        "titel": "K-029: Ḥajj & ʿUmrah (Pilgerfahrt)",
        "quelle": "Sure 2: Verse 196–197; Sure 3: Vers 97",
        "ziel": "gebietet(zaid, hajj_vollziehen)",
        "positive": [
            ("ist_glaeubig(zaid)", "Ist die Person gläubig?"),
            ("reisefaehig_und_vermoegend(zaid)", "Ist die Person reisefähig und vermögend?")
        ],
        "sperren": []
    },
    "K-030": {
        "titel": "K-030: Schwerer Banditenraub (Ḥirābah)",
        "quelle": "Sure 5: Verse 33–34",
        "ziel": "gebietet(staat, strafe_hirabah(delikt1))",
        "positive": [
            ("ist_delikt(delikt1, taeter_amr, opfer_zaid)", "Liegt ein Delikt vor?"),
            ("delikttyp(delikt1, schwerer_raub_raubmord)", "Handelt es sich um schweres Raubverbrechen?")
        ],
        "sperren": []
    },
    # Systematische Erweiterung für K-031 bis K-108 (Kern-Normenblöcke im Gesamtsystem)
    "K-031": {
        "titel": "K-031: Vertragstreue (Awfū bi-l-ʿuqūd)",
        "quelle": "Sure 5: Vers 1; Sure 17: Vers 34",
        "ziel": "gebietet(zaid, erfuellung_vertrag(vertrag1))",
        "positive": [
            ("geschlossen_vertrag(zaid, vertrag1)", "Wurde ein gültiger Vertrag geschlossen?")
        ],
        "sperren": [
            ("sittenwidrig_oder_baatil(vertrag1)", "Liegt ein Nichtigkeitsgrund (Bāṭil) vor?")
        ]
    },
    "K-032": {
        "titel": "K-032: Schutz der Minderjährigen & Vermögensübergabe",
        "quelle": "Sure 4: Vers 6",
        "ziel": "gebietet(zaid, uebergabe_vermoegen_nach_rueschde(waisenkind1))",
        "positive": [
            ("ist_muendig_und_reif(waisenkind1)", "Hat das Mündel die geistige Reife (Rüschde) erreicht?")
        ],
        "sperren": []
    },
    "K-033": {
        "titel": "K-033: Verbot missbräuchlicher Ehescheidung zur Schadenszufügung",
        "quelle": "Sure 2: Vers 231",
        "untersagt": "untersagt(zaid, schikanöse_scheidung(amina))",
        "ziel": "untersagt(zaid, schikaenöse_scheidung(amina))",
        "positive": [
            ("beabsichtigt_schaden_oder_zwang(zaid)", "Wird die Scheidung als Druckmittel oder zur Schädigung eingesetzt?")
        ],
        "sperren": []
    },
    "K-034": {
        "titel": "K-034: Stillzeit & Entlohnung der Mütter",
        "quelle": "Sure 2: Vers 233; Sure 65: Vers 6",
        "ziel": "gebietet(zaid, unterhalt_und_lohn_fuer_stillen(amina))",
        "positive": [
            ("ist_mutter_und_stillt(amina, kind1)", "Stillt die Mutter das gemeinsame Kind?"),
            ("ist_vater_oder_verpflichtet(zaid)", "Ist der Vater unterhaltspflichtig?")
        ],
        "sperren": []
    },
    "K-035": {
        "titel": "K-035: Verbot der erzwungenen Heirat von Witwen",
        "quelle": "Sure 4: Vers 19",
        "ziel": "untersagt(zaid, erzwungene_erbschaft_oder_heirat(amina))",
        "positive": [
            ("beansprucht_frau_gegen_wille(zaid, amina)", "Wird die Frau gegen ihren Willen als Erbe oder Ehefrau beansprucht?")
        ],
        "sperren": []
    },
    "K-036": {
        "titel": "K-036: Güterrecht bei Ehescheidung vor Vollzug",
        "quelle": "Sure 2: Vers 236–237",
        "ziel": "gebietet(zaid, abfindung_vor_vollzug(amina))",
        "provenienz": "Sure 2: 236-237",
        "positive": [
            ("scheidung_vor_vollzug_und_mahr_festlegung(zaid, amina)", "Erfolgt die Scheidung vor Ehevollzug ohne feste Mahr?")
        ],
        "sperren": []
    },
    "K-037": {
        "titel": "K-037: Wahrung der Intimsphäre im Haus",
        "quelle": "Sure 24: Vers 58",
        "ziel": "gebietet(zaid, anmeldung_vor_eintritt(kinder_und_sklaven))",
        "positive": [
            ("befindet_sich_in_privatsphaere(zaid)", "Befindet sich die Person im privaten Wohnbereich zu Ruhezeiten?")
        ],
        "sperren": []
    },
    "K-038": {
        "titel": "K-038: Verbot des unbefugten Betretens fremder Häuser",
        "quelle": "Sure 24: Vers 27",
        "ziel": "untersagt(zaid, betreten_fremder_haeuser_ohne_erlaubnis)",
        "positive": [
            ("naehert_sich_fremdem_haus(zaid)", "Nähert sich die Person einem fremden Haus?"),
            (r"\+erhalten_erlaubnis_und_gruss(zaid)", "Wurde um Erlaubnis gebeten und gegrüßt?")
        ],
        "sperren": []
    },
    "K-039": {
        "titel": "K-039: Verbot übler Nachrede und Verleumdung (Qadhf)",
        "quelle": "Sure 24: Vers 4, 11–15",
        "ziel": "untersagt(zaid, verleumdung_keuscher_frauen(amina))",
        "positive": [
            ("unterstellt_unzucht_ohne_vier_zeugen(zaid, amina)", "Wird ehrabschneidende Rede ohne vier Zeugen geführt?")
        ],
        "sperren": []
    },
    "K-040": {
        "titel": "K-040: Das Liʿān-Verfahren bei Ehebruchsverdacht",
        "quelle": "Sure 24: Verse 6–9",
        "ziel": "gebietet(staat, lian_eid_verfahren(zaid, amina))",
        "positive": [
            ("beschuldigt_ehepartner_ohne_zeugen(zaid, amina)", "Beschuldigt der Ehepartner die Frau ohne externe Zeugen?")
        ],
        "sperren": []
    },
    "K-041": {
        "titel": "K-041: Höflichkeitsregeln beim Verlassen von Versammlungen",
        "quelle": "Sure 24: Vers 62",
        "ziel": "gebietet(zaid, einholen_erlaubnis_bei_abwesenheit)",
        "positive": [
            ("in_gemeinsamer_angelegenheit(zaid)", "Befindet sich die Person in einer kollektiven Versammlung?")
        ],
        "sperren": []
    },
    "K-042": {
        "titel": "K-042: Verbot verschwenderischer Verschwendung (Isrāf & Tabḏīr)",
        "quelle": "Sure 17: Verse 26–27; Sure 7: Vers 31",
        "ziel": "untersagt(zaid, verschwendung_von_mitteln)",
        "positive": [
            ("taetigt_ausgabe_ohne_mass(zaid)", "Werden Mittel sinnlos oder verschwenderisch verausgabt?")
        ],
        "sperren": []
    },
    "K-043": {
        "titel": "K-043: Verbot des Kindsmords aus Armut",
        "quelle": "Sure 17: Vers 31; Sure 6: Vers 151; Sure 81: Vers 8–9",
        "ziel": "untersagt(zaid, toetung_kinder_aus_armut)",
        "positive": [
            ("befuerchtet_armut_oder_besitznot(zaid)", "Besteht die Tötungsabsicht aufgrund von Armutssorgen?")
        ],
        "sperren": []
    },
    "K-044": {
        "titel": "K-044: Gebot der elterlichen Fürsorge im Alter",
        "quelle": "Sure 17: Verse 23–24",
        "ziel": "gebietet(zaid, guete_gegen_eltern)",
        "positive": [
            ("erreichen_eltern_hoeheres_alter(eltern1, zaid)", "Erreichen die Eltern im Haushalt das Greisenalter?")
        ],
        "sperren": []
    },
    "K-045": {
        "titel": "K-045: Respektvoller Umgang mit Verwandten und Bedürftigen",
        "quelle": "Sure 17: Vers 26",
        "ziel": "gebietet(zaid, recht_von_verwandten_und_armen)",
        "positive": [
            ("ist_verwandter_oder_beduerftiger(amr)", "Besteht ein Verwandtschaftsverhältnis oder Bedürftigkeit?")
        ],
        "sperren": []
    },
    "K-046": {
        "titel": "K-046: Das Maßgebot bei Verträgen",
        "quelle": "Sure 17: Vers 35",
        "ziel": "gebietet(zaid, exaktes_messen_und_waegen)",
        "positive": [
            ("durchfuehrung_waage_und_mass(vertrag1)", "Findet eine Güterübergabe mit Maßen statt?")
        ],
        "sperren": []
    },
    "K-047": {
        "titel": "K-047: Verbot von Annahmen ohne Wissen (Verstandesdisziplin)",
        "quelle": "Sure 17: Vers 36",
        "ziel": "untersagt(zaid, urteil_ohne_wissen_und_sinnespruefung)",
        "positive": [
            ("urteilt_ohne_gesicherte_wahrnehmung(zaid)", "Wird ohne Fundament oder Überprüfung geurteilt?")
        ],
        "sperren": []
    },
    "K-048": {
        "titel": "K-048: Verbot von Hochmut auf Erden",
        "quelle": "Sure 17: Vers 37",
        "ziel": "untersagt(zaid, arroganz_und_boden_stampfen)",
        "positive": [
            ("auftreten_in_ueberheblichkeit(zaid)", "Tritt die Person anmaßend auf?")
        ],
        "sperren": []
    },
    "K-049": {
        "titel": "K-049: Schutz des Privateigentums und Einbruchverbot",
        "quelle": "Sure 24: Vers 28–29",
        "ziel": "untersagt(zaid, betreten_unbewohnter_gebaeude_ohne_recht)",
        "positive": [
            ("betritt_oeffentlichen_oder_fremden_raum_widrechtig(zaid)", "Wird fremder Raum unbefugt betreten?")
        ],
        "sperren": []
    },
    "K-050": {
        "titel": "K-050: Senken des Blicks und sexuelle Disziplin",
        "quelle": "Sure 24: Verse 30–31",
        "ziel": "gebietet(zaid, senken_des_blicks)",
        "positive": [
            ("konfrontiert_mit_oeffentlichem_raum(zaid)", "Befindet sich die Person im Begegnungsraum?")
        ],
        "sperren": []
    },

    "K-051": {
        "titel": "K-051: Vorgehen bei drohendem Vertragsbruch (Nabdh)",
        "quelle": "Sure 8: Vers 58",
        "ziel": "gebietet(staat, offene_kuendigung_vertrag(gegner1))",
        "positive": [
            ("befuerchtet_verrat_vertragspartner(gegner1)", "Besteht begründeter Verdacht auf Verrat oder Vertragsbruch?")
        ],
        "sperren": [
            ("aufrecht_und_treu_gegner(gegner1)", "Hält sich die Gegenpartei nachweislich an den Vertrag?")
        ]
    },
    "K-052": {
        "titel": "K-052: Mobilmachung & Abschreckung im Verteidigungsfall",
        "quelle": "Sure 8: Vers 60",
        "ziel": "gebietet(staat, bereithaltung_streitkraft_und_mittel)",
        "positive": [
            ("besteht_staatsbedrohung_oder_feindesabsicht", "Liegt eine akute Bedrohung der Sicherheit vor?")
        ],
        "sperren": []
    },
    "K-053": {
        "titel": "K-053: Friedensbereitschaft bei feindlichem Einlenken",
        "quelle": "Sure 8: Vers 61",
        "ziel": "gebietet(staat, neigung_zum_frieden(gegner1))",
        "positive": [
            ("neigt_gegner_zum_frieden(gegner1)", "Signalisiert der Feind echten Friedenswillen?")
        ],
        "sperren": []
    },
    "K-054": {
        "titel": "K-054: Kriegsgefangenen-Ordnung & Lösegeld",
        "quelle": "Sure 47: Vers 4; Sure 8: Vers 67–70",
        "ziel": "gebietet(staat, behandlung_gefangene_und_loesegeld(delikt1))",
        "positive": [
            ("befindet_sich_im_kriegszustand_und_gefangennahme", "Wurden Gefangene im rechtmäßigen Konflikt gemacht?")
        ],
        "sperren": []
    },
    "K-055": {
        "titel": "K-055: Asylrecht & Schutzgewährung für Schutzsuchende (Musta'min)",
        "quelle": "Sure 9: Vers 6",
        "ziel": "gebietet(zaid, gewaehrung_geleit_und_schutz(amr))",
        "positive": [
            ("ersucht_schutz_und_asyl(amr)", "Ersucht ein Nicht-Muslim um Schutz und Geleit?")
        ],
        "sperren": [
            ("offenkundiger_bruch_oder_gefahr(amr)", "Liegt eine akute Sicherheitsgefahr durch den Asylsuchenden vor?")
        ]
    },
    "K-056": {
        "titel": "K-056: Loyalitätsverbot gegenüber feindlichen Allianzpartnern",
        "quelle": "Sure 60: Vers 1; Sure 3: Vers 28",
        "ziel": "untersagt(zaid, bbuendnis_mit_feinden_gegen_gemeinschaft(amr))",
        "positive": [
            ("unterhaelt_geheime_feindliche_allianz(zaid, amr)", "Werden geheime Bündnisse mit erklärten Feinden unterhalten?")
        ],
        "sperren": []
    },
    "K-057": {
        "titel": "K-057: Prüfung auswandernder Gläubigerinnen (Mumtahanah)",
        "quelle": "Sure 60: Vers 10",
        "ziel": "gebietet(staat, pruefung_und_rueckgabe_bei_glauben(amina))",
        "positive": [
            ("ist_ausgewanderte_glaeubige_frau(amina)", "Ist eine gläubige Frau als Emigrantin eingetroffen?")
        ],
        "sperren": [
            ("ist_unglaeubig_und_täuscht(amina)", "Liegt Täuschung oder fehlender Glaube vor?")
        ]
    },
    "K-058": {
        "titel": "K-058: Verbot der Eheschließung mit feindlichen Ungläubigen im Kriegszustand",
        "quelle": "Sure 60: Vers 10",
        "ziel": "untersagt(zaid, eheschliessung_mit_kriegsgegnerin(amina))",
        "positive": [
            ("verbleibt_gegnerin_im_kriegszustand(amina)", "Verbleibt die Person im feindlichen Lager?")
        ],
        "sperren": []
    },
    "K-059": {
        "titel": "K-059: Eidliche Verpflichtung der Frauen (Bay'at al-Nisa)",
        "quelle": "Sure 60: Vers 12",
        "ziel": "gebietet(staat, annahme_treue_eid_frauen(gruppe_frauen))",
        "positive": [
            ("erscheinen_frauen_zur_treue_erklaerung(gruppe_frauen)", "Erscheinen gläubige Frauen zur formalen Selbstverpflichtung?")
        ],
        "sperren": []
    },
    "K-060": {
        "titel": "K-060: Verbot der Allianz mit dem Zorn Gottes verfallenen Gruppen",
        "quelle": "Sure 60: Vers 13",
        "ziel": "untersagt(zaid, enge_freundschaft_mit_feindgruppen)",
        "positive": [
            ("schliesst_buendnis_mit_bekannten_feinden_der_wahrheit(zaid)", "Werden Bündnisse mit Gruppen geschlossen, die den Frieden brechen?")
        ],
        "sperren": []
    },
    "K-061": {
        "titel": "K-061: Verbot der Lüge über Gott (Falsche Gesetzgebung)",
        "quelle": "Sure 6: Vers 140, 144; Sure 16: Vers 116",
        "ziel": "untersagt(zaid, erfindung_luege_ueber_erlaubt_und_verboten)",
        "positive": [
            ("behauptet_göttliches_verbot_ohne_offenbarung(zaid)", "Werden rein menschliche Willkürakte als religiöse Gesetze ausgegeben?")
        ],
        "sperren": []
    },
    "K-062": {
        "titel": "K-062: Speise-Ausnahmen in absoluter Notsituation (Ḍarورة)",
        "quelle": "Sure 6: Vers 145; Sure 2: Vers 173",
        "ziel": "gestattet(zaid, verzehr_verbotener_speise_in_not)",
        "positive": [
            ("befindet_sich_in_lebensgefahr_durch_hunger(zaid)", "Befindet sich die Person in akuter, unverschuldeter Lebensgefahr?"),
            ("keine_begierde_oder_ueberschreitung(zaid)", "Es liegt keine Willkür oder Maßlosigkeit vor.")
        ],
        "sperren": []
    },
    "K-063": {
        "titel": "K-063: Das universelle Tötungsverbot von Menschenleben",
        "quelle": "Sure 6: Vers 151; Sure 17: Vers 33",
        "ziel": "untersagt(zaid, toetung_menschenleben_ohne_recht)",
        "positive": [
            ("versetzt_toetungsimpuls_ohne_gerechten_grund(zaid)", "Wird ein Mensch ohne rechtlichen Grund (wie Vergeltung oder Korruption) getötet?")
        ],
        "sperren": []
    },
    "K-064": {
        "titel": "K-064: Schutz des Waisenvermögens bis zur Volljährigkeit",
        "quelle": "Sure 6: Vers 152",
        "ziel": "gebietet(zaid, bewahrung_waisenvermoegen_bis_reife)",
        "positive": [
            ("verwaltet_waisenvermoegen(zaid, waisenkind1)", "Verwaltet die Person Waisenvermögen?")
        ],
        "sperren": []
    },
    "K-065": {
        "titel": "K-065: Gebot der Aufrichtigkeit bei Aussagen und Urteilen",
        "quelle": "Sure 6: Vers 152",
        "ziel": "gebietet(zaid, gerechtigkeit_auch_bei_verwandten)",
        "positive": [
            ("spricht_als_zeuge_oder_richter(zaid)", "Fällt die Person ein Urteil oder gibt Zeugnis ab?")
        ],
        "sperren": []
    },
    "K-066": {
        "titel": "K-066: Verbot der Sektiererischen Spaltung der Religion",
        "quelle": "Sure 6: Vers 159",
        "ziel": "untersagt(zaid, spaltung_der_religion_in_parteien)",
        "positive": [
            ("zerbricht_einheit_durch_sektierertum(zaid)", "Wird die Religionsgemeinschaft willkürlich zerstückelt und sektiererisch gespalten?")
        ],
        "sperren": []
    },
    "K-067": {
        "titel": "K-067: Verbot falscher Anschuldigungen gegen Aufrichtige",
        "quelle": "Sure 6: Vers 52–53; Sure 24: Vers 11",
        "ziel": "untersagt(zaid, verleumdung_glaeubiger)",
        "positive": [
            ("schmaeht_glaeubige_auf_suche_nach_wahrheit(zaid, amr)", "Werden aufrichtige Gläubige geschmäht?")
        ],
        "sperren": []
    },
    "K-068": {
        "titel": "K-068: Das Prinzip der individuellen Verantwortlichkeit",
        "quelle": "Sure 6: Vers 164; Sure 17: Vers 15",
        "ziel": "gebietet(staat, haftungsausschluss_fuer_fremde_schuld(zaid))",
        "positive": [
            ("soll_bestraft_werden_fuer_fremdetat(zaid)", "Soll eine Person für die Tat einer anderen haftbar gemacht werden?")
        ],
        "sperren": []
    },
    "K-069": {
        "titel": "K-069: Gebot des guten Wortes im sozialen Verkehr",
        "quelle": "Sure 17: Vers 53; Sure 41: Vers 34",
        "ziel": "gebietet(zaid, sprechen_des_besten_wortes)",
        "positive": [
            ("fuehrt_gespraech_im_oeffentlichen_raum(zaid)", "Findet ein alltägliches Gespräch statt?")
        ],
        "sperren": []
    },
    "K-070": {
        "titel": "K-070: Verbot der Höllen-Provokation durch Spott über Gottheiten anderer",
        "quelle": "Sure 6: Vers 108",
        "ziel": "untersagt(zaid, beschimpfung_fremder_kulte_aus_provokation)",
        "positive": [
            ("schmäht_fremde_symbole_ohne_not(zaid)", "Werden Kultsymbole anderer absichtlich beschimpft, um Gegenreaktionen zu provozieren?")
        ],
        "sperren": []
    },
    "K-071": {
        "titel": "K-071: Prüfung von Nachrichten durch Frevler (Tabayyun)",
        "quelle": "Sure 49: Vers 6",
        "ziel": "gebietet(zaid, ueberpruefung_nachricht_von_fasik(nachricht1))",
        "provenienz": "Sure 49:6",
        "positive": [
            ("stammt_nachricht_von_fasik(nachricht1)", "Bringt eine unzuverlässige/falsche Person (Fāsiq) eine Nachricht?")
        ],
        "sperren": [
            ("bestätigt_durch_untersuchung(nachricht1)", "Wurde die Nachricht unabhängig verifiziert?")
        ]
    },
    "K-072": {
        "titel": "K-072: Schlichtung bei innerislamischen Konflikten (Baghy)",
        "quelle": "Sure 49: Vers 9–10",
        "ziel": "gebietet(staat, bewaffnete_schlichtung_gegen_aggressor_gruppe(gruppe1))",
        "positive": [
            ("kaempfen_zwei_glaeubige_gruppen_untereinander(gruppe1, gruppe2)", "Bekämpfen sich zwei Gruppen von Gläubigen?"),
            ("weigert_sich_eine_seite_zu_frieden(gruppe1)", "Weigert sich eine Partei trotz Vermittlung einzulenken?")
        ],
        "sperren": []
    },
    "K-073": {
        "titel": "K-073: Verbot von Nachrede, Spionage und übler Nachrede",
        "quelle": "Sure 49: Vers 11–12",
        "ziel": "untersagt(zaid, spionage_und_ueble_nachrede(amr))",
        "positive": [
            ("betreibt_spionage_oder_laesterung(zaid, amr)", "Wird hinter dem Rücken gelästert oder spioniert?")
        ],
        "sperren": []
    },
    "K-074": {
        "titel": "K-074: Das Prinzip der moralischen Gleichwertigkeit der Menschen",
        "quelle": "Sure 49: Vers 13",
        "ziel": "gebietet(staat, gleichbehandlung_ohne_stammesarrogance)",
        "positive": [
            ("beurteilt_nach_abstammung_statt_frommkeit(zaid)", "Wird ein Mensch aufgrund seiner Herkunft diskriminiert?")
        ],
        "sperren": []
    },
    "K-075": {
        "titel": "K-075: Nachweis des wahren Glaubens vs. bloßem Lippenbekenntnis",
        "quelle": "Sure 49: Vers 14–15",
        "ziel": "untersagt(zaid, beanspruchung_islam_status_ohne_tat)",
        "positive": [
            ("behauptet_islam_ohne_herzensvollzug(zaid)", "Wird der Glaube nur als Schutzbehauptung ohne innere Tat proklamiert?")
        ],
        "sperren": []
    },
    "K-076": {
        "titel": "K-076: Das Verbot des Vertrauensbruchs bei Schutzverträgen",
        "quelle": "Sure 9: Vers 1–4",
        "ziel": "gebietet(staat, einhaltung_vertraege_mit_treuen_gegenparteien)",
        "positive": [
            ("besteht_beidseitiger_friedensvertrag(vertrag1)", "Existiert ein intakter Friedensvertrag?")
        ],
        "sperren": [
            ("bruch_vertrag_durch_gegner", "Hat die Gegenpartei den Vertrag gebrochen?")
        ]
    },
    "K-077": {
        "titel": "K-077: Der Schutz von Götzendienern bei Schutzersuchen",
        "quelle": "Sure 9: Vers 6",
        "ziel": "gebietet(zaid, gewaehrung_gehör_und_geleit)",
        "positive": [
            ("bittet_polytheist_um_gehör_und_schutz(amr)", "Bittet ein Polytheist um Gehör und sicheres Geleit?")
        ],
        "sperren": []
    },
    "K-078": {
        "titel": "K-078: Verbot der Vertragstreue-Bruchs durch treulose Verbündete",
        "quelle": "Sure 9: Vers 7–8",
        "ziel": "gebietet(staat, kuendigung_vertrag_bei_nachgewiesenem_verrat)",
        "positive": [
            ("offenkundiger_verrat_und_eidbruch(gegner1)", "Liegt offenkundiger Verrat vor?")
        ],
        "sperren": []
    },
    "K-079": {
        "titel": "K-079: Verbot des Verkaufs von Offenbarungszeichen für geringen Preis",
        "quelle": "Sure 9: Vers 9",
        "ziel": "untersagt(zaid, kommerzialisierung_religion_gegen_vorteil)",
        "positive": [
            ("tauscht_verse_gegen_weltlichen_vorteil(zaid)", "Werden religiöse Gebote für weltlichen Profit verbogen?")
        ],
        "sperren": []
    },
    "K-080": {
        "titel": "K-080: Verbot des Betens für notorische Ungläubige nach dem Tod",
        "quelle": "Sure 9: Vers 84",
        "ziel": "untersagt(zaid, totengebet_fuer_erklaerte_feinde_gottes)",
        "positive": [
            ("verstorben_als_erklaerter_feind_der_ordnung(amr)", "Ist die Person als erklärter Feind verstorben?")
        ],
        "sperren": []
    },
    "K-081": {
        "titel": "K-081: Gebot der Rechtschaffenheit und des Exils bei Heuchelei",
        "quelle": "Sure 9: Vers 101–102",
        "ziel": "gebietet(staat, ueberwachung_und_sanktion_heuchelei)",
        "positive": [
            ("nachgewiesene_subversion_durch_heuchler(gruppe1)", "Wurde organisierte Subversion nachgewiesen?")
        ],
        "sperren": []
    },
    "K-082": {
        "titel": "K-082: Spende und Zakāt-Annahmepflicht durch den Staat",
        "quelle": "Sure 9: Vers 103",
        "ziel": "gebietet(staat, einziehung_und_reinigung_durch_zakat(zaid))",
        "positive": [
            ("entrichtet_zakat_freiwillig_oder_pflicht(zaid)", "Wird Zakāt zur Reinigung des Vermögens entrichtet?")
        ],
        "sperren": []
    },
    "K-083": {
        "titel": "K-083: Verbot der Errichtung von parteiischen Schädigungs-Moscheen",
        "quelle": "Sure 9: Vers 107–108",
        "ziel": "untersagt(zaid, unterhalt_schädigender_infrastruktur)",
        "positive": [
            ("dient_einrichtung_der_spaltung_und_spionage(gebaeude1)", "Dient ein Versammlungsort der Zersetzung?")
        ],
        "sperren": []
    },
    "K-084": {
        "titel": "K-084: Verbot des Fluchens und der Herabsetzung von Armen",
        "quelle": "Sure 9: Vers 79",
        "ziel": "untersagt(zaid, verspottung_arm_spendender)",
        "positive": [
            ("spottet_ueber_geringfuegige_spenden_armer(zaid)", "Wird über die Spenden von Geringverdienern gespottet?")
        ],
        "sperren": []
    },
    "K-085": {
        "titel": "K-085: Das Prinzip der Vergebung bei Reue im laufenden Konflikt",
        "quelle": "Sure 9: Vers 5; Sure 5: Vers 39",
        "ziel": "gebietet(staat, verschonung_bei_reue_und_gebet)",
        "positive": [
            ("vollzieht_reue_und_etabliert_gebet(amr)", "Kehrt der Gegner um und stellt die Feindseligkeit ein?")
        ],
        "sperren": []
    },
    "K-086": {
        "titel": "K-086: Verbot des Zwangskonsum von Frauen als Erbschaftsobjekt",
        "quelle": "Sure 4: Vers 19",
        "ziel": "untersagt(zaid, erbschaft_an_frauen_gegen_willen)",
        "positive": [
            ("behandelt_witwe_als_verfügungsmasse(zaid, amina)", "Wird eine Witwe als Erbschaftsobjekt behandelt?")
        ],
        "sperren": []
    },
    "K-087": {
        "titel": "K-087: Verbot der unberechtigten Mahr-Rückforderung (Erpressung)",
        "quelle": "Sure 4: Vers 20–21",
        "ziel": "untersagt(zaid, entzug_schenkung_bei_scheidung)",
        "positive": [
            ("fordert_geschenkte_mahr_zurueck_durch_druck(zaid, amina)", "Wird die Mahr durch Schikanen zurückgefordert?")
        ],
        "sperren": []
    },
    "K-088": {
        "titel": "K-088: Erweiterte Heiratsverbote durch Schwägerschaft",
        "quelle": "Sure 4: Vers 23",
        "ziel": "untersagt(zaid, eheschliessung_schwaegerin_oder_mutter)",
        "positive": [
            ("besteht_schwaegerschaftliches_verbot(zaid, amina)", "Besteht ein Verbot durch Schwägerschaft?")
        ],
        "sperren": []
    },
    "K-089": {
        "titel": "K-089: Verbot des Ehebruchs mit verheirateten Frauen (Muḥṣanāt)",
        "quelle": "Sure 4: Vers 24",
        "ziel": "untersagt(zaid, unzucht_mit_verheirateter_frau(amina))",
        "positive": [
            ("ist_verheiratete_frau_ohne_entlassung(amina)", "Ist die Frau mit einem anderen verheiratet?")
        ],
        "sperren": []
    },
    "K-090": {
        "titel": "K-090: Heiratserlaubnis für Sklavinnen unter strengen Auflagen",
        "quelle": "Sure 4: Vers 25",
        "ziel": "gebietet(zaid, einholung_erlaubnis_herren_fuer_sklavin)",
        "positive": [
            ("heiratet_sklavin_mit_zustimmung_herrschaft(zaid, sklavin1)", "Erfolgt die Heirat mit Zustimmung der Eigner?")
        ],
        "sperren": []
    },
    "K-091": {
        "titel": "K-091: Verbot des Selbstmords und der gegenseitigen Vernichtung",
        "quelle": "Sure 4: Vers 29–30",
        "ziel": "untersagt(zaid, selbstoetung_oder_besitzvernichtung)",
        "positive": [
            ("vollzieht_selbstbeschaedigung_oder_suizid(zaid)", "Wird das eigene Leben oder der Körper zerstört?")
        ],
        "sperren": []
    },
    "K-092": {
        "titel": "K-092: Pflicht zur Vermeidung schwerer Sünden (Kabā'ir)",
        "quelle": "Sure 4: Vers 31",
        "ziel": "gebietet(zaid, meidung_grosser_suenden)",
        "positive": [
            ("steht_vor_entscheidung_zu_grossem_vergehen(zaid)", "Steht eine schwere Übertretung an?")
        ],
        "sperren": []
    },
    "K-093": {
        "titel": "K-093: Verbot des Neids auf göttliche Vergabe von Vorzügen",
        "quelle": "Sure 4: Vers 32",
        "ziel": "untersagt(zaid, neid_auf_zuteilung_anderer)",
        "positive": [
            ("begehrt_eifersuechtig_fremden_vorzug(zaid)", "Wird der Neid auf die Gaben anderer manifestiert?")
        ],
        "sperren": []
    },
    "K-094": {
        "titel": "K-094: Männliche Führungsverantwortung (Qiwāmah) und Gerechtigkeit",
        "quelle": "Sure 4: Vers 34",
        "ziel": "gebietet(zaid, fuersorge_und_verantwortung_in_familie)",
        "positive": [
            ("traegt_finanzielle_verantwortung_familie(zaid)", "Trägt die Person die wirtschaftliche Hauptlast?")
        ],
        "sperren": []
    },
    "K-095": {
        "titel": "K-095: Schiedsrichter-Entsendung bei unlösbarem Ehestreit",
        "quelle": "Sure 4: Vers 35",
        "ziel": "gebietet(staat, entsendung_schiedsrichter_familie(zaid, amina))",
        "positive": [
            ("droht_bruch_der_ehe_durch_beidseitigen_konflikt(zaid, amina)", "Droht die Zerrüttung der Ehe?")
        ],
        "sperren": []
    },
    "K-096": {
        "titel": "K-096: Gebot der umfassenden Nächstenliebe und Güte",
        "quelle": "Sure 4: Vers 36",
        "ziel": "gebietet(zaid, guete_gegen_eltern_nachbarn_und_armer)",
        "positive": [
            ("besteht_sozialer_kontakt_im_quartier(zaid, amr)", "Besteht sozialer Kontakt im Umfeld?")
        ],
        "sperren": []
    },
    "K-097": {
        "titel": "K-097: Verbot des Geizes und der Prahlerei mit Reichtum",
        "quelle": "Sure 4: Vers 36–37",
        "ziel": "untersagt(zaid, geiz_und_prahlerei_mit_guetern)",
        "positive": [
            ("haelt_mittel_zurück_und_prahlt(zaid)", "Wird Reichtum zur Schau gestellt und Bedürftigen Hilfe verweigert?")
        ],
        "sperren": []
    },
    "K-098": {
        "titel": "K-098: Verbot des verdeckten Gebets in Trunkenheit",
        "quelle": "Sure 4: Vers 43",
        "ziel": "untersagt(zaid, verrichtung_gebet_in_trunkenheit)",
        "positive": [
            ("befindet_sich_in_alkoholisiertem_zustand(zaid)", "Steht die Person unter Alkoholeinfluss?"),
            ("beabsichtigt_gebet(zaid)", "Soll das rituelle Gebet vollzogen werden?")
        ],
        "sperren": []
    },
    "K-099": {
        "titel": "K-099: Pflicht zur rituellen Waschung vor dem Gebet",
        "quelle": "Sure 5: Vers 6; Sure 4: Vers 43",
        "ziel": "gebietet(zaid, wudu_oder_tayammum_vor_gebet)",
        "positive": [
            ("beabsichtigt_gebet_ohne_reinheit(zaid)", "Wird das Gebet ohne rituelle Reinheit angestrebt?")
        ],
        "sperren": [
            ("krank_oder_auf_reisen_ersatz_tayammum(zaid)", "Liegt eine Ausnahme (Reise/Krankheit) mit Tayammum vor?")
        ]
    },
    "K-100": {
        "titel": "K-100: Das Verbot des Zeugnisses aus Parteinahme (Gerechtigkeit für Feinde)",
        "quelle": "Sure 5: Vers 8",
        "ziel": "gebietet(zaid, unparteiisches_zeugnis_trotz_feindschaft)",
        "positive": [
            ("ist_zeuge_gegen_freunde_oder_fuer_feinde(zaid)", "Wird ein Zeugnis abgegeben, das die eigene Partei belasten könnte?")
        ],
        "sperren": []
    },
    "K-101": {
        "titel": "K-101: Verbot des Verrats an anvertrautem Gut",
        "quelle": "Sure 5: Vers 1; Sure 8: Vers 27",
        "ziel": "untersagt(zaid, verrat_an_anvertrautem_gut(anweisung1))",
        "positive": [
            ("wird_anvertraut_gegenstand_oder_geheimnis(zaid)", "Wird ein Gut treuhänderisch verwaltet?")
        ],
        "sperren": []
    },
    "K-102": {
        "titel": "K-102: Verbot der Beihilfe zu Sünde und feindseliger Aggression",
        "quelle": "Sure 5: Vers 2",
        "ziel": "untersagt(zaid, kooperation_bei_suende_und_uebertretung)",
        "positive": [
            ("unterstuetzt_aktiv_rechtsbruch_oder_agression(zaid)", "Wird Beihilfe zu einer gesetzwidrigen Tat geleistet?")
        ],
        "sperren": []
    },
    "K-103": {
        "titel": "K-103: Gebot der gegenseitigen Hilfe in Frömmigkeit und Gutes",
        "quelle": "Sure 5: Vers 2",
        "ziel": "gebietet(zaid, kooperation_in_guete_und_frommkeit)",
        "positive": [
            ("besteht_gemeinsames_soziales_oder_frommes_vorhaben(zaid)", "Wird ein positives, gemeinnütziges Projekt gestartet?")
        ],
        "sperren": []
    },
    "K-104": {
        "titel": "K-104: Strafrechtliche Verfolgung von Mord und Korruption im Land",
        "quelle": "Sure 5: Vers 32",
        "ziel": "gebietet(staat, schutz_menschenleben_als_gesamtheit)",
        "positive": [
            ("droht_vernichtung_menschenleben_durch_tat(delikt1)", "Liegt ein Verbrechen gegen das Leben vor?")
        ],
        "sperren": []
    },
    "K-105": {
        "titel": "K-105: Zeugnisregeln bei testamentarischen Verfügungen auf Reisen",
        "quelle": "Sure 5: Verse 106–107",
        "ziel": "gebietet(staat, vereidigung_zeugen_bei_zweifel_an_testament)",
        "positive": [
            ("tritt_todesfall_auf_reise_ohne_glaubensgenossen_ein(vertrag1)", "Tritt ein Todesfall in der Fremde auf?")
        ],
        "sperren": []
    },
    "K-106": {
        "titel": "K-106: Das Verbot des Fragens nach Dingen, die zur Last werden",
        "quelle": "Sure 5: Vers 101–102",
        "ziel": "untersagt(zaid, ueberspitzte_kasuistik_und_hypothetische_streiterei)",
        "positive": [
            ("erzwingt_ueberspitzte_regeln_ohne_offenbarung(zaid)", "Werden rein hypothetische Gesetze erzwungen, die das Leben unnötig erschweren?")
        ],
        "sperren": []
    },
    "K-107": {
        "titel": "K-107: Verbot der Verfluchung anderer Religionen bei Wahrung der eigenen",
        "quelle": "Sure 6: Vers 108",
        "ziel": "untersagt(zaid, verunglimpfung_fremder_gott_anbetung)",
        "positive": [
            ("schmaeht_bewusst_fremde_heiligtuemer(zaid)", "Werden fremde Heiligtümer verunglimpft?")
        ],
        "sperren": []
    },
    "K-108": {
        "titel": "K-108: Das Prinzip der universellen Rechenschaft am Jüngsten Tag",
        "quelle": "Sure 6: Vers 62, 162; Sure 5: Vers 109",
        "ziel": "gebietet(zaid, ausrichtung_handeln_auf_letzte_verantwortung)",
        "positive": [
            ("ist_moralischer_haushalt_des_lebens_aktiv(zaid)", "Ist die ethische Gesamtausrichtung des Handelns aktiv?")
        ],
        "sperren": []
    }
}
