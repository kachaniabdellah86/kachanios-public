from src.models import Domain

DOMAIN_KEYWORDS: dict[Domain, tuple[str, ...]] = {
    "studies": ("study", "exam", "revision", "course", "sql", "ccna"),
    "productivity": ("plan", "schedule", "organize", "focus", "task"),
    "software_engineering": ("python", "code", "bug", "api", "database", "react"),
    "finance": ("money", "budget", "income", "revenue", "save"),
    "general": (),
}


def route_message(message: str) -> Domain:
    normalized = message.casefold()

    for domain, keywords in DOMAIN_KEYWORDS.items():
        if domain == "general":
            continue
        if any(keyword in normalized for keyword in keywords):
            return domain

    return "general"
