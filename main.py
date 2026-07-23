from src.models import AgentRequest
from src.orchestrator import process_request


def main() -> None:
    print("KachaniOS Public - privacy-safe architecture demo")
    message = input("Your message: ").strip()

    if not message:
        print("Please enter a non-empty message.")
        return

    result = process_request(AgentRequest(message=message))
    print(f"Domain: {result.domain}")
    print(f"Response: {result.response}")


if __name__ == "__main__":
    main()
