import datetime
import runpy
import sys

import pytest

import show_datetime

FIXED_NOW = datetime.datetime(2023, 10, 1, 12, 0, 0)


class FixedDatetime(datetime.datetime):
    @classmethod
    def now(cls, tz=None):
        return FIXED_NOW


@pytest.fixture
def fixed_datetime(monkeypatch):
    monkeypatch.setattr(show_datetime.datetime, "datetime", FixedDatetime)


def test_prints_fixed_datetime(fixed_datetime, capsys):
    show_datetime.print_current_datetime()
    assert capsys.readouterr().out == "Aktualna data i godzina: 2023-10-01 12:00:00\n"


def test_prints_microseconds_when_present(monkeypatch, capsys):
    class WithMicros(datetime.datetime):
        @classmethod
        def now(cls, tz=None):
            return datetime.datetime(2024, 2, 29, 23, 59, 59, 123456)

    monkeypatch.setattr(show_datetime.datetime, "datetime", WithMicros)
    show_datetime.print_current_datetime()
    assert capsys.readouterr().out == "Aktualna data i godzina: 2024-02-29 23:59:59.123456\n"


def test_returns_none(fixed_datetime, capsys):
    assert show_datetime.print_current_datetime() is None


def test_real_time_is_close_to_now(capsys):
    before = datetime.datetime.now()
    show_datetime.print_current_datetime()
    after = datetime.datetime.now()

    out = capsys.readouterr().out
    prefix = "Aktualna data i godzina: "
    assert out.startswith(prefix)
    printed = datetime.datetime.fromisoformat(out[len(prefix):].strip())
    assert before <= printed <= after


def test_runs_as_script(fixed_datetime, capsys, monkeypatch):
    monkeypatch.delitem(sys.modules, "show_datetime", raising=False)
    runpy.run_path(show_datetime.__file__, run_name="__main__")
    assert capsys.readouterr().out == "Aktualna data i godzina: 2023-10-01 12:00:00\n"
