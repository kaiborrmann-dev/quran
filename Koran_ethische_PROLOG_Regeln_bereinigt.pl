% ==============================================================================
% MUTTER-WISSENSBASIS: KORANISCHE NORMATIVITÄT & ETHIK
% BLOCK 1 / 4: KOMPLEXE K-001 BIS K-030
% Status: Vollständig, unverkürzt, harmonisiertes Vokabular (Blöcke 1-5)
% ==============================================================================

% ==============================================================================
% DYNAMISCHE PRÄDIKATE (INTERPRETER-DEKLARATION)
% ==============================================================================
:- dynamic quelle/2.
:- dynamic gebietet/2.
:- dynamic untersagt/2.
:- dynamic gestattet/2.
:- dynamic teilmenge/2.
:- dynamic disjunkt/2.
:- dynamic adresse_jilbab_gebot/1.
:- dynamic erfuellt_kaffarah/1.
:- dynamic erfuellt_kaffarah_zihar/1.
:- dynamic erfuellt_kaffarah_jagd/2.




% ------------------------------------------------------------------------------
% K-001: KISAṢ (DELIKT, VERGELTUNG & BLUTGELD)
% ------------------------------------------------------------------------------
quelle(kisas_und_blutgeld, sura_2_verse_178_179).
quelle(kisas_und_blutgeld, sura_5_verse_45).
quelle(kisas_und_blutgeld, sura_17_verse_33).

gebietet(staat, kisas_vergeltung(D)) :-
    ist_delikt(D, Taelter, Opfer),
    delikttyp(D, vorsaetzliche_toetung),
    \+ gewaehrt_verzeihung(Opfer, Taelter, D).

gestattet(Taelter, diya_blutgeld(D)) :-
    ist_delikt(D, Taelter, Opfer),
    delikttyp(D, vorsaetzliche_toetung),
    gewaehrt_verzeihung(Opfer, Taelter, D).

% ------------------------------------------------------------------------------
% K-002: TESTAMENT UND ERBRECHTLICHE VERFÜGUNG (WASIYYAH)
% ------------------------------------------------------------------------------
quelle(testament_wasiyya, sura_2_verse_180_182).
quelle(testament_wasiyya, sura_5_verse_106_108).

gebietet(X, abfassen_testament) :-
    hat_vermoegen(X),
    befuerchtet_ableben(X).

untersagt(Y, aenderung_testament(T)) :-
    ist_testament(T),
    erblasser_verstorben(Y).

% ------------------------------------------------------------------------------
% K-003: FASTENORDNUNG & KULTISCHE DISPENSE (ṢIYĀM)
% ------------------------------------------------------------------------------
quelle(fastenordnung_ramadan, sura_2_verse_183_185).
quelle(fastenordnung_ramadan, sura_2_verse_187).

gebietet(X, fasten_ramadan) :-
    ist_glaeubig(X),
    \+ krank(X),
    \+ auf_reisen(X).

gebietet(X, nachholen_fasttage) :-
    ist_glaeubig(X),
    (krank(X) ; auf_reisen(X)).

gestattet(X, intimitaet_ehepartner) :-
    ist_glaeubig(X),
    in_ramadan_nacht(X).

% ------------------------------------------------------------------------------
% K-004: WIRTSCHAFTSETHIK & ZINSVERBOT (RIBĀ)
% ------------------------------------------------------------------------------
quelle(zinsverbot_riba, sura_2_verse_275_279).
quelle(zinsverbot_riba, sura_3_verse_130).
quelle(zinsverbot_riba, sura_30_verse_39).

untersagt(X, vollzug_transaktion(T)) :-
    taetigt_transaktion(X, T),
    beinhaltet_riba(T).

gestattet(X, vollzug_transaktion(T)) :-
    taetigt_transaktion(X, T),
    ist_wirtschaftstransaktion(T),
    \+ beinhaltet_riba(T).

disjunkt(j_al_akiluna_ar_riba, j_al_muta_arrifina_bi_l_falah).

% ------------------------------------------------------------------------------
% K-005: DOKUMENTATION, SCHULDENVERTRAG & ZEUGENSCHAFT
% ------------------------------------------------------------------------------
quelle(schuldenvertrag_und_zeugen, sura_2_verse_282_283).

gebietet(X, schriftform_dokumentation(T)) :-
    taetigt_transaktion(X, T),
    ist_befristete_schuld(T, S, G, V).

gebietet(X, zuziehung_zeugen(T)) :-
    taetigt_transaktion(X, T),
    ist_befristete_schuld(T, S, G, V).

gestattet(G, pfandnahme(P)) :-
    ist_befristete_schuld(T, S, G, V),
    \+ findet_schreiber(S, G).

% ------------------------------------------------------------------------------
% K-006: EHEVERBOTE (MAḤRAM) & EHESTRUKTUR
% ------------------------------------------------------------------------------
quelle(eheverbote_mahram, sura_4_verse_22_24).
quelle(eheverbote_mahram, sura_2_verse_221).
quelle(eheverbote_mahram, sura_60_verse_10).

untersagt(M, eheschliessung(F)) :-
    ist_mahram(M, F).

gestattet(M, eheschliessung(F)) :-
    \+ ist_mahram(M, F).

% ------------------------------------------------------------------------------
% K-007: EHEKONFLIKTE, NUŠŪZ UND SCHLICHTUNG
% ------------------------------------------------------------------------------
quelle(ehekonflikte_und_schlichtung, sura_4_verse_34_35).
quelle(ehekonflikte_und_schlichtung, sura_4_verse_128).

gebietet(staat, schlichtungsverfahren(M, F)) :-
    ist_ehepartner(M, F),
    ehekonflikt_unueberbrueckbar(M, F).

gestattet(M, gattliche_versöhnung(F)) :-
    ist_ehepartner(M, F),
    bereitschaft_zu_frieden(M, F).

% ------------------------------------------------------------------------------
% K-008: STATUT DER PROPHETENGATTINNEN (NISĀʾ AN-NABĪ)
% ------------------------------------------------------------------------------
quelle(statut_nisa_an_nabi, sura_33_verse_32_33).
quelle(statut_nisa_an_nabi, sura_33_verse_28_30).
quelle(statut_nisa_an_nabi, sura_66_verse_1_5).

untersagt(X, weiche_intonation) :-
    prophetengattin(X),
    in_gespraechsfuehrung(X).

gebietet(X, sachliche_ansprache) :-
    prophetengattin(X),
    in_oeffentlichkeit(X).

untersagt(X, tabarruj_jahiliyyah) :-
    prophetengattin(X).

disjunkt(j_muta_barrijat_tabarruj_al_jahiliyyah, j_al_muttaqiyat_min_nisa_an_nabi).

% ------------------------------------------------------------------------------
% K-009: BEKLEIDUNG & ÖFFENTLICHKEITSSTATUT (JILBĀB)
% ------------------------------------------------------------------------------
quelle(jilbab_und_bekleidung, sura_33_verse_59).
quelle(jilbab_und_bekleidung, sura_24_verse_31).

gebietet(X, ueberziehen_jilbab) :-
    adresse_jilbab_gebot(X),
    in_oeffentlichkeit(X).

adresse_jilbab_gebot(X) :- prophetengattin(X).
adresse_jilbab_gebot(X) :- prophetentochter(X).
adresse_jilbab_gebot(X) :- ist_glaeubig(X), ist_frau(X).

teilmenge(j_mudniyat_alayhinna_min_jalabibihinna, j_al_muta_arrifat_bi_l_iffah_wa_l_himayah).

% ------------------------------------------------------------------------------
% K-010: GERECHTIGKEITSPRINZIP (QIṢṬ) & PROZESSORDNUNG
% ------------------------------------------------------------------------------
quelle(prinzip_qist, sura_4_verse_135).
quelle(prinzip_qist, sura_5_verse_8).
quelle(prinzip_qist, sura_57_verse_25).
quelle(prinzip_qist, sura_16_verse_90).

