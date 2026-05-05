import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from goit_pycore_hw_05.task_04 import (
    add_contact,
    change_contact,
    main,
    parse_input,
    show_all,
    show_phone,
)


class AssistantBotDecoratorTests(unittest.TestCase):
    def test_parse_input_normalizes_command(self):
        command, args = parse_input("  HeLLo John  ")

        self.assertEqual(command, "hello")
        self.assertEqual(args, ["John"])

    def test_add_contact_returns_error_for_missing_arguments(self):
        result = add_contact(["Bob"], {})

        self.assertEqual(result, "Give me name and phone please.")

    def test_add_contact_saves_contact(self):
        contacts = {}

        result = add_contact(["Bob", "0501234567"], contacts)

        self.assertEqual(result, "Contact added.")
        self.assertEqual(contacts, {"Bob": "0501234567"})

    def test_change_contact_returns_not_found_for_unknown_contact(self):
        result = change_contact(["Bob", "0501234567"], {})

        self.assertEqual(result, "Contact not found.")

    def test_show_phone_returns_prompt_when_name_is_missing(self):
        result = show_phone([], {"Bob": "0501234567"})

        self.assertEqual(result, "Enter user name.")

    def test_show_phone_returns_contact_not_found_for_unknown_name(self):
        result = show_phone(["Bob"], {})

        self.assertEqual(result, "Contact not found.")

    def test_show_all_formats_saved_contacts(self):
        result = show_all({"Bob": "0501234567", "Alice": "1234567890"})

        self.assertEqual(result, "Alice: 1234567890\nBob: 0501234567")

    def test_main_runs_conversation_without_stopping_on_input_errors(self):
        output = StringIO()
        inputs = [
            "add",
            "add Bob",
            "add Bob 0501234567",
            "phone",
            "all",
            "exit",
        ]

        with patch("builtins.input", side_effect=inputs), redirect_stdout(output):
            main()

        transcript = output.getvalue()
        self.assertIn("Welcome to the assistant bot!", transcript)
        self.assertIn("Give me name and phone please.", transcript)
        self.assertIn("Contact added.", transcript)
        self.assertIn("Enter user name.", transcript)
        self.assertIn("Bob: 0501234567", transcript)
        self.assertIn("Good bye!", transcript)


if __name__ == "__main__":
    unittest.main()
