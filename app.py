# 1. Zuerst das Haupt-Regelwerk konsultieren
    prolog = Prolog()
    prolog.consult(pl_file)

    # 2. Dann die Fakten dynamisch per assertz im selben Modul-Kontext einspeisen
    for fkt in gesetzte_fakten:
        # Punkt am Ende für assertz entfernen
        fkt_clean = fkt.rstrip(".")
        try:
            prolog.assertz(fkt_clean)
        except Exception as e:
            pass

    # 3. Zielabfrage
    ziel_term = regel_data["ziel"]
    
    try:
        res = list(prolog.query(ziel_term))
        # PySWIP liefert bei Treffer ohne Variablen [{}] zurück (Länge > 0)
        if len(res) > 0:
            st.error(f"⛔ **MODUS PONENS ERFÜLLT:** `{ziel_term}` gilt als erwiesen.")
        else:
            st.info(f"ℹ️ **MODUS PONENS NICHT ERFÜLLT:** `{ziel_term}` lässt sich aus den gewählten Prämissen nicht ableiten.")
    except Exception as e:
        st.error(f"Fehler bei der Abfrage: {e}")
