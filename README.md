# myapp

**Documentation:** https://bstcpext.github.io/sb2/

![CI](https://github.com/bstcpext/sb2/actions/workflows/ci.yml/badge.svg)

## Installation

Clone the repository and install dependencies:

```bash
git clone <repo-url>
cd myapp
uv sync
```

## Usage

Via the CLI entrypoint:

```bash
uv run myapp
```

With dev environment variables loaded:

```bash
uv run --env-file .env myapp
```

Via the Python module:

```bash
uv run python -m myapp
```

## Environment Variables

`.env.example` is the template — copy it to `.env` for development:

```bash
cp .env.example .env
```

| Variable    | Default    | Description                                          |
|-------------|------------|------------------------------------------------------|
| `LOG_LEVEL` | `INFO`     | Console log level. Set to `DEBUG` in `.env` for verbose output. |
| `LOG_FILE`  | `app.log`  | Path to the log file.                                |

Note: uv does not auto-load `.env`. Use `uv run --env-file .env <command>` to load dev settings explicitly.

## Testing

Run tests:

```bash
uv run pytest
```

Run tests with coverage:

```bash
uv run pytest --cov
```

## Documentation

Preview docs locally:

```bash
uv run python scripts/serve_docs.py
```

Build static docs:

```bash
uv run mkdocs build
```
