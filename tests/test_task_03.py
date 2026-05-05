import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from goit_pycore_hw_05.task_03 import (
    build_log_report,
    count_logs_by_level,
    display_log_counts,
    filter_logs_by_level,
    load_logs,
    main,
    parse_log_line,
)


SAMPLE_LOGS = """2024-01-22 08:30:01 INFO User logged in successfully.
2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
2024-01-22 09:00:45 ERROR Database connection failed.
2024-01-22 09:15:10 INFO Data export completed.
2024-01-22 10:30:55 WARNING Disk usage above 80%.
2024-01-22 11:05:00 DEBUG Starting data backup process.
2024-01-22 11:30:15 ERROR Backup process failed.
2024-01-22 12:00:00 INFO User logged out.
2024-01-22 12:45:05 DEBUG Checking system health.
2024-01-22 13:30:30 INFO Scheduled maintenance.
"""


class LogAnalysisTests(unittest.TestCase):
    def create_log_file(self, content=SAMPLE_LOGS):
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)
        file_path = Path(temp_dir.name) / "sample.log"
        file_path.write_text(content, encoding="utf-8")
        return str(file_path)

    def test_parse_log_line_returns_expected_parts(self):
        line = "2024-01-22 09:00:45 ERROR Database connection failed."

        result = parse_log_line(line)

        self.assertEqual(
            result,
            {
                "date": "2024-01-22",
                "time": "09:00:45",
                "level": "ERROR",
                "message": "Database connection failed.",
            },
        )

    def test_load_logs_reads_all_entries(self):
        file_path = self.create_log_file()

        result = load_logs(file_path)

        self.assertEqual(len(result), 10)

    def test_filter_logs_by_level_is_case_insensitive(self):
        logs = load_logs(self.create_log_file())

        result = filter_logs_by_level(logs, "error")

        self.assertEqual(len(result), 2)
        self.assertTrue(all(log["level"] == "ERROR" for log in result))

    def test_count_logs_by_level_returns_expected_counts(self):
        logs = load_logs(self.create_log_file())

        result = count_logs_by_level(logs)

        self.assertEqual(
            result,
            {"INFO": 4, "DEBUG": 3, "ERROR": 2, "WARNING": 1},
        )

    def test_display_log_counts_formats_table(self):
        counts = {"INFO": 4, "DEBUG": 3, "ERROR": 2, "WARNING": 1}

        result = display_log_counts(counts)

        self.assertEqual(
            result,
            "\n".join(
                [
                    "Log level        | Count",
                    "-----------------|--------",
                    "INFO             | 4",
                    "DEBUG            | 3",
                    "ERROR            | 2",
                    "WARNING          | 1",
                ]
            ),
        )

    def test_build_log_report_includes_filtered_details(self):
        file_path = self.create_log_file()

        result = build_log_report(file_path, "error")

        self.assertIn("Details for level 'ERROR':", result)
        self.assertIn("2024-01-22 09:00:45 - Database connection failed.", result)
        self.assertIn("2024-01-22 11:30:15 - Backup process failed.", result)

    def test_main_returns_usage_error_for_missing_arguments(self):
        output = StringIO()

        with redirect_stdout(output):
            result = main([])

        self.assertEqual(result, 1)
        self.assertIn("Usage:", output.getvalue())


if __name__ == "__main__":
    unittest.main()
