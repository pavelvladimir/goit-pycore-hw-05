---
sidebar_position: 2
---

# Task 2

`generator_numbers(text)` yields numbers from text, and `sum_profit(text, func)` sums them into the final profit value.

## Requirements covered

- regular-expression-based number extraction
- generator with `yield`
- total profit calculation through a passed generator function
- clean separation between extraction and aggregation

## Example

```python
from goit_pycore_hw_05 import generator_numbers, sum_profit

text = (
    "Загальний дохід працівника складається з декількох частин: "
    "1000.01 як основний дохід, доповнений додатковими надходженнями "
    "27.45 і 324.00 доларів."
)

print(sum_profit(text, generator_numbers))
```

For the generated Python API reference, open [API Reference](/python-api).
