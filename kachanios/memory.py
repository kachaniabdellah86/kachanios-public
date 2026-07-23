from collections import defaultdict, deque

from .models import AgentContext


class InMemoryContextStore:
    """Privacy-safe context store used by the public edition.

    The private KachaniOS project uses richer local state. This public version
    deliberately keeps context ephemeral and never writes personal data to disk.
    """

    def __init__(self, max_messages: int = 8) -> None:
        self._messages: dict[str, deque[str]] = defaultdict(
            lambda: deque(maxlen=max_messages)
        )
        self._tasks: dict[str, list[str]] = defaultdict(list)

    def add_message(self, conversation_id: str, text: str) -> None:
        self._messages[conversation_id].append(text)

    def add_task(self, conversation_id: str, task: str) -> None:
        task = task.strip()
        if task and task not in self._tasks[conversation_id]:
            self._tasks[conversation_id].append(task)

    def get_context(self, conversation_id: str) -> AgentContext:
        return AgentContext(
            conversation_id=conversation_id,
            recent_messages=tuple(self._messages[conversation_id]),
            active_tasks=tuple(self._tasks[conversation_id]),
            user_preferences={"response_style": "clear and practical"},
        )
