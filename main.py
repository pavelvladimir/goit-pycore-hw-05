from goit_pycore_hw_05 import caching_fibonacci


def main():
    user_input = input("Enter n for Fibonacci: ").strip()

    try:
        n = int(user_input)
    except ValueError:
        print("Invalid input: n must be an integer.")
        return

    fibonacci = caching_fibonacci()
    print(f"Fibonacci({n}) = {fibonacci(n)}")


if __name__ == "__main__":
    main()