gebietet(X, gerechtes_zeugnis(V)) :-
    ist_zeuge_in(X, V).

teilmenge(j_qaimina_bi_l_qist, j_muttabiina_lil_kutubi_wa_r_rusul).

% ------------------------------------------------------------------------------
% K-011: SHŪRĀ (BERATUNGSPRINZIP) & REZIPROZITÄT
% ------------------------------------------------------------------------------
quelle(shura_und_reziprozitaet, sura_42_verse_36_39).
quelle(shura_und_reziprozitaet, sura_42_verse_40_43).
quelle(shura_und_reziprozitaet, sura_3_verse_159).

gebietet(leiter, beratung_konsultation(Gruppe)) :-
    ist_gemeinschaftsentscheidung(Gruppe).

teilmenge(j_amruhum_shura_bainahum, j_lahum_ma_indallahi_khairun_wa_abqa).
teilmenge(j_man_intasara_ba_da_zulmihi, j_ma_alayhim_min_sabil).

% ------------------------------------------------------------------------------
% K-012: SOZIALETHIK (VERBOT VON SPOTT, GHĪBAH, SCHMÄHUNGEN)
% ------------------------------------------------------------------------------
quelle(sozialethik_und_ehrschutz, sura_49_verse_11).
quelle(sozialethik_und_ehrschutz, sura_49_verse_12).
quelle(sozialethik_und_ehrschutz, sura_104_verse_1).

untersagt(X, spott_ueber_andere(Y)) :-
    ist_glaeubig(X),
    ist_glaeubig(Y).

untersagt(X, ghibah_ueble_nachrede(Y)) :-
    ist_glaeubig(X),
    ist_glaeubig(Y).

teilmenge(j_lam_yatub_ba_da_s_sukhriyyah, j_az_zalimun).
disjunkt(j_al_mughtabuna_li_ikhwanihim, j_al_muttaquna_indallah).

% ------------------------------------------------------------------------------
% K-013: TAʿĀRUF (UNIVERSALISMUS & ANTHROPOLOGIE)
% ------------------------------------------------------------------------------
quelle(taaruf_und_universalismus, sura_49_verse_13).
quelle(taaruf_und_universalismus, sura_30_verse_22).

gebietet(X, kochen_und_kennenlernen(Y)) :-
    verschiedene_abstammung(X, Y).

teilmenge(j_atqaakum, j_akramakum_indallah).

% ------------------------------------------------------------------------------
% K-014: AUSSENVERHÄLTNIS ZU NICHT-MUSLIMEN (AḤKĀM GHAYR AL-MUSLIMĪN)
% ------------------------------------------------------------------------------
quelle(guete_zu_nicht_aggressoren, sura_60_verse_8_9).
quelle(guete_zu_nicht_aggressoren, sura_2_verse_190).

gebietet(X, guete_und_gerechtigkeit(Y)) :-
    ist_glaeubig(X),
    \+ ist_delikt(D, Y, X),
    (delikttyp(D, bekaempft_wegen_religion) ; delikttyp(D, vertreibt_aus_wohnstaette)).

untersagt(X, engbuendnis(Y)) :-
    ist_delikt(D, Y, X),
    (delikttyp(D, bekaempft_wegen_religion) ; delikttyp(D, vertreibt_aus_wohnstaette)).

teilmenge(j_al_muqsituna_ila_ghair_al_muqatilin, j_yuhibbihum_allah).
disjunkt(j_al_muwaliyuna_lil_mukhrijin, j_al_muminun).

% ------------------------------------------------------------------------------
% K-015: SCHEIDUNG (ṬALĀQ), ʿIDDAH & UNTERHALTSPFLICHTEN
% ------------------------------------------------------------------------------
quelle(scheidungsrecht_komplex, sura_2_verse_228_232).
quelle(scheidungsrecht_komplex, sura_65_verse_1_2).
quelle(scheidungsrecht_komplex, sura_65_verse_6_7).

gebietet(H, berechnung_iddah(F)) :-
    spricht_talaq_aus(H, F).

untersagt(H, ausweisung_aus_ehewohnung(F)) :-
    in_iddah_frist(F, H),
    \+ (ist_delikt(D, F, H), delikttyp(D, offenkundige_scheusslichkeit)).

gebietet(H, zuziehung_zweier_gerechter_zeugen) :-
    vollzieht_talaq_oder_rajah(H, _F).

gebietet(H, wohnsitzgewaehrung(F)) :-
    in_iddah_frist(F, H).

untersagt(H, schaedigung_zwecks_bedraengnis(F)) :-
    ist_geschieden(H, F).

gebietet(H, vollunterhalt(F)) :-
    ist_geschieden(H, F),
    ist_schwanger(F),
    unterhaltspflicht(H, F).

gebietet(H, stilllohn(F)) :-
    ist_geschieden(H, F),
    stillt_gemeinsames_kind(F, H),
    unterhaltspflicht(H, F).

teilmenge(j_al_munfiquna_ala_qadri_musaihim, j_la_yukallifullahu_nafsa_illa_ma_ataha).

% ------------------------------------------------------------------------------
% K-016: HANDELSMORAL, EICHWESEN & MAß (TAṬFĪF)
% ------------------------------------------------------------------------------
quelle(handelsmoral_tatfif, sura_83_verse_1_3).
quelle(handelsmoral_tatfif, sura_6_verse_152).
quelle(handelsmoral_tatfif, sura_17_verse_35).
quelle(handelsmoral_tatfif, sura_55_verse_9).

untersagt(X, vollzug_transaktion(T)) :-
    taetigt_transaktion(X, T),
    beinhaltet_tatfif(T).

disjunkt(j_al_mutaffifun, j_al_muta_arrifina_bi_l_falah).

% ------------------------------------------------------------------------------
% K-017: SPEISERECHT, RITUALSCHLACHTUNG & INTERRELIGIÖSER TISCH
% ------------------------------------------------------------------------------
quelle(speiserecht_und_reinheit, sura_5_verse_1_5).
quelle(speiserecht_und_reinheit, sura_2_verse_172_173).
quelle(speiserecht_und_reinheit, sura_6_verse_145).
quelle(speiserecht_und_reinheit, sura_16_verse_115).

untersagt(X, verzehr(S)) :-
    (ist_aas(S) ; ist_blut_fliessend(S) ; ist_schweinefleisch(S) ; ist_opfergabe_an_goetzen(S)),
    \+ notlage_fuer_ueberleben(X).

gestattet(X, verzehr(S)) :-
    \+ untersagt(X, verzehr(S)),
    (ordnungsgemaess_geschlachtet(S) ; jagdbeute_abgerichtet(S) ; meeresbeute(S)).

gestattet(X, verzehr(S)) :-
    ist_glaeubig(X),
    speise_der_schriftbesitzer(S),
    \+ untersagt(X, verzehr(S)).

disjunkt(j_al_akiluna_al_maitah_wa_d_dam, j_al_muttiuna_li_amrillah).

% ------------------------------------------------------------------------------
% K-018: EIDSCHWÜRE, EIDBRUCH & SÜHNELEISTUNG (KAFFĀRAH)
% ------------------------------------------------------------------------------
quelle(eidschwuere_und_kaffarah, sura_5_verse_89).
quelle(eidschwuere_und_kaffarah, sura_2_verse_224_225).
quelle(eidschwuere_und_kaffarah, sura_16_verse_91_92).

gebietet(X, einhaltung_eid(E)) :-
    eid_bekraeftigt(X, E),
    \+ verpflichtet_zu_suende(E).

gebietet(X, kaffarah(E)) :-
    eid_bekraeftigt(X, E),
    bricht_eid(X, E).

