from goit_pycore_hw_05 import caching_fibonacci, generator_numbers, sum_profit
from goit_pycore_hw_05.task_03 import build_log_report


def run_task_01():
    user_input = input("Enter n for Fibonacci: ").strip()

    try:
        n = int(user_input)
    except ValueError:
        print("Invalid input: n must be an integer.")
        return

    fibonacci = caching_fibonacci()
    print(f"Fibonacci({n}) = {fibonacci(n)}")


def run_task_02():
    text = input("Enter text with income values: ")
    total = sum_profit(text, generator_numbers)
    print(f"Total profit: {total}")


def run_task_03():
    file_path = input("Enter path to log file [data/sample.log]: ").strip()
    log_file = file_path or "data/sample.log"
    level = input("Enter log level filter [optional]: ").strip()

    try:
        report = build_log_report(log_file, level or None)
    except (FileNotFoundError, OSError, ValueError) as error:
        print(f"Invalid input: {error}")
        return

    print(report)


def main():
    print("Choose a task:")
    print("1 - Caching Fibonacci")
    print("2 - Sum profit from text")
    print("3 - Log file analysis")
    choice = input("Enter task number: ").strip()

    if choice == "1":
        run_task_01()
        return
    if choice == "2":
        run_task_02()
        return
    if choice == "3":
        run_task_03()
        return

    print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
