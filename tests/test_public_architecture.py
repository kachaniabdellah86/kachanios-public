import unittest

from kachanios.models import Message
from kachanios.orchestrator import KachaniOS
from kachanios.router import TopicRouter


class PublicArchitectureTests(unittest.TestCase):
    def test_routes_multilingual_study_request(self) -> None:
        decision = TopicRouter().route(Message("Je dois réviser SQL pour mon examen"))
        self.assertEqual(decision.primary_domain, "studies")

    def test_routes_software_request(self) -> None:
        decision = TopicRouter().route(Message("Debug my Python API and database bug"))
        self.assertEqual(decision.primary_domain, "software_engineering")

    def test_combines_secondary_domain(self) -> None:
        result = KachaniOS().respond(
            Message("Plan my budget and organize the tasks for my business")
        )
        self.assertEqual(result.route.primary_domain, "finance")
        self.assertGreaterEqual(len(result.agent_outputs), 1)
        self.assertIn("Next actions:", result.text)

    def test_rejects_empty_message(self) -> None:
        with self.assertRaises(ValueError):
            KachaniOS().respond(Message("   "))


if __name__ == "__main__":
    unittest.main()
