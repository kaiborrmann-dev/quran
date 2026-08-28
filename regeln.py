# regeln.py - Bereinigte Architektur nach deontischer Reduktion und Struktur-Typen

KANON_REGELN = {
    "K-001": {
        "titel": "Beispiel: Tötung und Vergeltung (Kisas)",
        # 1. Deontischer Vektor (Hier: Verbot der Tötung -> O(¬A))
        "deontik": "Verbot", # Entspricht O(¬A)
        "operator_formel": "O(¬A)",
        
        # 2. Logische Struktur (Hier: Exzeptiv mit Sperrtatbestand wie Verzeihung)
        "struktur_typ": "Exzeptiv",
        "beschreibung_struktur": "Grundregel mit Sperrtatbestand (z.B. formelle Verzeihung)",
        
        # Funktionale Prüfung im System
        "praemissen": ["vorsatz", "taetigkeit"],
        "sperren": ["verzeihung", "notwehr"]
    },
    
    "K-002": {
        "titel": "Beispiel: Verträge und Fristen",
        # 1. Deontischer Vektor (Hier: Gebot -> O(A))
        "deontik": "Gebot",
        "operator_formel": "O(A)",
        
        # 2. Logische Struktur (Hier: Kumulativ mit mehreren Tatbeständen)
        "struktur_typ": "Kumulativ",
        "beschreibung_struktur": "Mehrere Bedingungen müssen gleichzeitig vorliegen (A ^ B ^ C)",
        
        "praemissen": ["schriftform", "zeugen", "befristung"],
        "sperren": []
    },
    
    "K-003": {
        "titel": "Beispiel: Allgemeine Handlungsfreiheit / Erlaubnis",
        # 1. Deontischer Vektor (Hier: Erlaubnis -> ¬O(¬A))
        "deontik": "Erlaubnis",
        "operator_formel": "¬O(¬A)",
        
        # 2. Logische Struktur (Hier: Einfaches Konditional)
        "struktur_typ": "Einfach",
        "beschreibung_struktur": "Direkte Prämisse ohne komplexe Verzweigungen",
        
        "praemissen": ["grundvoraussetzung"],
        "sperren": []
    }
}

def evaluiere_norm(norm_id, sachverhalt_fakten, sachverhalt_sperren):
    """
    Evaluiert eine Norm basierend auf ihrem Struktur-Typ und ihrer Deontik,
    ohne den Umweg über den epistemischen Status.
    """
    norm = KANON_REGELN.get(norm_id)
    if not norm:
        return {"ergebnis": False, "grund": "Norm nicht gefunden"}
    
     struktur = norm["struktur_typ"]
    
    # 1. Prüfung bei Exzeptiven Normen (Prüfung auf Sperren)
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
                
    # 2. Prüfung der Prämissen nach Struktur-Typ
    if struktur == "Kumulativ":
        # Alle Prämissen müssen erfüllt sein (A ^ B ^ C)
        erfüllt = all(p in sachverhalt_fakten for p in norm["praemissen"])
    elif struktur in ["Einfach", "Exzeptiv"]:
        # Mindestens die Kernprämisse(n) müssen greifen
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
