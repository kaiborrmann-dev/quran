def extract_prolog_facts(client, user_text):
    system_prompt = """
Du bist ein NLU-Parser für ein koranisches Rechts- und Ethik-Logiksystem in SWI-Prolog.
Deine Aufgabe ist es, beliebigen Freitext in eine Liste korrekter Prolog-Fakten (nur Kleinschreibung, snake_case) zu übersetzen.

EXTRAKTIONS-REGELN:
1. Akteur-Erkennung:
   - Identifiziere genannte Personen (z.B. zaid, amina). Falls keine Person genannt ist (z.B. "ich"), nutze das Atom 'person'.
2. Grund-Axiom:
   - Ergänze für den primären Akteur stets das Faktum: ist_glaeubig(Akteur).
3. Mengen & Absichten (z.B. Polygamie / Eherecht):
   - "fünfte Frau heiraten" -> Der Akteur hat bereits 4 Frauen und beabsichtigt eine Eheschließung.
   - Generiere: anzahl_ehefrauen(Akteur, 4) und beabsichtigt_eheschliessung(Akteur) [oder beabsichtigt(Akteur, eheschliessung)].
4. Transaktionen & Sonstiges:
   - Übersetze Handlungen direkt in Prädikate (z.B. in_iddah_frist(Frau, Mann), beinhaltet_riba(TransaktionId)).

Gib das Ergebnis STRIKT als JSON-Array von Strings zurück.
Beispiel für "kann Zaid eine fünfte Frau heiraten?":
[
  "ist_glaeubig(zaid)",
  "anzahl_ehefrauen(zaid, 4)",
  "beabsichtigt_eheschliessung(zaid)"
]
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_text}
            ],
            response_format={"type": "json_object"},
            temperature=0.0
        )
        
        content = response.choices[0].message.content
        parsed = json.loads(content)
        
        if isinstance(parsed, dict):
            for key in parsed:
                if isinstance(parsed[key], list):
                    return parsed[key]
            return []
        elif isinstance(parsed, list):
            return parsed
        return []
        
    except Exception as e:
        st.error(f"Fehler bei der NLU-Anfrage: {e}")
        return []