erfuellt_kaffarah(X) :- speisung_zehn_beduerftige(X).
erfuellt_kaffarah(X) :- bekleidung_zehn_beduerftige(X).
erfuellt_kaffarah(X) :- freikauf_sklavische_person(X).
erfuellt_kaffarah(X) :- \+ vermoegend_fuer_sachkaffarah(X), fasten_tage(X, 3).

teilmenge(j_al_hafizuna_li_aymanihim, j_al_muttaqun).

% ------------------------------------------------------------------------------
% K-019: BEUTERECHT, FISKAL- UND STAATSVERMÖGEN (GHANĪMAH & FAYʾ)
% ------------------------------------------------------------------------------
quelle(beuterecht_und_fay, sura_8_verse_41).
quelle(beuterecht_und_fay, sura_59_verse_7).

gebietet(G, khums_abgabe(K)) :-
    militaerbeute_erbeutet(G),
    berechne_fuenftel(G, K).

untersagt(V, privatisierung_fay) :-
    gewaltloses_staatsvermoegen_fay(V),
    monopolisiert_durch_reiche(V).

gebietet(staat, verteilung_fay_gemeinwohl(V)) :-
    gewaltloses_staatsvermoegen_fay(V).

teilmenge(j_al_muffaqqiruna_li_amwal_al_fay, j_al_mufsiduna_fi_l_ard).

% ------------------------------------------------------------------------------
% K-020: STRAFRECHT / DIEBSTAHL (SARIQAH)
% ------------------------------------------------------------------------------
quelle(strafrecht_sariqah, sura_5_verse_38_39).

gebietet(staat, strafe_sariqah(D)) :-
    ist_delikt(D, Taelter, Opfer),
    delikttyp(D, diebstahl),
    erreicht_nisab_schwellenwert(D).

gestattet(staat, erlass_nach_reue(Taelter)) :-
    bereut_vor_ergreifung(Taelter).

% ------------------------------------------------------------------------------
% K-021: STRAFRECHT / UNZUCHT (ZINĀ) UND VERLEUMDUNG (QADHF)
% ------------------------------------------------------------------------------
quelle(strafrecht_zina_qadhf, sura_24_verse_2_5).

gebietet(staat, strafe_zina(D)) :-
    ist_delikt(D, Taelter, Opfer),
    delikttyp(D, unzucht_zina),
    belegt_durch_vier_zeugen(D).

gebietet(staat, strafe_qadhf(D)) :-
    ist_delikt(D, Taelter, Opfer),
    delikttyp(D, verleumdung_qadhf),
    \+ belegt_durch_vier_zeugen(D).

% ------------------------------------------------------------------------------
% K-022: ERBRECHT (MIRĀTH - TEILE & QUOTEN)
% ------------------------------------------------------------------------------
quelle(erbrecht_mirath, sura_4_verse_11_12).
quelle(erbrecht_mirath, sura_4_verse_176).

gebietet(staat, verteilung_erbe(E)) :-
    todesfall(E),
    erfuellt_schulden_und_wasiyyah(E).

% ------------------------------------------------------------------------------
% K-023: VORMUNDSCHAFT & WAISENVERMÖGEN (YATĀMĀ)
% ------------------------------------------------------------------------------
quelle(waisenvermoegen_schutz, sura_4_verse_2_6).
quelle(waisenvermoegen_schutz, sura_17_verse_34).

untersagt(Vormund, zehrung_waisenvermoegen(W)) :-
    ist_vormund(Vormund, W),
    vermoegend(Vormund).

gebietet(Vormund, aushaendigung_vermoegen(W)) :-
    ist_vormund(Vormund, W),
    reife_erreicht(W).

% ------------------------------------------------------------------------------
% K-024: UNEHRLICHE ANEIGNUNG & KORRUPTION (BĀṬIL & RISHWAH)
% ------------------------------------------------------------------------------
quelle(vermoegensverbrauch_batil, sura_2_verse_188).
quelle(vermoegensverbrauch_batil, sura_4_verse_29).

untersagt(X, aneignung_fremden_vermoegens(V)) :-
    \+ einverstaendlicher_handel(V).

untersagt(X, bestechung_richter(R)) :-
    beabsichtigt_unrechtmaessigen_gewinn(X).

% ------------------------------------------------------------------------------
% K-025: GEBETS- UND VERKAUFSORDNUNG AM FREITAG (JUMUʿAH)
% ------------------------------------------------------------------------------
quelle(freitagsgebet_wirtschaft, sura_62_verse_9_10).

gebietet(X, eilen_zum_gedenken) :-
    ist_glaeubig(X),
    ruf_zum_gebet(freitag).

untersagt(X, vollzug_transaktion(T)) :-
    ist_glaeubig(X),
    taetigt_transaktion(X, T),
    ruf_zum_gebet(freitag).

gestattet(X, erwerbstaetigkeit) :-
    gebet_beendet(freitag).

% ------------------------------------------------------------------------------
% K-026: VERSAMMLUNGSORDNUNG & SOZIALE ETIKETTE (TAFASSUḤ)
% ------------------------------------------------------------------------------
quelle(versammlungsordnung, sura_58_verse_11).

gebietet(X, platzmachen_in_versammlung) :-
    in_versammlung(X),
    aufgefordert_zu_tafassuh(X).

gebietet(X, erheben_oder_aufruecken) :-
    in_versammlung(X),
    aufgefordert_zu_inshaz(X).

% ------------------------------------------------------------------------------
% K-027: SELBST- UND FAMILIENSCHUTZ (TAḤRĪM)
% ------------------------------------------------------------------------------
quelle(obhut_und_familie, sura_66_verse_6).

gebietet(X, selbst_und_familienschutz) :-
    ist_glaeubig(X),
    familienoberhaupt(X).

% ------------------------------------------------------------------------------
% K-028: KULTISCHE OBLIATIONEN: ZAKĀT & INFĀQ
% ------------------------------------------------------------------------------
quelle(zakat_und_infaq, sura_2_verse_267).
quelle(zakat_und_infaq, sura_9_verse_60).

gebietet(X, zakat_entrichten) :-
    ist_glaeubig(X),
    vermoegen_erreicht_nisab(X).

% ------------------------------------------------------------------------------
% K-029: KULTISCHE OBLIGATIONEN: HAJJ & ʿUMRAH
% ------------------------------------------------------------------------------
quelle(hajj_und_umrah, sura_2_verse_196_197).
quelle(hajj_und_umrah, sura_3_verse_97).

gebietet(X, hajj_vollziehen) :-
    ist_glaeubig(X),
    reisefaehig_und_vermoegend(X).

% ------------------------------------------------------------------------------
% K-030: SCHWERER BANDITENRAUB (ḤIRĀBAH)
% ------------------------------------------------------------------------------
quelle(strafrecht_hirabah, sura_5_verse_33_34).

gebietet(staat, strafe_hirabah(D)) :-
    ist_delikt(D, Taelter, Opfer),
    delikttyp(D, schwerer_raub_raubmord).

gestattet(staat, erlass_hudud_hirabah(Taelter)) :-
    bereut_vor_ergreifung(Taelter).
% ==============================================================================
% MUTTER-WISSENSBASIS: KORANISCHE NORMATIVITÄT & ETHIK
% BLOCK 2 / 4: KOMPLEXE K-031 BIS K-060
% Status: Vollständig, unverkürzt, harmonisiertes Vokabular (Blöcke 1-5)
% ==============================================================================

% ------------------------------------------------------------------------------
% K-031: EHEVORBEREITUNG, BRAUTGABE (MAHR) & NIKĀḤ
% ------------------------------------------------------------------------------
quelle(eheschliessung_mahr, sura_4_verse_4).
quelle(eheschliessung_mahr, sura_4_verse_24_25).

gebietet(M, entrichtung_mahr(F)) :-
    ist_ehepartner(M, F).

gestattet(M, verbrauch_mahr_anteil(F)) :-
    ist_ehepartner(M, F),
    freiwilliges_geschenk_von(F, M).

