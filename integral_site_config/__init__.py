"""Top-level package for INTEGRAL site configuration."""

__author__ = """Volodymyr Savchenko"""
__email__ = "contact@volodymyrsavchenko.com"
__version__ = "0.1.0"

from dynaconf import Dynaconf, Validator
import click

from pathlib import Path


settings = Dynaconf(
    envvar_prefix="INTEGRAL",
    settings_files=[
        Path.home() / ".integral-settings.toml",
    ],
)

settings.validators.register(
    Validator("REP_BASE_PROD", must_exist=True),
    Validator("IC_BASE", must_exist=True)
)

settings.validators.validate()


@click.group()
def cli():
    pass

@cli.command()
def show():
    pass


if __name__ == "__main__":
    cli()