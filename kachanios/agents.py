from collections.abc import Callable

from .models import AgentContext, AgentOutput, Domain, Message

AgentHandler = Callable[[Message, AgentContext], AgentOutput]


def studies_agent(message: Message, context: AgentContext) -> AgentOutput:
    return AgentOutput(
        domain="studies",
        summary="Turn the request into a focused study objective and a short execution sequence.",
        action_items=(
            "Define the exact topic and expected outcome.",
            "Work through one explanation and one practical exercise.",
            "Finish with a short recall test without notes.",
        ),
    )


def productivity_agent(message: Message, context: AgentContext) -> AgentOutput:
    return AgentOutput(
        domain="productivity",
        summary="Reduce the request to one priority, one time block, and one measurable finish line.",
        action_items=(
            "Choose the single highest-value task.",
            "Reserve a distraction-free 45-minute block.",
            "Record the next action before stopping.",
        ),
    )


def software_agent(message: Message, context: AgentContext) -> AgentOutput:
    return AgentOutput(
        domain="software_engineering",
        summary="Use a reproducible debugging workflow before changing implementation details.",
        action_items=(
            "Reproduce the issue with the smallest possible input.",
            "Inspect logs, inputs, outputs, and boundary conditions.",
            "Apply one change and verify it with a focused test.",
        ),
    )


def finance_agent(message: Message, context: AgentContext) -> AgentOutput:
    return AgentOutput(
        domain="finance",
        summary="Evaluate the request through speed to revenue, cost, risk, and proof of demand.",
        action_items=(
            "State the offer and the person who would pay for it.",
            "Choose a zero-cost validation method.",
            "Track outreach, conversion, and revenue separately.",
        ),
        warnings=("This module provides planning support, not financial advice.",),
    )


def health_agent(message: Message, context: AgentContext) -> AgentOutput:
    return AgentOutput(
        domain="health_habits",
        summary="Focus on a safe, sustainable next action and avoid pretending to diagnose medical conditions.",
        action_items=(
            "Identify the immediate trigger or obstacle.",
            "Choose one low-risk action for today.",
            "Escalate to a qualified professional when symptoms or risk are significant.",
        ),
        warnings=("The public demo does not provide diagnosis or emergency care.",),
    )


def relationships_agent(message: Message, context: AgentContext) -> AgentOutput:
    return AgentOutput(
        domain="relationships",
        summary="Separate facts, interpretations, boundaries, and the next respectful action.",
        action_items=(
            "Describe what happened without assumptions.",
            "Identify the boundary or outcome you need.",
            "Choose a calm action that protects dignity and clarity.",
        ),
    )


def general_agent(message: Message, context: AgentContext) -> AgentOutput:
    return AgentOutput(
        domain="general",
        summary="Clarify the goal and produce a direct next step.",
        action_items=("State the desired outcome in one sentence.",),
    )


AGENTS: dict[Domain, AgentHandler] = {
    "studies": studies_agent,
    "productivity": productivity_agent,
    "software_engineering": software_agent,
    "finance": finance_agent,
    "health_habits": health_agent,
    "relationships": relationships_agent,
    "general": general_agent,
}
