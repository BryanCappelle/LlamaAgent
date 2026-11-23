import logging

import groq
from langchain_groq import ChatGroq

from app.llm.models import MODELS
from app.tools.schemas import TOOLS

log = logging.getLogger(__name__)


def _build():
    runnables = [
        ChatGroq(
            model=m.name,
            max_tokens=m.max_tokens,
            temperature=m.temperature,
            api_key=m.provider.api_key,
        ).bind_tools(TOOLS)
        for m in MODELS
    ]
    return runnables[0].with_fallbacks(
        runnables[1:],
        exceptions_to_handle=(groq.APIStatusError, groq.APIConnectionError),
    )


llm = _build()


def generate_with_fallback(messages: list[dict]):
    """Renvoie un AIMessage : .content (texte) et .tool_calls (liste de dicts name/args/id)."""
    try:
        return llm.invoke(messages)
    except Exception as e:
        raise RuntimeError("Tous les modèles ont échoué") from e