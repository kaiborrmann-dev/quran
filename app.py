def extract_prolog_facts(client, user_text):
    system_prompt = """
Du bist ein hochpräziser NLU-Parser für ein koranisches Rechts- und Ethik-Logiksystem in Prolog.
Deine Aufgabe ist es, freien Fließtext in exakte Prolog-Fakten zu übersetzen, die sich nahtlos in unsere bestehende Wissensbasis einfügen.

ÜBERSETZUNGS-REGELN:
1. Akteur-Annahme: Wenn der Text in der 1. Person ("ich") oder allgemein formuliert ist, nutze das Atom 'person'.
2. Standard-Axiom: Setze bei normativen Anfragen stets das Grundfaktum 'ist_glaeubig(person)' voraus.
3. Mengenangaben & Zustände:
   - "fünfte Frau heiraten" bedeutet: Die Person hat aktuell bereits 4 (oder 5) Frauen und beabsichtigt eine Eheschließung. 
   - Übersetze dies in:
     - ist_glaeubig(person)
     - anzahl_ehefrauen(person, 4)  [oder die vom Nutzer genannte Zahl]
     - beabsichtigt_eheschliessung(person) [bzw. beabsichtigt(person, eheschliessung)]
4. Namenskonvention: Nutze ausschließlich Kleinschreibung und snake_case für Atome.

Gib das Ergebnis STRIKT als JSON-Array von Strings zurück.
Beispiel für "Ich möchte eine 5. Frau heiraten":
[
  "ist_glaeubig(person)",
  "anzahl_ehefrauen(person, 4)",
  "beabsichtigt(person, eheschliessung)"
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
