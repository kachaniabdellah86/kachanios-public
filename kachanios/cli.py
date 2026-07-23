from .models import Message
from .orchestrator import KachaniOS


def main() -> None:
    assistant = KachaniOS()
    print("KachaniOS Public - privacy-safe multi-agent edition")
    print("Type 'exit' to stop.\n")

    while True:
        text = input("You: ").strip()
        if text.casefold() in {"exit", "quit"}:
            break
        if not text:
            continue

        result = assistant.respond(Message(text=text, conversation_id="cli-demo"))
        print(f"\nRoute: {result.route.primary_domain} ({result.route.confidence:.0%})")
        print(result.text)
        print()


if __name__ == "__main__":
    main()
