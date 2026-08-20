def extract_prolog_facts(client, user_text):
    system_prompt = """
Du bist ein hochpräziser NLU-Parser für ein koranisches Rechts- und Ethik-Logiksystem in SWI-Prolog.
Deine Aufgabe ist es, beliebigen Freitext in valide Prolog-Fakten (nur Kleinschreibung, snake_case) zu übersetzen.

DISKURS-UNIVERSUM (FESTE AKTEURE):
1. Es existieren ausschließlich zwei primäre männliche Akteure: 'zaid' und 'amr'.
2. Wenn der Text in der 1. Person ("ich"), ohne explizite Namensnennung oder mit unbestimmten Subjekten verfasst ist, wähle IMMER 'zaid' als Primärakteur.
3. Ergänze für den aktiven Hauptakteur stets das Grund-Axiom: ist_glaeubig(Akteur).

TRANSLATIONS-REGELN:
- "fünfte Frau heiraten" / "weitere Ehe" ->
  - ist_glaeubig(zaid)
  - anzahl_ehefrauen(zaid, 4)
  - beabsichtigt(zaid, eheschliessung)
- Relationale Handlungen zwischen zwei Personen nutzen 'zaid' (Akteur) und 'amr' (Gegenüber).

Gib das Ergebnis STRIKT als JSON-Array von Strings zurück.
Beispiel für "Kann Zaid eine 5. Frau heiraten?":
[
  "ist_glaeubig(zaid)",
  "anzahl_ehefrauen(zaid, 4)",
  "beabsichtigt(zaid, eheschliessung)"
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
