MAX_MESSAGE = 300
MAX_HISTORY = 10
MAX_HISTORY_CONTENT = 500


def parse_payload(data):
    """Renvoie (message, history) ou lève ValueError si la requête est invalide."""
    if not isinstance(data, dict):
        raise ValueError("JSON attendu")

    message = data.get("message")
    if not isinstance(message, str) or not message.strip() or len(message) > MAX_MESSAGE:
        raise ValueError("message invalide")

    history = data.get("history", [])
    if not isinstance(history, list) or len(history) > MAX_HISTORY:
        raise ValueError("history invalide")

    clean = []
    for item in history:
        if not isinstance(item, dict):
            raise ValueError("history invalide")
        role, content = item.get("role"), item.get("content")
        if role not in ("user", "assistant") or not isinstance(content, str) or len(content) > MAX_HISTORY_CONTENT:
            raise ValueError("history invalide")
        clean.append({"role": role, "content": content})

    return message.strip(), clean
