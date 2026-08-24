import streamlit as st
from regeln import KANON

# Vollständige Zitat-Datenbank mit vollständigem Wortlaut aller einschlägigen Verse
VOLLTEXTE = {
    "K-001": (
        "„O ihr, die ihr glaubt, vorgeschrieben ist euch die Vergeltung für die Getöteten: "
        "der Freie für den Freien, der Sklave für den Sklaven und das weibliche Wesen für das weibliche Wesen. "
        "Wer aber von seinem Bruder etwas erlässt, so soll die Verfolgung in rechtlicher Weise und die Entrichtung an ihn auf gütige Art geschehen... "
        "Für euch gibt es in der Vergeltung Leben, o ihr Einsichtigen, auf dass ihr euch hegt.“ (Sure 2:178–179)\n\n"
        "„Und wir haben ihnen darin vorgeschrieben: Leben für Leben, Auge für Auge, Nase für Nase, Ohr für Ohr, Zahn für Zahn, "
        "und für Verletzungen die Wiedervergeltung...“ (Sure 5:45)\n\n"
        "„Und tötet nicht die Seele, die Gott verboten hat, außer mit Recht. Und wer unschuldig getötet wird, "
        "dessen Erben haben wir Gewalten gegeben; er soll aber im Töten nicht maßlos sein, denn er wird (von Gott) unterstützt.“ (Sure 17:33)"
    ),
    "K-002": "„Vorgeschrieben ist euch, wenn einem von euch der Tod vor Augen tritt, wenn er Vermögen hinterlässt, das Vermächtnis zugunsten der Eltern und der nächsten Angehörigen in rechtlicher Weise...“ (Sure 2:180–182; vgl. Sure 5:106–108)",
    "K-003": "„O ihr, die ihr glaubt, vorgeschrieben ist euch das Fasten, so wie es denjenigen vor euch vorgeschrieben worden ist, auf dass ihr gottesfürchtig werdet...“ (Sure 2:183–185, 187)",
    "K-004": "Diejenigen, die den Zins verschlingen, stehen nicht anders da als wie einer, den der Satan durch den Anfall umschlingt... (Sure 2:275–279; Sure 3:130; Sure 30:39)",
    "K-005": "„O ihr, die ihr glaubt, wenn ihr eine Schuld gegeneinander auf eine befristete Zeit eingeht, so schreibt sie auf...“ (Sure 2:282–283)",
    "K-006": "„Und heiratet nicht Frauen, die eure Väter geheiratet haben... Verboten sind euch eure Mütter, eure Töchter, eure Schwestern...“ (Sure 4:22–24; Sure 2:221; Sure 60:10)",
    "K-007": "„Und wenn ihr den Bruch zwischen den beiden befürchtet, so schickt einen Schiedsrichter von seiner Familie und einen Schiedsrichter von ihrer Familie...“ (Sure 4:34–35, 128)",
    "K-008": "„O ihr Frauen des Propheten, ihr seid nicht wie irgendwelche von den Frauen... Und seid nicht weich in der Rede, auf dass derjenige, in dessen Herzen Krankheit ist, Begehren hegt...“ (Sure 33:32–33)",
    "K-009": "„O Prophet, sprich zu deinen Gattinnen und deinen Töchtern und den Frauen der Gläubigen, sie sollen etwas von ihren Überhängen über sich ziehen...“ (Sure 33:59; Sure 24:31)",
    "K-010": "„O ihr, die ihr glaubt, seid Wahrer der Gerechtigkeit als Zeugen für Gott, und wenn es gegen euch selbst ist oder gegen die Eltern und die Nächsten...“ (Sure 4:135; Sure 5:8)",
    "K-011": "„...und deren Angelegenheit Beratung unter ihnen ist...“ (Sure 42:36–43; Sure 3:159)",
    "K-012": "„O ihr, die ihr glaubt, es sollen nicht Leute über andere Leute spotten... Und verleumdet einander nicht und bewerft einander nicht mit Schimpfnamen...“ (Sure 49:11–12)",
    "K-013": "„O ihr Menschen, wir haben euch aus männlichem und weiblichem Wesen erschaffen und euch zu Völkern und Stämmen gemacht, damit ihr einander kennenlernt...“ (Sure 49:13; Sure 30:22)",
    "K-014": "„Gott verbietet euch nicht bezüglich derer, die nicht gegen euch des Glaubens wegen gekämpft und euch nicht aus euren Häusern vertrieben haben, dass ihr ihnen Gutes tut und gerecht gegen sie seid...“ (Sure 60:8–9)",
    "K-015": "„Die sich scheidenden Frauen sollen drei Perioden lang abwarten... Und vertreibt sie nicht aus ihren Häusern, und sie sollen nicht ausziehen, es sei denn, sie bringen eine offenkundige Schändlichkeit vor...“ (Sure 2:228–232; Sure 65:1–7)"
}

# ------------------------------------------------------------------------------
# 1. ARCHITEKTUR & SEITEN-SETUP
# ------------------------------------------------------------------------------
st.set_page_config(page_title="Koranischer Normen-Apparat", layout="centered")

st.title("Koranischer Normen-Apparat")

st.markdown("---")

# ------------------------------------------------------------------------------
# 2. BENUTZEROBERFLÄCHE
# ------------------------------------------------------------------------------
sortierte_ids = sorted(KANON.keys())
auswahl_id = st.selectbox("Normenkomplex wählen:", sortierte_ids, format_func=lambda x: KANON[x]["titel"])
regel = KANON[auswahl_id]

# Offenbarungsquelle und vollständiger Wortlaut aller einschlägigen Verse
st.markdown(f"**Offenbarungsquelle:** {regel['quelle']}")
offenbarungs_text = VOLLTEXTE.get(auswahl_id, f"Vollständiger Offenbarungstext zu {regel['titel']} gemäß Korankorpus.")
st.markdown(f"> *{offenbarungs_text}*")

st.markdown("---")
st.subheader("Norm")
st.code(regel["ziel"], language="prolog")

st.subheader("Bedingungen zur Erfüllung der Norm")

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

# ------------------------------------------------------------------------------
# 3. AUSWERTUNG & WESSEL-KLASSIFIKATION
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
        st.markdown(f"**Prüfung:** Die Fragestellung ist **erfüllt**. `{ziel_term}` ist nachgewiesen.")
    else:
        gruende = "\n".join([f"- {p}" for p in protokoll])
        st.markdown(f"**Prüfung:** Die Fragestellung ist **nicht erfüllt**.\n\nFehlende Bedingungen:\n{gruende}")

    st.markdown("---")
    st.markdown(f"**Epistemischer Status:** `{status_text}`")
    st.markdown(f"*Befund:* {befund}")
