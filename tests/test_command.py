import typing as t
from pathlib import Path

import pytest
from alembic_autogen_check import main
from click.testing import CliRunner

config_file = Path(__file__).parent / "alembic.ini"


@pytest.fixture()
def run_command():
    runner = CliRunner()

    def func(args: t.Union[str, t.List[str]]):
        return runner.invoke(main, args)

    return func


def test_help(run_command):
    result = run_command("--help")
    assert result.exit_code == 0


def test_version(run_command):
    result = run_command("--version")
    assert result.exit_code == 0


def test_in_sync_exits_with_success(run_command):
    result = run_command(["--config", str(config_file)])
    assert result.exit_code == 0
    assert "INFO: Migrations in sync." in result.output


def test_out_of_sync_exits_with_error(run_command, monkeypatch):
    monkeypatch.setenv("ALEMBIC_OUT_OF_SYNC", "true")
    result = run_command(["--config", str(config_file)])
    assert result.exit_code == 1
    assert "ERROR: Migrations are out of sync with models." in result.output
