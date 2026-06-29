# Usage

## Installation

Clone the repository and install dependencies:

```bash
uv sync
```

## Running

Via the CLI entrypoint:

```bash
uv run myapp                          # production defaults
uv run --env-file .env myapp          # dev settings
```

Or as a Python module:

```bash
uv run python -m myapp
```

## Environment Variables

| Variable    | Default    | Description                          |
|-------------|------------|--------------------------------------|
| `LOG_LEVEL` | `INFO`     | Console log level (DEBUG, INFO, …)   |
| `LOG_FILE`  | `app.log`  | Path to the log file                 |

Copy `.env.example` to `.env` for development defaults, then run with `uv run --env-file .env`.

## Log format

Both the console and file handlers use a compact format with second-precision
timestamps, 3-letter level abbreviations, and `|` separators throughout:

```
2025-05-07 14:23:45 | INF | myapp.app:main:29 | Hello from myapp!
```

Level abbreviations: `DBG`, `INF`, `WRN`, `ERR`, `CRT`.
