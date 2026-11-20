import os
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Provider:
    name: str
    base_url: str
    api_key_env: str

    @property
    def api_key(self) -> str:
        return os.environ[self.api_key_env]


@dataclass(frozen=True)
class LanguageModel:
    name: str
    provider: Provider
    max_tokens: int = 150
    temperature: float = 0.7
    extra: dict = field(default_factory=dict)


GROQ = Provider(
    name="groq",
    base_url="https://api.groq.com/openai/v1",
    api_key_env="GROQ_API_KEY",
)

MODELS = [
    LanguageModel("qwen/qwen3.8-27b", GROQ, max_tokens=150),
    LanguageModel("openai/gpt-oss-120b", GROQ, max_tokens=150),
]
