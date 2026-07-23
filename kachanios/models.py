from dataclasses import dataclass, field
from typing import Literal

Domain = Literal[
    "studies",
    "productivity",
    "software_engineering",
    "finance",
    "health_habits",
    "relationships",
    "general",
]


@dataclass(frozen=True)
class Message:
    text: str
    conversation_id: str = "demo"
    metadata: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class RouteDecision:
    primary_domain: Domain
    secondary_domains: tuple[Domain, ...] = ()
    confidence: float = 0.0
    reasons: tuple[str, ...] = ()


@dataclass(frozen=True)
class AgentContext:
    conversation_id: str
    recent_messages: tuple[str, ...] = ()
    active_tasks: tuple[str, ...] = ()
    user_preferences: dict[str, str] = field(default_factory=dict)


@dataclass(frozen=True)
class AgentOutput:
    domain: Domain
    summary: str
    action_items: tuple[str, ...] = ()
    warnings: tuple[str, ...] = ()


@dataclass(frozen=True)
class FinalResponse:
    route: RouteDecision
    text: str
    agent_outputs: tuple[AgentOutput, ...]