% ------------------------------------------------------------------------------
% K-032: EHESCHLIESSUNG MIT UNFREIEN / SKLAVISCHEN PERSONEN
% ------------------------------------------------------------------------------
quelle(ehe_mit_unfreien, sura_4_verse_25).
quelle(ehe_mit_unfreien, sura_24_verse_32).

gestattet(M, eheschliessung(F)) :-
    \+ vermoegend_fuer_freie_frau(M),
    ist_glaeubig(M),
    ist_glaeubig(F),
    erlaubnis_von_vormund(F).

% ------------------------------------------------------------------------------
% K-033: SCHWUR ZUR EHELICHEN ENTHALTSAMKEIT (ĪLĀʾ)
% ------------------------------------------------------------------------------
quelle(ehe_ila, sura_2_verse_226_227).

gebietet(M, entscheidung_ila(F)) :-
    schwurt_enthaltung(M, F),
    frist_vier_monate_abgelaufen.

gestattet(M, rueckkehr_zu_eheleben(F)) :-
    bereut_schwur(M),
    frist_vier_monate_nicht_ueberschritten.

% ------------------------------------------------------------------------------
% K-034: SCHWUR DER GLEICHSETZUNG (ẒIHĀR) & KAFFĀRAH
% ------------------------------------------------------------------------------
quelle(zihar_und_kaffarah, sura_58_verse_2_4).
quelle(zihar_und_kaffarah, sura_33_verse_4).

untersagt(M, intimitaet_ehepartner(F)) :-
    ausgesprochen_zihar(M, F),
    \+ erfuellt_kaffarah_zihar(M).

erfuellt_kaffarah_zihar(M) :- freikauf_sklavische_person(M).
erfuellt_kaffarah_zihar(M) :- \+ vermoegend_fuer_freikauf(M), fasten_monate_folge(M, 2).
erfuellt_kaffarah_zihar(M) :- \+ leistungfaehig_fasten(M), speisung_sechzig_beduerftige(M).

% ------------------------------------------------------------------------------
% K-035: EHEBRUCHSBESCHULDIGUNG UNTER EHELEUTEN (LIʿĀN)
% ------------------------------------------------------------------------------
quelle(ehebruch_lican, sura_24_verse_6_9).

gebietet(M, vollzug_lican_eidschwur(F)) :-
    beschuldigt_ehebruch(M, F),
    \+ bringt_vier_zeugen(M).

gestattet(F, abwendung_strafe_durch_eidschwur(M)) :-
    schwurt_vierfache_unschuld(F).

% ------------------------------------------------------------------------------
% K-036: STILLZEIT & AMMENVERTRAG (RIḌĀʿAH)
% ------------------------------------------------------------------------------
quelle(stillzeit_ridaah, sura_2_verse_233).
quelle(stillzeit_ridaah, sura_65_verse_6).

gebietet(F, stillen_kind(K)) :-
    ist_mutter(F, K),
    wunsch_vollstaendige_stillzeit(F).

gebietet(H, verpflegung_und_kleidung(F)) :-
    ist_vater(H, K),
    stillt_gemeinsames_kind(F, H).

gestattet(H, inanspruchnahme_amme(K)) :-
    einverstaendnis_eheleute(H, F).

% ------------------------------------------------------------------------------
% K-037: WARTEZEIT NACH TOD DES EHEMANNES (ʿIDDAT AL-WAFĀT)
% ------------------------------------------------------------------------------
quelle(iddat_al_wafat, sura_2_verse_234).
quelle(iddat_al_wafat, sura_2_verse_240).

gebietet(F, einzuhalten_iddat_wafat) :-
    ehemann_verstorben(F).

untersagt(F, wiederverheiratung) :-
    in_iddat_wafat_frist(F).

% ------------------------------------------------------------------------------
% K-038: VERLOBUNG UND HEIRATSANTRAG IN DER WARTEZEIT
% ------------------------------------------------------------------------------
quelle(verlobung_in_iddah, sura_2_verse_235).

gestattet(M, andeutung_heiratsabsicht(F)) :-
    in_iddah_frist(F).

untersagt(M, geheimes_eheversprechen(F)) :-
    in_iddah_frist(F).

untersagt(M, vollzug_eheschliessung(F)) :-
    in_iddah_frist(F).

% ------------------------------------------------------------------------------
% K-039: GÜTERTRENNUNG & ABFINDUNG BEI SCHEIDUNG VOR INTIMITÄT (MUTʿAH)
% ------------------------------------------------------------------------------
quelle(scheidung_vor_vollzug, sura_2_verse_236_237).

gebietet(H, entrichtung_mutcah_abfindung(F)) :-
    ist_geschieden(H, F),
    \+ intimitaet_vollzogen(H, F),
    \+ mahr_festgesetzt(H, F).

gebietet(H, entrichtung_halbes_mahr(F)) :-
    ist_geschieden(H, F),
    \+ intimitaet_vollzogen(H, F),
    mahr_festgesetzt(H, F).

% ------------------------------------------------------------------------------
% K-040: ADOPTION & AUFHEBUNG DER ZUFAILSVERWANDTSCHAFT (TABANNĪ)
% ------------------------------------------------------------------------------
quelle(tabanni_adoption, sura_33_verse_4_5).
quelle(tabanni_adoption, sura_33_verse_37).

gebietet(gesellschaft, benennung_nach_leiblichem_vater(Child)) :-
    ist_adoptivkind(Child).

untersagt(X, gleichsetzung_adoptivkind_mit_leiblichem_kind(Child)) :-
    ist_adoptivkind(Child).

% ------------------------------------------------------------------------------
% K-041: RECHT AUF PERSÖNLICHE PRIVATSPHÄRE & BETRETENSVERBOT (ISTIʾDHĀN)
% ------------------------------------------------------------------------------
quelle(privatsphaere_istidhan, sura_24_verse_27_29).
quelle(privatsphaere_istidhan, sura_24_verse_58_59).

untersagt(X, betreten_fremder_haeuser) :-
    \+ um_erlaubnis_gebeten(X),
    \+ bewohner_begruesst(X).

gebietet(X, umkehr_bei_weisung) :-
    aufgefordert_zu_umkehr(X).

% ------------------------------------------------------------------------------
% K-042: BLICKSTEUERUNG & ANSTANDSBESTIMMUNGEN (GHAḌḌ AL-BAṢAR)
% ------------------------------------------------------------------------------
quelle(ghadd_al_basar, sura_24_verse_30_31).

gebietet(X, senken_des_blickes) :-
    ist_glaeubig(X).

gebietet(X, wahrung_der_scham) :-
    ist_glaeubig(X).

untersagt(F, zeigen_von_schmuck_ausser_offenkundigem) :-
    ist_glaeubig(F),
    ist_frau(F).

% ------------------------------------------------------------------------------
% K-043: FREIKAUF VON UNFREIEN (MUKĀTABAH)
% ------------------------------------------------------------------------------
quelle(mukatabah_freikauf, sura_24_verse_33).

gebietet(Eigentuemer, gewaehrung_freikaufsvertrag(U)) :-
    ist_unfrei(U),
    verlangt_mukatabah(U),
    erkennbare_redlichkeit(U).

gebietet(X, unterstuetzung_mukatab(U)) :-
    ist_in_freikauf(U).

% ------------------------------------------------------------------------------
% K-044: VERBOT DER PROSTITUTION UND AUSBEUTUNG UNFREIER
% ------------------------------------------------------------------------------
quelle(verbot_prostitution, sura_24_verse_33).

untersagt(Eigentuemer, zwingen_zu_prostitution(U)) :-
    ist_unfrei(U),
    wunsch_nach_keuschheit(U).

% ------------------------------------------------------------------------------
% K-045: HÄUSLICHE PRIVATSPHÄRE IN DREI RUHEZEITEN
% ------------------------------------------------------------------------------
quelle(drei_ruhezeiten_privatsphaere, sura_24_verse_58_59).

