import logging

import groq
from groq import Groq

from app.llm.models import MODELS, LanguageModel

log = logging.getLogger(__name__)


def generate(model: LanguageModel, messages: list[dict]) -> str:
    client = Groq(api_key=model.provider.api_key)
    response = client.chat.completions.create(
        model=model.name,
        messages=messages,
        max_tokens=model.max_tokens,
        temperature=model.temperature,
        **model.extra,
    )
    return response.choices[0].message.content


def generate_with_fallback(messages: list[dict]) -> str:
    last_error = None
    for model in MODELS:
        try:
            return generate(model, messages)
        except (
            groq.RateLimitError,
            groq.NotFoundError,
            groq.APIConnectionError,
            groq.APIStatusError,
        ) as e:
            log.warning("Modèle %s en échec : %s", model.name, e)
            last_error = e
    raise RuntimeError("Tous les modèles ont échoué") from last_error
