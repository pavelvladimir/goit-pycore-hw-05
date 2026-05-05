---
sidebar_position: 1
---

# Task 1

`caching_fibonacci()` returns an inner Fibonacci function that remembers previously computed values in a closure-based cache.

## Requirements covered

- closure-based cache
- recursive Fibonacci calculation
- cached reuse of previous values
- clean inner-function interface

## Example

```python
from goit_pycore_hw_05 import caching_fibonacci

fib = caching_fibonacci()
print(fib(10))
print(fib(15))
```

For the generated Python API reference, open [API Reference](/python-api).
