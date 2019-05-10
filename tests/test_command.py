import typing as t

import pytest
from alembic_autogen_check import main
from click.testing import CliRunner


@pytest.fixture()
def run_command():
    runner = CliRunner()

    def func(args: t.Union[str, t.List[str]]):
        return runner.invoke(main, args)

    return func


def test_help(run_command):
    result = run_command("--help")
    assert result.exit_code == 0


# TODO: Test the actual command
