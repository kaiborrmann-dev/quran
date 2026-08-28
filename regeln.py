# regeln.py - Bereinigte Architektur nach deontischer Reduktion und Struktur-Typen

KANON_REGELN = {
    "K-001": {
        "titel": "Beispiel: Tötung und Vergeltung (Kisas)",
        "deontik": "Verbot",
        "operator_formel": "O(¬A)",
        "struktur_typ": "Exzeptiv",
        "beschreibung_struktur": "Grundregel mit Sperrtatbestand (z.B. formelle Verzeihung)",
        "praemissen": ["vorsatz", "taetigkeit"],
        "sperren": ["verzeihung", "notwehr"],
        "quelle": "Sure 2:178",
        "text": "O ihr, die ihr glaubt, vorgeschrieben ist euch die Vergeltung für die Getöteten... (Sure 2:178)"
    },
    "K-002": {
        "titel": "Beispiel: Verträge und Fristen",
        "deontik": "Gebot",
        "operator_formel": "O(A)",
        "struktur_typ": "Kumulativ",
        "beschreibung_struktur": "Mehrere Bedingungen müssen gleichzeitig vorliegen (A ^ B ^ C)",
        "praemissen": ["schriftform", "zeugen", "befristung"],
        "sperren": [],
        "quelle": "Sure 2:282",
        "text": "Wenn ihr eine Schuld aufeinander nehmt auf eine bestimmte Frist, so schreibt sie auf... (Sure 2:282)"
    },
    "K-003": {
        "titel": "Beispiel: Allgemeine Handlungsfreiheit / Erlaubnis",
        "deontik": "Erlaubnis",
        "operator_formel": "¬O(¬A)",
        "struktur_typ": "Einfach",
        "beschreibung_struktur": "Direkte Prämisse ohne komplexe Verzweigungen",
        "praemissen": ["grundvoraussetzung"],
        "sperren": [],
        "quelle": "Sure 2:29",
        "text": "Er ist es, der für euch alles, was auf der Erde ist, erschaffen hat... (Sure 2:29)"
    }
}

# Alias für den Import in Streamlit
KANON = KANON_REGELN

def evaluiere_norm(norm_id, sachverhalt_fakten, sachverhalt_sperren):
    norm = KANON_REGELN.get(norm_id)
    if not norm:
        return {"ergebnis": False, "grund": "Norm nicht gefunden"}
    
    struktur = norm["struktur_typ"]
    
    if struktur == "Exzeptiv":
        for sperre in norm["sperren"]:
            if sperre in sachverhalt_sperren:
                return {
                    "norm": norm_id,
                    "deontik": norm["deontik"],
                    "struktur": struktur,
                    "ergebnis": False,
                    "status": "Blockiert durch Sperrtatbestand"
                }
                
    if struktur == "Kumulativ":
        erfüllt = all(p in sachverhalt_fakten for p in norm["praemissen"])
    elif struktur in ["Einfach", "Exzeptiv"]:
        erfüllt = all(p in sachverhalt_fakten for p in norm["praemissen"]) if norm["praemissen"] else True
    else:
        erfüllt = False
        
    return {
        "norm": norm_id,
        "deontik": norm["deontik"],
        "struktur": struktur,
        "ergebnis": erfüllt,
        "status": "Norm greift (Aktiv)" if erfüllt else "Voraussetzungen nicht erfüllt"
    }
