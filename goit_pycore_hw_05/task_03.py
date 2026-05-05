import sys


LEVEL_ORDER = ["INFO", "DEBUG", "ERROR", "WARNING"]


def parse_log_line(line):
    """Parse a single log line into its parts."""

    parts = line.strip().split(maxsplit=3)
    if len(parts) != 4:
        raise ValueError("Invalid log line format.")

    date, time, level, message = parts
    return {
        "date": date,
        "time": time,
        "level": level.upper(),
        "message": message,
    }


def load_logs(file_path):
    """Load and parse log entries from a file."""

    logs = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if not line.strip():
                    continue
                try:
                    logs.append(parse_log_line(line))
                except ValueError as error:
                    raise ValueError(
                        f"Invalid log format on line {line_number}."
                    ) from error
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Log file not found: {file_path}") from error
    except OSError as error:
        raise OSError(f"Unable to read log file: {file_path}") from error

    return logs


def filter_logs_by_level(logs, level):
    """Return only logs that match the selected level."""

    normalized_level = level.upper()
    return list(filter(lambda log: log["level"] == normalized_level, logs))


def count_logs_by_level(logs):
    """Count log entries by logging level."""

    counts = {level: 0 for level in LEVEL_ORDER}

    for log in logs:
        level = log["level"]
        if level not in counts:
            counts[level] = 0
        counts[level] += 1

    return {level: count for level, count in counts.items() if count > 0}


def display_log_counts(counts):
    """Return a formatted table of log counts."""

    lines = [
        f"{'Log level':<17}| {'Count'}",
        f"{'-' * 17}|{'-' * 8}",
    ]

    for level, count in counts.items():
        lines.append(f"{level:<17}| {count}")

    return "\n".join(lines)


def build_log_report(file_path, level=None):
    """Build a full log analysis report for the selected file."""

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    report = display_log_counts(counts)

    if not level:
        return report

    filtered_logs = filter_logs_by_level(logs, level)
    normalized_level = level.upper()
    detail_lines = [f"Details for level '{normalized_level}':"]

    if not filtered_logs:
        detail_lines.append("No log entries found for this level.")
    else:
        for log in filtered_logs:
            detail_lines.append(
                f"{log['date']} {log['time']} - {log['message']}"
            )

    return f"{report}\n\n" + "\n".join(detail_lines)


def main(args=None):
    arguments = sys.argv[1:] if args is None else args

    if not 1 <= len(arguments) <= 2:
        print("Usage: python -m goit_pycore_hw_05.task_03 <log_file_path> [level]")
        return 1

    file_path = arguments[0]
    level = arguments[1] if len(arguments) == 2 else None

    try:
        print(build_log_report(file_path, level))
    except (FileNotFoundError, OSError, ValueError) as error:
        print(f"Error: {error}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
