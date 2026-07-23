import unittest

from src.router import route_message


class RouterTests(unittest.TestCase):
    def test_routes_study_request(self) -> None:
        self.assertEqual(
            route_message("Help me prepare for my SQL exam"),
            "studies",
        )

    def test_routes_software_request(self) -> None:
        self.assertEqual(
            route_message("I need help debugging a Python API"),
            "software_engineering",
        )

    def test_falls_back_to_general(self) -> None:
        self.assertEqual(route_message("How are you today?"), "general")


if __name__ == "__main__":
    unittest.main()
