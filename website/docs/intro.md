---
sidebar_position: 1
---

# Overview

This website documents the Python homework repository.

## Stack

- `uv` manages the Python environment and Python dependencies
- `pnpm` manages the Docusaurus website
- `Sphinx` generates the Python API reference from docstrings
- `Docusaurus` provides the main documentation site

## Commands

Run the Python CLI:

```bash
uv run python main.py
```

Run tests:

```bash
uv run python -m unittest discover -s tests -q
```

Start the documentation site:

```bash
pnpm install
uv sync --group docs
pnpm docs:start
```
