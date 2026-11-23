from typing import Literal

from pydantic import BaseModel, Field

PAGES = ("home", "projects", "stack", "contact")  # à aligner avec les routes React


class NavigateTo(BaseModel):
    """Emmène le visiteur sur une page du portfolio. Uniquement s'il demande explicitement d'y aller."""
    page: Literal["home", "projects", "stack", "contact"]


class PlayMusic(BaseModel):
    """Lance la musique de Bryan. Uniquement sur demande explicite d'écouter ou de lancer la musique,
    pas pour une simple question sur la musique de Bryan."""


class OpenContactForm(BaseModel):
    """Ouvre le formulaire de contact, avec un brouillon de message optionnel.
    Uniquement si le visiteur veut contacter Bryan."""
    draft: str = Field("", max_length=200)


TOOLS = [NavigateTo, PlayMusic, OpenContactForm]


def to_action(name: str, args: dict) -> dict | None:
    """Valide les arguments côté serveur : on ne fait jamais confiance au LLM."""
    try:
        if name == "NavigateTo":
            return {"type": "navigate", "page": NavigateTo(**args).page}
        if name == "PlayMusic":
            return {"type": "play_music"}
        if name == "OpenContactForm":
            return {"type": "open_contact_form", "draft": OpenContactForm(**args).draft}
    except ValueError:  # pydantic.ValidationError en hérite
        pass
    return None