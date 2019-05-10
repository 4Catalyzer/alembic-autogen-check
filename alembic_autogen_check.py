import itertools
import typing as t
from pprint import pformat

import click
from alembic.command import revision
from alembic.config import Config
from alembic.operations.ops import MigrationScript

__version__ = "1.1.1"


def simulate_autogenerate(config_path: str) -> t.List[tuple]:
    """Simulate the `alembic revision --autogenerate` command
    and return a list of generated operations.
    """
    config = Config(config_path)
    revisions: t.List[MigrationScript] = []

    def process_revision_directives(context, revision, directives):
        nonlocal revisions
        revisions = list(directives)
        # Prevent actually generating a migration
        directives[:] = []

    revision(
        config=config,
        autogenerate=True,
        process_revision_directives=process_revision_directives,
    )
    return list(
        itertools.chain.from_iterable(
            op.as_diffs()
            for script in revisions
            for op in script.upgrade_ops_list
        )
    )


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option(version=__version__)
@click.option(
    "--config",
    type=click.Path(exists=True, dir_okay=False),
    default="alembic.ini",
    help="Path to alembic.ini file.",
)
@click.pass_context
def main(ctx: click.Context, config: str):
    """Command to check that alembic mugrations are in sync with your SQLAlchemy models."""
    diff = simulate_autogenerate(config)
    if diff:
        click.secho(
            "ERROR: Migrations are out of sync with models. Diff:",
            fg="red",
            err=True,
        )
        click.secho(pformat(diff, indent=2), fg="red", err=True)
        click.echo(err=True)
        command = click.style(
            "PYTHONPATH=. alembic revision --autogenerate -m 'Your message'",
            bold=True,
        )
        click.echo(f"You may need to run `{command}`.", err=True)
        ctx.exit(1)
    else:
        click.secho("INFO: Migrations in sync.", fg="green", err=True)


if __name__ == "__main__":
    main()
