from goit_pycore_hw_05 import caching_fibonacci, generator_numbers, sum_profit


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


def main():
    print("Choose a task:")
    print("1 - Caching Fibonacci")
    print("2 - Sum profit from text")
    choice = input("Enter task number: ").strip()

    if choice == "1":
        run_task_01()
        return
    if choice == "2":
        run_task_02()
        return

    print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
