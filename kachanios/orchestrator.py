from .agents import AGENTS
from .memory import InMemoryContextStore
from .models import AgentOutput, FinalResponse, Message
from .router import TopicRouter


class FinalSpeaker:
    """Combines multiple domain outputs into one coherent response."""

    def compose(self, outputs: tuple[AgentOutput, ...]) -> str:
        primary = outputs[0]
        lines = [primary.summary, "", "Next actions:"]

        seen: set[str] = set()
        for output in outputs:
            for action in output.action_items:
                if action not in seen:
                    seen.add(action)
                    lines.append(f"- {action}")

        warnings = [warning for output in outputs for warning in output.warnings]
        if warnings:
            lines.extend(["", "Important:"])
            lines.extend(f"- {warning}" for warning in dict.fromkeys(warnings))

        return "\n".join(lines)


class KachaniOS:
    def __init__(
        self,
        router: TopicRouter | None = None,
        context_store: InMemoryContextStore | None = None,
        final_speaker: FinalSpeaker | None = None,
    ) -> None:
        self.router = router or TopicRouter()
        self.context_store = context_store or InMemoryContextStore()
        self.final_speaker = final_speaker or FinalSpeaker()

    def respond(self, message: Message) -> FinalResponse:
        cleaned = message.text.strip()
        if not cleaned:
            raise ValueError("message text must not be empty")

        route = self.router.route(message)
        context = self.context_store.get_context(message.conversation_id)

        domains = (route.primary_domain, *route.secondary_domains[:1])
        outputs = tuple(AGENTS[domain](message, context) for domain in domains)
        response_text = self.final_speaker.compose(outputs)

        self.context_store.add_message(message.conversation_id, cleaned)

        return FinalResponse(
            route=route,
            text=response_text,
            agent_outputs=outputs,
        )
