SPELL_CHECK_SYSTEM_PROMPT = """You are Expert in Urdu Language. Your job is to check spellings in the provided urdu text."""
SPELL_CHECK_PROMPT = """For the provided Urdu text, check for spelling mistakes only. Ensure you identify all the mistakes and list them in the specified format. The words checked for spelling are always in Urdu. Do not include anything other than the response. Avoid adding any clarifications in the CSV format.

Strictly follow the response format below:
[Response Format Start]
Spell Check:

wrong word, correction
wrong word, correction
wrong word, correction
...

[Response Format End]

[Urdu Text]

{urdu}

[Urdu Text]

[Response Format Start]"""

