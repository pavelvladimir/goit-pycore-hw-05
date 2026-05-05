---
sidebar_position: 4
---

# Task 4

`task_04.py` implements the assistant bot and uses a decorator to keep input errors from crashing the CLI.

## Requirements covered

- shared `input_error` decorator
- handling of `KeyError`, `ValueError`, and `IndexError`
- separate command handlers
- continuous CLI loop after invalid input
- contact storage in a dictionary

## Example

```bash
uv run python -m goit_pycore_hw_05.task_04
```

Example session:

```text
add
add Bob
add Bob 0501234567
phone
all
exit
```

For the generated Python API reference, open [API Reference](/python-api).
