import sys

from loguru import logger

# 3-letter level abbreviations. These are not simple prefixes of the level
# names (e.g. WARNING -> WRN, not WAR), so an explicit mapping is required.
_LEVEL_ABBR = {
    "DEBUG": "DBG",
    "INFO": "INF",
    "WARNING": "WRN",
    "ERROR": "ERR",
    "CRITICAL": "CRT",
}


def _fmt(record):
    """Build the log format template for a record.

    A callable format is needed because loguru's format string syntax cannot
    derive the abbreviated level name. The abbreviation is stashed in
    ``record["extra"]`` so the returned template can reference it.

    The trailing ``\n{exception}`` is appended manually: loguru only adds it
    automatically for string formats, so a callable must include it to keep
    tracebacks (e.g. from ``@logger.catch``) in the output.
    """
    record["extra"]["lvl"] = _LEVEL_ABBR.get(
        record["level"].name, record["level"].name[:3]
    )
    return (
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{extra[lvl]}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>\n{exception}"
    )


def configure_logging():
    """Configure loguru for console and file logging.

    Removes the default handler and sets up:
    - stderr handler at LOG_LEVEL (default: INFO, configurable via env var)
    - File handler at DEBUG level writing to LOG_FILE (default: app.log)

    Both handlers share :func:`_fmt`, producing lines like::

        2025-05-07 14:23:45 | INF | myapp.app:main:29 | Hello from myapp!
    """
    import os

    log_level = os.environ.get("LOG_LEVEL", "INFO")
    log_file = os.environ.get("LOG_FILE", "app.log")
    logger.remove()
    logger.add(sys.stderr, level=log_level, format=_fmt)
    logger.add(log_file, level="DEBUG", rotation="50 KB", retention=1, format=_fmt)


@logger.catch
def main():
    """Run the application.

    Configures logging and prints a greeting to verify the setup works.
    """
    configure_logging()
    logger.info("Hello from myapp!")
