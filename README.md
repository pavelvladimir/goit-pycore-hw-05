# goit-pycore-hw-05

This repository is set up for `uv` and organized so each homework assignment can live in its own module. It also includes a documentation stack based on `pnpm`, Docusaurus, and Sphinx-generated API pages.

## Project Structure

```text
goit-pycore-hw-05/
├── main.py
├── pyproject.toml
├── package.json
├── pnpm-lock.yaml
├── pnpm-workspace.yaml
├── README.md
├── .gitignore
├── uv.lock
├── data/
│   └── sample.log
├── goit_pycore_hw_05/
│   ├── __init__.py
│   ├── task_01.py
│   ├── task_02.py
│   └── task_03.py
├── sphinx/
│   ├── conf.py
│   ├── index.rst
│   └── api.rst
├── tests/
│   ├── test_task_01.py
│   ├── test_task_02.py
│   └── test_task_03.py
└── website/
    ├── docs/
    ├── src/
    ├── docusaurus.config.js
    ├── package.json
    └── sidebars.js
```

## Task 1

The module [goit_pycore_hw_05/task_01.py](goit_pycore_hw_05/task_01.py) contains the `caching_fibonacci()` function.

It:

- returns an inner `fibonacci(n)` function
- uses a closure-based cache dictionary
- calculates Fibonacci numbers recursively
- reuses previously computed values from the cache

## Task 2

The module [goit_pycore_hw_05/task_02.py](goit_pycore_hw_05/task_02.py) contains the `generator_numbers(text)` and `sum_profit(text, func)` functions.

It:

- extracts numbers from text with a generator
- uses regular expressions to find whitespace-delimited numeric values
- converts found values to `float`
- sums all yielded values into the total profit

## Task 3

The module [goit_pycore_hw_05/task_03.py](goit_pycore_hw_05/task_03.py) contains the log analysis functions and a standalone CLI entrypoint.

It:

- parses log lines into date, time, level, and message fields
- loads logs from a file and counts entries by level
- filters logs by a selected logging level
- formats the results as a readable table
- can be run directly with a log file path and an optional level filter

## Run

Run the CLI with:

```bash
uv run python main.py
```

The CLI lets you choose a task and prints the computed result.

Example flow for Task 1:

```text
1
10
```

Example flow for Task 2:

```text
2
Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.
```

Example flow for Task 3:

```text
3
data/sample.log
error
```

Standalone command-line usage for Task 3:

```bash
uv run python -m goit_pycore_hw_05.task_03 data/sample.log error
```

## Tests

Run the test suite with:

```bash
uv run python -m unittest discover -s tests -q
```

## Documentation

The documentation setup uses:

- `pnpm` for the Docusaurus site in `website/`
- `uv` for Python tooling
- `Sphinx` to generate API reference from Python docstrings

Install dependencies:

```bash
pnpm install
uv sync --group docs
```

Start the docs site locally:

```bash
pnpm docs:start
```

Build the static docs output:

```bash
pnpm docs:build
```
