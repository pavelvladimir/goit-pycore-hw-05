import re


def generator_numbers(text):
    """Yield all whitespace-delimited numbers found in text."""

    pattern = r"(?<!\S)[+-]?\d+(?:\.\d+)?(?!\S)"

    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text, func):
    """Return the sum of all numbers produced by the given generator function."""

    return sum(func(text))
