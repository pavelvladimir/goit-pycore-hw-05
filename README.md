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
├── goit_pycore_hw_05/
│   ├── __init__.py
│   └── task_01.py
├── sphinx/
│   ├── conf.py
│   ├── index.rst
│   └── api.rst
├── tests/
│   └── test_task_01.py
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

## Run

Run the CLI with:

```bash
uv run python main.py
```

The CLI asks for `n`, creates a cached Fibonacci function, and prints the result.

Example flow for Task 1:

```text
10
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