gebietet(Person, einholen_erlaubnis) :-
    (ist_unfrei(Person) ; ist_minderjaehrig(Person)),
    in_drei_ruhezeiten.

% ------------------------------------------------------------------------------
% K-046: DISPENS FÜR ÄLTERE FRAUEN (QAWĀʿID MIN AN-NISĀʾ)
% ------------------------------------------------------------------------------
quelle(qawaid_min_an_nisa, sura_24_verse_60).

gestattet(F, ablegen_aeusserer_kleidung) :-
    ist_fortgeschrittenen_alters(F),
    \+ wunsch_nach_eheschliessung(F),
    \+ absicht_schmuckzurseitestellung(F).

% ------------------------------------------------------------------------------
% K-047: GEMEINSAME MAHLZEITEN & VERWANDTSCHAFTSTISCH
% ------------------------------------------------------------------------------
quelle(gemeinsame_mahlzeiten, sura_24_verse_61).

gestattet(X, einnahme_mahlzeit_in_verwandtenhaeusern) :-
    ist_glaeubig(X).

gestattet(X, mahlzeit_gemeinsam_oder_getrennt) :-
    ist_glaeubig(X).

% ------------------------------------------------------------------------------
% K-048: ORDNUNG VON STAATLICHEN & GEMEINSCHAFTLICHEN SITZUNGEN
% ------------------------------------------------------------------------------
quelle(gemeinschaftsversammlung, sura_24_verse_62_63).

untersagt(X, entfernen_aus_gemeinschaftsversammlung) :-
    ist_glaeubig(X),
    \+ um_erlaubnis_gebeten(X, leiter).

% ------------------------------------------------------------------------------
% K-049: RECHT DES SCHUTZSUCHENDEN (ISTIJĀRAH / ASYL)
% ------------------------------------------------------------------------------
quelle(istijarah_schutzrecht, sura_9_verse_6).

gebietet(staat, gewaehrung_schutz_und_geleit(Y)) :-
    sucht_schutz(Y),
    \+ ist_glaeubig(Y).

% ------------------------------------------------------------------------------
% K-050: STAATSVERTRÄGE UND BÜNDNISTREUE (ʿUHŪD)
% ------------------------------------------------------------------------------
quelle(vertragstreue_uhud, sura_9_verse_4).
quelle(vertragstreue_uhud, sura_9_verse_7).
quelle(vertragstreue_uhud, sura_16_verse_91).

gebietet(staat, erfuellung_staatsvertrag(V)) :-
    ist_staatsvertrag(V),
    \+ vertragsbruch_durch_partner(V).

% ------------------------------------------------------------------------------
% K-051: KRIEGSERKLÄRUNG BEI DROHENDEM VERTRAGSBRUCH (INBIDH)
% ------------------------------------------------------------------------------
quelle(inbidh_vertragsbruch, sura_8_verse_58).

gebietet(staat, loesung_vertrag_auf_gleicher_ebene(V)) :-
    befuerchtet_vertragsbruch(V).

untersagt(staat, angriff_ohne_kuendigung(V)) :-
    ist_staatsvertrag(V).

% ------------------------------------------------------------------------------
% K-052: VERBOT DES VERRATS BEI STRATEGISCHEN GÜTERN
% ------------------------------------------------------------------------------
quelle(schutz_strategischer_güter, sura_8_verse_27).

untersagt(X, verrat_an_staat_und_gemeinschaft) :-
    ist_glaeubig(X),
    anvertraut_strategische_güter(X).

% ------------------------------------------------------------------------------
% K-053: RÜSTUNG UND ABSCHRECKUNG ZUR FRIEDENSICHERUNG (IʿDĀD AL-QUWWAH)
% ------------------------------------------------------------------------------
quelle(ruestung_und_verteidigung, sura_8_verse_60).

gebietet(staat, bereithaltung_verteidigungsmittel) :-
    zweck_friedenssicherung_und_abschreckung.

% ------------------------------------------------------------------------------
% K-054: FRIEDENSANGEBOT UND KAPITULATION (SALM)
% ------------------------------------------------------------------------------
quelle(friedensangebot_salm, sura_8_verse_61).
quelle(friedensangebot_salm, sura_4_verse_90).

gebietet(staat, eingehen_auf_friedensangebot) :-
    neigt_zu_frieden(gegner).

% ------------------------------------------------------------------------------
% K-055: KRIEGSGEFANGENE UND LÖSEGELD / FREILASSUNG (MANNN WA FIDĀʾ)
% ------------------------------------------------------------------------------
quelle(kriegsgefangene_mann_fida, sura_47_verse_4).

gebietet(staat, entscheidung_gefangene(G)) :-
    ist_kriegsgefangener(G),
    (freilassung_ohne_entgelt(G) ; freilassung_gegen_loesegeld(G)).

% ------------------------------------------------------------------------------
% K-056: BEKÄMPFUNG VON RELIGIÖSER UNTERDRÜCKUNG (FITNAH)
% ------------------------------------------------------------------------------
quelle(bekaempfung_fitnah, sura_2_verse_193).
quelle(bekaempfung_fitnah, sura_8_verse_39).

gebietet(staat, einsatz_gegen_unterdrueckung) :-
    besteht_religioese_unterdrueckung.

% ------------------------------------------------------------------------------
% K-057: ASYL UND EXPULSION BEI RELIGIÖSER VERFOLGUNG (HIJRAH)
% ------------------------------------------------------------------------------
quelle(hijrah_aus_verfolgung, sura_4_verse_97_100).

gebietet(X, auswanderung_aus_unterdrueckung) :-
    ist_unterdrueckt(X),
    leistungsfaehig_zur_auswanderung(X).

% ------------------------------------------------------------------------------
% K-058: BEVOLLMÄCHTIGUNG UND VERTRETUNG IM PROZESS (WAKĀLAH)
% ------------------------------------------------------------------------------
quelle(vertretung_wakalah, sura_18_verse_19).

gestattet(X, bevollmachtigung_vertreter(Y)) :-
    ist_zivilgeschaeft.

% ------------------------------------------------------------------------------
% K-059: ERSETZUNG DES WASSERRITUALS BEI WASSERMANGEL (TAYAMMUM)
% ------------------------------------------------------------------------------
quelle(tayammum_dispens, sura_4_verse_43).
quelle(tayammum_dispens, sura_5_verse_6).

gestattet(X, vollzug_tayammum) :-
    ist_glaeubig(X),
    (krank(X) ; auf_reisen(X) ; \+ findet_wasser(X)).

% ------------------------------------------------------------------------------
% K-060: SILENTIUM UND ZUHÖREN BEI DER KORANREZITATION
% ------------------------------------------------------------------------------
quelle(zuhören_koran, sura_7_verse_204).

gebietet(X, zuhoeren_und_schweigen) :-
    wird_rezitiert_koran.
% ==============================================================================
% MUTTER-WISSENSBASIS: KORANISCHE NORMATIVITÄT & ETHIK
% BLOCK 3 / 4: KOMPLEXE K-061 BIS K-085
% Status: Vollständig, unverkürzt, harmonisiertes Vokabular (Blöcke 1-5)
% ==============================================================================

% ------------------------------------------------------------------------------
% K-061: KULTISCHE REINIGUNG (WUḌŪʾ & GHUSL)
% ------------------------------------------------------------------------------
quelle(reinigung_wudu_ghusl, sura_5_verse_6).
quelle(reinigung_wudu_ghusl, sura_4_verse_43).

gebietet(X, vollzug_wudu) :-
    ist_glaeubig(X),
    beabsichtigt_gebet(X),
    \+ im_zustand_der_reinheit(X).

gebietet(X, vollzug_ghusl) :-
    ist_glaeubig(X),
    im_zustand_der_janabah(X).

