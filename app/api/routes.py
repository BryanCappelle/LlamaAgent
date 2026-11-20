import logging

from flask import Blueprint, jsonify, request

from app.api.validation import parse_payload
from app.services.chat import answer

log = logging.getLogger(__name__)
api = Blueprint("api", __name__)

SLEEP_REPLY = "Une éclipse passe devant mes étoiles... écris plutôt à Bryan via le formulaire !"


@api.get("/health")
def health():
    return jsonify(status="ok")


@api.post("/chat")
def chat():
    try:
        message, history = parse_payload(request.get_json(silent=True))
    except ValueError as e:
        return jsonify(error=str(e)), 400

    try:
        result = answer(message, history)
    except Exception:
        log.exception("Erreur dans l'agent")
        return jsonify(reply=SLEEP_REPLY, actions=[{"type": "open_contact_form", "draft": ""}])

    return jsonify(reply=result["reply"], actions=result.get("actions", []))


@api.app_errorhandler(413)
def too_large(_):
    return jsonify(error="requête trop volumineuse"), 413
