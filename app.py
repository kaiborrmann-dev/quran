def extract_prolog_facts(client, user_text):
    system_prompt = """
Du bist ein NLU-Parser für ein koranisches Logiksystem in SWI-Prolog.
Übersetze Freitext streng in einstellige und zweistellige Prädikate über den Akteuren 'zaid' (Subjekt X) und 'amr' (Objekt/Partner Y).

REGELN FÜR DIE ABBILDUNG:
1. Subjekt X: 'zaid' (bei "ich", anonymen Anfragen oder explizit Zaid).
2. Objekt/Partner Y: 'amr'.
3. Standard-Axiom: Setze stets 'ist_glaeubig(zaid)'.
4. Handlungen & Zustände als Prädikate für X:
   - "fünfte Frau heiraten" -> 
     ist_glaeubig(zaid)
     anzahl_ehefrauen(zaid, 4)
     beabsichtigt_eheschliessung(zaid)

Gib STRIKT ein JSON-Array von Strings zurück:
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
        st.error(f"Fehler bei NLU: {e}")
        return []
