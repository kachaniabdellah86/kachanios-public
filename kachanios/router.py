from collections import defaultdict

from .models import Domain, Message, RouteDecision

DOMAIN_SIGNALS: dict[Domain, tuple[str, ...]] = {
    "studies": (
        "study", "exam", "revision", "course", "sql", "ccna", "uml",
        "étude", "examen", "révision", "cours", "قراية", "امتحان",
    ),
    "productivity": (
        "plan", "schedule", "organize", "focus", "task", "routine",
        "planning", "organisation", "concentration", "نظم", "برنامج",
    ),
    "software_engineering": (
        "python", "code", "bug", "api", "database", "react", "next.js",
        "typescript", "debug", "supabase", "prisma", "github",
    ),
    "finance": (
        "money", "budget", "income", "revenue", "business", "save",
        "argent", "revenu", "budget", "فلوس", "دخل", "مشروع",
    ),
    "health_habits": (
        "gym", "workout", "sleep", "nicotine", "smoking", "habit",
        "santé", "sport", "sommeil", "تدخين", "صحة", "رياضة",
    ),
    "relationships": (
        "relationship", "breakup", "friend", "message", "dating",
        "relation", "rupture", "amour", "صاحبي", "حبيبة", "علاقة",
    ),
    "general": (),
}


class TopicRouter:
    def route(self, message: Message) -> RouteDecision:
        text = message.text.casefold()
        scores: dict[Domain, int] = defaultdict(int)
        reasons: dict[Domain, list[str]] = defaultdict(list)

        for domain, signals in DOMAIN_SIGNALS.items():
            for signal in signals:
                if signal in text:
                    scores[domain] += 1
                    reasons[domain].append(signal)

        ranked = sorted(
            ((domain, score) for domain, score in scores.items() if score > 0),
            key=lambda item: (-item[1], item[0]),
        )

        if not ranked:
            return RouteDecision(
                primary_domain="general",
                confidence=0.35,
                reasons=("no strong domain signal",),
            )

        primary, primary_score = ranked[0]
        secondary = tuple(domain for domain, _ in ranked[1:3])
        total = sum(score for _, score in ranked)
        confidence = min(0.98, 0.55 + (primary_score / max(total, 1)) * 0.4)

        return RouteDecision(
            primary_domain=primary,
            secondary_domains=secondary,
            confidence=round(confidence, 2),
            reasons=tuple(reasons[primary][:5]),
        )