% ------------------------------------------------------------------------------
% K-062: RICHTUNG DER GEBETSORIENTIERUNG (QIBLAH)
% ------------------------------------------------------------------------------
quelle(gebetsrichtung_qiblah, sura_2_verse_144).
quelle(gebetsrichtung_qiblah, sura_2_verse_149_150).

gebietet(X, ausrichtung_kaaba) :-
    ist_glaeubig(X),
    vollzieht_gebet(X).

% ------------------------------------------------------------------------------
% K-063: GEBETSVERKÜRZUNG AUF REISEN (QAṢR)
% ------------------------------------------------------------------------------
quelle(gebetsverkuerzung_qasr, sura_4_verse_101).

gestattet(X, verkuerzung_gebet) :-
    ist_glaeubig(X),
    auf_reisen(X).

% ------------------------------------------------------------------------------
% K-064: GEBET BEI GEFAHR UND KAMPF (ṢALĀT AL-KHAWF)
% ------------------------------------------------------------------------------
quelle(gebet_bei_gefahr, sura_4_verse_102).

gebietet(X, gebet_im_schichtwechsel) :-
    ist_glaeubig(X),
    im_gefecht_oder_gefahr(X).

% ------------------------------------------------------------------------------
% K-065: VERTEILUNGSSCHLÜSSEL DER ZAKĀT-EMPFÄNGER
% ------------------------------------------------------------------------------
quelle(zakat_empfaenger, sura_9_verse_60).

gebietet(staat, zuteilung_zakat(E)) :-
    ist_zakat_vermoegen(E),
    (empfaenger_arm(E) ; empfaenger_beduerftig(E) ; verwalter_zakat(E) ; 
     herzengewinnung(E) ; freikauf_unfreier(E) ; verschuldet(E) ; 
     auf_dem_wege_gottes(E) ; reisender_in_not(E)).

% ------------------------------------------------------------------------------
% K-066: UNTERSTÜTZUNG DER BEDÜRFTIGEN UND INṢĀḐ (SADAQAH)
% ------------------------------------------------------------------------------
quelle(sadaqah_und_freiwilliges_opfer, sura_2_verse_271_274).
quelle(sadaqah_und_freiwilliges_opfer, sura_2_verse_261_265).

gestattet(X, geheime_sadaqah_gabe) :-
    ist_glaeubig(X).

untersagt(X, entwertung_sadaqah_durch_vorwurf) :-
    ist_glaeubig(X),
    uebergibt_sadaqah(X).

% ------------------------------------------------------------------------------
% K-067: OPFERTIERE ZUM HAJJ UND BUNDESSCHLACHTUNG (HADY)
% ------------------------------------------------------------------------------
quelle(hady_opfertiere, sura_5_verse_2).
quelle(hady_opfertiere, sura_5_verse_95_96).
quelle(hady_opfertiere, sura_22_verse_36_37).

gebietet(X, darbringung_hady) :-
    ist_glaeubig(X),
    vollzieht_hajj_tamattu(X).

% ------------------------------------------------------------------------------
% K-068: RITUELLE JAGD UND WEIHEZUSTAND (IḤRĀM)
% ------------------------------------------------------------------------------
quelle(jagdverbot_ihram, sura_5_verse_1).
quelle(jagdverbot_ihram, sura_5_verse_94_95).

untersagt(X, jagd_landtiere) :-
    im_zustand_ihram(X).

gestattet(X, jagd_meerestiere) :-
    im_zustand_ihram(X).

% ------------------------------------------------------------------------------
% K-069: SACHLICHE SÜHNELEISTUNG FÜR JAGDVERSTOSS IM IḤRĀM
% ------------------------------------------------------------------------------
quelle(kaffarah_jagdverstoss, sura_5_verse_95).

gebietet(X, kaffarah_jagdverstoss(T)) :-
    im_zustand_ihram(X),
    toetet_landtier(X, T).

erfuellt_kaffarah_jagd(X, T) :- opfertier_aequivalenz(X, T).
erfuellt_kaffarah_jagd(X, T) :- speisung_armenequivalent(X, T).
erfuellt_kaffarah_jagd(X, T) :- fasten_aequivalent(X, T).

% ------------------------------------------------------------------------------
% K-070: BESCHÜTZUNG DER HEILIGEN STÄTTEN (AL-MASJID AL-ḤARĀM)
% ------------------------------------------------------------------------------
quelle(schutz_heilige_staetten, sura_9_verse_28).

untersagt(X, betreten_heilige_staette) :-
    ist_gotzenanbeter(X).

% ------------------------------------------------------------------------------
% K-071: Drogen-, Alkohol- und Glücksspielverbot (Khamr & Maysir)
% ------------------------------------------------------------------------------
quelle(verbot_khamr_maysir, sura_5_verse_90_91).
quelle(verbot_khamr_maysir, sura_2_verse_219).

untersagt(X, konsum_khamr) :-
    ist_glaeubig(X).

untersagt(X, teilnahme_maysir) :-
    ist_glaeubig(X).

disjunkt(j_al_mushribuna_al_khamr, j_al_muta_arrifina_bi_l_falah).

% ------------------------------------------------------------------------------
% K-072: VERBOT DES VETTERNWIRTSCHAFT UND VERFÄLSCHUNG VON WAREN
% ------------------------------------------------------------------------------
quelle(fremdvermoegen_und_reue, sura_3_verse_75_76).

gebietet(X, rueckgabe_fremdvermoegen) :-
    anvertraut_vermoegen(X).

untersagt(X, einbehalt_fremdvermoegen_wegen_religion) :-
    anvertraut_vermoegen(X).

% ------------------------------------------------------------------------------
% K-073: VERBOT DES TESTAMENTSMISSBRAUCHS UND ERBENSCHAEDIGUNG
% ------------------------------------------------------------------------------
quelle(testamentsschutz_vor_harm, sura_4_verse_12).

untersagt(Erblasser, schaedigung_erben_durch_wasiyyah) :-
    fuer_mehr_als_drittel_testiert(Erblasser).

% ------------------------------------------------------------------------------
% K-074: SITTENWICHTIGKEIT VON KEUSCHHEITSBESCHULDIGUNGEN
% ------------------------------------------------------------------------------
quelle(schutz_keuschheit, sura_24_verse_23_25).

untersagt(X, verleumdung_ehrbarer_frauen) :-
    ist_glaeubig(X).

% ------------------------------------------------------------------------------
% K-075: VORSCHRIFTEN ZUM UMGANG MIT SPENDEN UND VORWÜRFEN
% ------------------------------------------------------------------------------
quelle(spendenetikette_und_heuchelei, sura_9_verse_79).

untersagt(X, spott_ueber_spendende) :-
    spottet_ueber_geringe_spende(X).

% ------------------------------------------------------------------------------
% K-076: DISPENS BEI NOTSTAND UND VERSTECKTEM ZZWANG (IKRĀH)
% ------------------------------------------------------------------------------
quelle(dispens_ikrah, sura_16_verse_106).

gestattet(X, aussage_unter_zwang) :-
    gezwungen_zu_aussage(X),
    herz_fest_im_glauben(X).

% ------------------------------------------------------------------------------
% K-077: ALLGEMEINES VERBOT DER SELBSTMORD- UND SELBSTSCHÄDIGUNG
% ------------------------------------------------------------------------------
quelle(verbot_selbstmord, sura_4_verse_29).
quelle(verbot_selbstmord, sura_2_verse_195).

untersagt(X, toetung_eigenes_leben) :-
    ist_glaeubig(X).

untersagt(X, werfen_in_den_eigenen_untergang) :-
    ist_glaeubig(X).

% ------------------------------------------------------------------------------
% K-078: BESCHÜTZUNG UND WÜRDE DER ELTERN (BIRR AL-WĀLIDAYN)
% ------------------------------------------------------------------------------
quelle(ehrung_der_eltern, sura_17_verse_23_24).
quelle(ehrung_der_eltern, sura_31_verse_14_15).

