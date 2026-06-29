import re

import pytest
from loguru import logger

from myapp.app import configure_logging, main


def test_main_logs_greeting(capfd):
    main()
    captured = capfd.readouterr()
    assert "Hello from myapp!" in captured.err


def _greeting_line(captured_err):
    lines = [line for line in captured_err.splitlines() if "Hello from myapp!" in line]
    assert lines, "expected a greeting log line on stderr"
    return lines[-1]


def test_console_timestamp_has_no_milliseconds(capfd):
    main()
    line = _greeting_line(capfd.readouterr().err)
    assert re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \| ", line)
    assert not re.search(r"\d{2}:\d{2}:\d{2}\.\d", line), (
        "timestamp should have no milliseconds"
    )


def test_console_uses_pipe_before_message(capfd):
    main()
    line = _greeting_line(capfd.readouterr().err)
    assert line.rstrip().endswith("| Hello from myapp!")
    assert " - Hello from myapp!" not in line


@pytest.mark.parametrize(
    ("method", "abbr"),
    [
        ("debug", "DBG"),
        ("info", "INF"),
        ("warning", "WRN"),
        ("error", "ERR"),
        ("critical", "CRT"),
    ],
)
def test_level_abbreviations(capfd, method, abbr):
    configure_logging()
    getattr(logger, method)("probe message")
    err = capfd.readouterr().err
    assert f"| {abbr} |" in err
