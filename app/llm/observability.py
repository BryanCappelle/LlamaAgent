import functools
import logging
import os
import time

log = logging.getLogger("llm.usage")

# Cumul sur la durée du process (utile pour résumer une suite de tests)
TOTALS = {"calls": 0, "input": 0, "output": 0, "total": 0}


def _cut(text: str, limit: int) -> str:
    text = " ".join(str(text).split())
    return text if len(text) <= limit else text[:limit] + "…"


def _usage(msg) -> dict:
    """Lit les tokens dans usage_metadata, sinon dans response_metadata (format Groq)."""
    meta = getattr(msg, "usage_metadata", None) or {}
    if not meta:
        raw = (getattr(msg, "response_metadata", None) or {}).get("token_usage", {})
        meta = {
            "input_tokens": raw.get("prompt_tokens", 0),
            "output_tokens": raw.get("completion_tokens", 0),
            "total_tokens": raw.get("total_tokens", 0),
        }
    return meta


def log_tokens(func=None, *, max_chars: int = 300):
    """Journalise tokens, latence et modèle de chaque appel LLM.
    Le contenu des messages n'est affiché que si LLM_LOG_CONTENT=1."""

    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(messages, *args, **kwargs):
            show_content = os.environ.get("LLM_LOG_CONTENT") == "1"
            start = time.perf_counter()
            try:
                msg = fn(messages, *args, **kwargs)
            except Exception:
                log.warning("LLM en échec après %.1fs", time.perf_counter() - start)
                raise
            elapsed = time.perf_counter() - start

            usage = _usage(msg)
            tin = usage.get("input_tokens", 0)
            tout = usage.get("output_tokens", 0)
            ttotal = usage.get("total_tokens", tin + tout)
            model = (getattr(msg, "response_metadata", None) or {}).get("model_name", "?")

            TOTALS["calls"] += 1
            TOTALS["input"] += tin
            TOTALS["output"] += tout
            TOTALS["total"] += ttotal

            log.info("[%s] %.1fs | entrée=%s sortie=%s total=%s tokens", model, elapsed, tin, tout, ttotal)

            if show_content:
                for m in messages:
                    log.info("  ► %s : %s", m["role"], _cut(m["content"], max_chars))
                log.info("  ◄ réponse : %s", _cut(msg.content or "(vide)", max_chars))
                for tc in getattr(msg, "tool_calls", []):
                    log.info("  ◄ outil : %s(%s)", tc["name"], tc["args"])
            return msg

        return wrapper

    return decorator(func) if func else decorator