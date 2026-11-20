from app.llm import generate_with_fallback

messages = [
    {"role": "system", "content": "Tu es un llama sympathique. Réponds en 2 phrases."},
    {"role": "user", "content": "Qui es-tu ?"},
]

print(generate_with_fallback(messages))