gebietet(X, guete_gegenueber_eltern) :-
    ist_glaeubig(X).

untersagt(X, kränkung_der_eltern) :-
    ist_glaeubig(X).

% ------------------------------------------------------------------------------
% K-079: RECHT AUF UNVERLETZLICHKEIT DES LEBENS (ḤURMAT AL-ḤAYĀT)
% ------------------------------------------------------------------------------
quelle(schutz_des_lebens, sura_5_verse_32).
quelle(schutz_des_lebens, sura_17_verse_33).

untersagt(X, toetung_seele_ohne_recht) :-
    ist_mensch(X).

% ------------------------------------------------------------------------------
% K-080: TÖTUNGSVERBOT AUS ARMUTSANGST (KINDERMORD)
% ------------------------------------------------------------------------------
quelle(verbot_kindestoetung, sura_17_verse_31).
quelle(verbot_kindestoetung, sura_6_verse_151).

untersagt(X, toetung_eigener_kinder) :-
    aus_furcht_vor_armut(X).

% ------------------------------------------------------------------------------
% K-081: VERBOT DES EHEBRUCHS (ZINĀ) ALS DELIKTSPRÄVENTION
% ------------------------------------------------------------------------------
quelle(praevention_zina, sura_17_verse_32).
quelle(praevention_zina, sura_25_verse_68).

untersagt(X, annaeherung_an_zina) :-
    ist_mensch(X).

% ------------------------------------------------------------------------------
% K-082: VERBOT DES HOCHMUTS UND STOLZEN AUFTRITTES (MARAḤ)
% ------------------------------------------------------------------------------
quelle(verbot_hochmut, sura_17_verse_37).
quelle(verbot_hochmut, sura_31_verse_18).

untersagt(X, stolzes_einthergehen) :-
    auf_erden(X).

% ------------------------------------------------------------------------------
% K-083: PRÜFUNG VON NACHRICHTEN UND GERÜCHTEN (TABAYYUN)
% ------------------------------------------------------------------------------
quelle(nachrichtenpruefung_tabayyun, sura_49_verse_6).
quelle(nachrichtenpruefung_tabayyun, sura_4_verse_83).

gebietet(X, verifizierung_nachricht(N)) :-
    ueberbringer_frevler(N),
    ist_glaeubig(X).

% ------------------------------------------------------------------------------
% K-084: SCHLICHTUNG ZWISCHEN MUSLIMISCHEN GRUPPEN (IṢLĀḤ)
% ------------------------------------------------------------------------------
quelle(schlichtung_unter_glaeubigen, sura_49_verse_9_10).

gebietet(gemeinschaft, schlichtung_zwischen_parteien(P1, P2)) :-
    im_konflikt(P1, P2).

gebietet(gemeinschaft, bekämpfung_aggressor(P1)) :-
    weigert_sich_schlichtung(P1).

% ------------------------------------------------------------------------------
% K-085: SPIONAGEVERBOT UND MUTMASSUNG (JAṢṢUṢ & ẒANN)
% ------------------------------------------------------------------------------
quelle(verbot_spionage_mutmassung, sura_49_verse_12).

untersagt(X, nachspionieren(Y)) :-
    ist_glaeubig(X),
    ist_glaeubig(Y).

untersagt(X, hegen_unbegruendeter_mutmassungen(Y)) :-
    ist_glaeubig(X),
    ist_glaeubig(Y).
% ==============================================================================
% MUTTER-WISSENSBASIS: KORANISCHE NORMATIVITÄT & ETHIK
% BLOCK 4 / 4: KOMPLEXE K-086 BIS K-108
% Status: Vollständig, unverkürzt, harmonisiertes Vokabular (Blöcke 1-5)
% ==============================================================================

% ------------------------------------------------------------------------------
% K-086: VERPFLICHTUNG ZUM RECHTSCHAFFENEN HANDELN UND GUTE WERKE (AʿMĀL ṢĀLIḤAH)
% ------------------------------------------------------------------------------
quelle(gute_werke_amaliyyah, sura_103_verse_1_3).
quelle(gute_werke_amaliyyah, sura_2_verse_82).

gebietet(X, verrichtung_guter_werke) :-
    ist_glaeubig(X).

gebietet(X, gegenseitiges_ermahnen_zur_wahrheit) :-
    ist_glaeubig(X).

gebietet(X, gegenseitiges_ermahnen_zur_geduld) :-
    ist_glaeubig(X).

teilmenge(j_al_amiluna_as_salihat, j_al_fauz_al_azim).

% ------------------------------------------------------------------------------
% K-087: VERBOT DER BEREICHERUNG AN WAISENGÜTERN (AKL MĀL AL-YATĪM)
% ------------------------------------------------------------------------------
quelle(schutz_waisenbesitz, sura_6_verse_152).
quelle(schutz_waisenbesitz, sura_4_verse_10).

untersagt(X, verbrauch_waisenvermoegen(W)) :-
    ist_vormund(X, W),
    \+ im_sinne_des_besten_nutzens(W).

disjunkt(j_al_akiluna_amwal_al_yatama_zulman, j_al_muttaquna_indallah).

% ------------------------------------------------------------------------------
% K-088: VERBOT VON FREVLERISCHEM FREVEL UND ÜBERMUT (BAGHY)
% ------------------------------------------------------------------------------
quelle(verbot_baghy, sura_16_verse_90).
quelle(verbot_baghy, sura_7_verse_33).

untersagt(X, begehung_baghy_uebermut) :-
    ist_mensch(X).

untersagt(X, begehung_fahsha_schandtat) :-
    ist_mensch(X).

% ------------------------------------------------------------------------------
% K-089: WAHRUNG VON TRAUTEN UND PFLEGE DES BUNDES (AMĀNĀT)
% ------------------------------------------------------------------------------
quelle(amānāt_erfuellung, sura_4_verse_58).
quelle(amānāt_erfuellung, sura_23_verse_8).

gebietet(X, aushaendigung_anvertrautes_gut(A)) :-
    ist_empfaenger_anvertrautes_gut(X, A).

gebietet(X, gerechtes_richten_zwischen_menschen) :-
    ist_richter_oder_leiter(X).

% ------------------------------------------------------------------------------
% K-090: WARNUNG VOR MEINEID UND EIDESBRUCH (YAMĪN GHAMŪS)
% ------------------------------------------------------------------------------
quelle(verbot_meineid, sura_16_verse_92_94).
quelle(verbot_meineid, sura_3_verse_77).

untersagt(X, nutzung_eid_als_betrugsmittel) :-
    ist_mensch(X).

disjunkt(j_al_muttakhidhuna_aymanahum_dakhalan, j_al_muttaqun).

% ------------------------------------------------------------------------------
% K-091: GEBOT DES RECHTEN MĀßES UND DER VERMÖGENSBALANCE (IQTIṢĀD)
% ------------------------------------------------------------------------------
quelle(maß_im_verbrauch, sura_17_verse_26_29).
quelle(maß_im_verbrauch, sura_25_verse_67).

untersagt(X, verschwendung_israf) :-
    ist_mensch(X).

untersagt(X, geiz_und_kargheit) :-
    ist_mensch(X).

gebietet(X, mittlere_ausgabenhaltung) :-
    ist_mensch(X).

% ------------------------------------------------------------------------------
% K-092: VERBOT DES TÖTENS AUS SCHAM ODER FURCHT VOR MANGEL
% ------------------------------------------------------------------------------
quelle(schutz_neugeborene, sura_81_verse_8_9).
quelle(schutz_neugeborene, sura_16_verse_58_59).

untersagt(X, lebendig_begraben_neugeborene) :-
    ist_mensch(X).

% ------------------------------------------------------------------------------
% K-093: VERPFLEGEN UND SPEISEN DES ARMEN UND GEFANGENEN (IṬʿĀM)
% ------------------------------------------------------------------------------
quelle(speisung_armenequivalent, sura_76_verse_8_9).
quelle(speisung_armenequivalent, sura_89_verse_17_18).

