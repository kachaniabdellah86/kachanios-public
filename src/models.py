from dataclasses import dataclass
from typing import Literal

Domain = Literal[
    "studies",
    "productivity",
    "software_engineering",
    "finance",
    "general",
]


@dataclass(frozen=True)
class AgentRequest:
    message: str


@dataclass(frozen=True)
class AgentResult:
    domain: Domain
    response: str