gebietet(X, speisung_beduerftiger_und_gefangener) :-
    ist_glaeubig(X),
    vermoegend(X).

teilmenge(j_al_mutimuna_ala_hubbihi, j_al_abrar).

% ------------------------------------------------------------------------------
% K-094: GEBOT DES MASSES BEI VERGELTUNG (LA TAYTAGHU)
% ------------------------------------------------------------------------------
quelle(mass_bei_strafe, sura_16_verse_126).
quelle(mass_bei_strafe, sura_42_verse_40).

gebietet(X, adäquate_gleiche_strafe) :-
    erleidet_unrecht(X),
    sucht_vergeltung(X).

gestattet(X, geduldiges_verzeihen) :-
    erleidet_unrecht(X).

% ------------------------------------------------------------------------------
% K-095: VERBOT DER KULTURELLEN ODER RELIGIÖSEN SCHMÄHUNG (SABB AL-ĀLIHAH)
% ------------------------------------------------------------------------------
quelle(verbot_religioese_schmaehung, sura_6_verse_108).

untersagt(X, schmaehung_fremder_gottheiten(G)) :-
    ist_glaeubig(X).

% ------------------------------------------------------------------------------
% K-096: DURCHSETZUNG DES FRIEDENS UND VERBOT DES ANGRIFFSKRIEGES
% ------------------------------------------------------------------------------
quelle(verbot_angriffskrieg, sura_2_verse_190).

untersagt(X, begehung_aggression_oder_uebertreitung) :-
    im_kampf(X).

% ------------------------------------------------------------------------------
% K-097: HILFELEISTUNG FÜR IN NOT GERATENE WANDERER (IBN AS-SABĪL)
% ------------------------------------------------------------------------------
quelle(unterstuetzung_reisende, sura_17_verse_26).
quelle(unterstuetzung_reisende, sura_30_verse_38).

gebietet(X, gewaehrung_anteil_fuer_reisende(R)) :-
    ist_reisender_in_not(R),
    vermoegend(X).

% ------------------------------------------------------------------------------
% K-098: VERBOT DER DEMÜTIGUNG BEI WOHLTÄTIGKEIT (MĀNN WA AḎĀ)
% ------------------------------------------------------------------------------
quelle(ethik_der_spende, sura_2_verse_262_264).

untersagt(X, entwertung_spende_durch_nachdenken_oder_kränkung) :-
    gibt_spende(X).

% ------------------------------------------------------------------------------
% K-099: WAHRUNG DES EIDES BEI RITUELLEN BÜNDNISSEN
% ------------------------------------------------------------------------------
quelle(bundeswahrung, sura_5_verse_1).
quelle(bundeswahrung, sura_17_verse_34).

gebietet(X, erfuellung_vertraege_und_buendnisse) :-
    ist_mensch(X),
    ist_vertragspartei(X).

% ------------------------------------------------------------------------------
% K-100: KULTISCHE ABFINDUNG BEI VERDORBENER RITUALHANDLUNG (FIDYAH)
% ------------------------------------------------------------------------------
quelle(fidyah_ersatzleistung, sura_2_verse_196).

gebietet(X, entrichtung_fidyah) :-
    hindernis_bei_hajj_oder_fasten(X).

% ------------------------------------------------------------------------------
% K-101: SCHUTZ DER KULTSTÄTTEN GEGEN ZERSTÖRUNG (MASĀJID)
% ------------------------------------------------------------------------------
quelle(schutz_der_gebetshaeuser, sura_2_verse_114).
quelle(schutz_der_gebetshaeuser, sura_22_verse_40).

untersagt(X, hinderung_am_gedenken_in_moscheen) :-
    ist_mensch(X).

untersagt(X, zerstoerung_von_gotteshäusern) :-
    ist_mensch(X).

% ------------------------------------------------------------------------------
% K-102: GEBOT DES ZENTRALEN ANDACHTS- UND RITUALSTANDORTES
% ------------------------------------------------------------------------------
quelle(andacht_in_gebetstaetten, sura_7_verse_31).

gebietet(X, anlegen_reiner_kleidung_zum_gebet) :-
    ist_glaeubig(X),
    sucht_gebetstaette(X).

% ------------------------------------------------------------------------------
% K-103: ABTRENNUNG UND SCHUTZ VON FRAUEN IN SONDERPHASEN (ḤAYḌ)
% ------------------------------------------------------------------------------
quelle(hygiene_hayd, sura_2_verse_222).

untersagt(M, intimitaet_waehrend_regelblutung(F)) :-
    ist_ehepartner(M, F),
    im_zustand_hayd(F).

gestattet(M, intimitaet_nach_reinigung(F)) :-
    ist_ehepartner(M, F),
    beendet_hayd_und_gereinigt(F).

% ------------------------------------------------------------------------------
% K-104: PFLEGE UND SCHUTZ DER VERWANDTSCHAFTSBANDE (ṢILAT AL-ARḤĀM)
% ------------------------------------------------------------------------------
quelle(verwandtschaftsbande_silah, sura_4_verse_1).
quelle(verwandtschaftsbande_silah, sura_47_verse_22_23).

gebietet(X, wahren_der_verwandtschaftsbande) :-
    ist_mensch(X).

untersagt(X, trennen_der_verwandtschaftsbande) :-
    ist_mensch(X).

% ------------------------------------------------------------------------------
% K-105: BEKÄMPFUNG DER ARROGANZ IM WISSEN UND BEHAUPTUNG OHNE EVIDENZ
% ------------------------------------------------------------------------------
quelle(evidenz_gebot, sura_17_verse_36).

untersagt(X, befolgung_ohne_wissen_und_evidenz) :-
    ist_mensch(X).

% ------------------------------------------------------------------------------
% K-106: WAHRMUNG DES ARMENRECHTS IM ERNTEERTRAG (ḤAQQ MAʿLŪM)
% ------------------------------------------------------------------------------
quelle(ernteabgabe_haqq, sura_6_verse_141).
quelle(ernteabgabe_haqq, sura_70_verse_24_25).

gebietet(X, entrichtung_armenrecht_am_erntetag) :-
    besitzt_landwirtschaftlichen_ertrag(X).

% ------------------------------------------------------------------------------
% K-107: MĀßHALTUNG BEI ZORN UND RÜCKSICHTSNAHME (KĀẒIMĪN AL-GHAYẒ)
% ------------------------------------------------------------------------------
quelle(zornbeherrschung, sura_3_verse_134).
quelle(zornbeherrschung, sura_42_verse_37).

gebietet(X, beherrschung_des_zorns) :-
    ist_glaeubig(X).

gestattet(X, vergebung_bei_zorn) :-
    ist_glaeubig(X).

teilmenge(j_al_kazimina_al_ghaiz, j_al_muhsinun).

% ------------------------------------------------------------------------------
% K-108: SCHLUSS-NORMATIVITÄT: GEBOT DES RECHTEN UND VERBOT DES BÖSEN (AL-AMR BI-L-MAʿRŪF)
% ------------------------------------------------------------------------------
quelle(al_amr_bi_l_maruf, sura_3_verse_104).
quelle(al_amr_bi_l_maruf, sura_3_verse_110).
quelle(al_amr_bi_l_maruf, sura_9_verse_71).

gebietet(X, gebieten_des_rechten) :-
    ist_glaeubig(X).

gebietet(X, verbieten_des_verwerflichen) :-
    ist_glaeubig(X).

teilmenge(j_al_amiruna_bi_l_maruf_wa_n_nahuna_an_il_munkar, j_al_muflihun).

% ==============================================================================
% ENDE DES GESAMTEN MUTTER-WISSENSBASIS EXPORTS (KANON K-001 BIS K-108)
% ==============================================================================