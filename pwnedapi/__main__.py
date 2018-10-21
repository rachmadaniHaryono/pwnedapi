import click
from typing import Any

from . import Password, Scanner


@click.group()
def cli() -> None:
    pass  # pragma: no cover


@cli.command()
@click.password_option(help="Password, which will be checked.")
def check(password: str) -> None:
    "Checks a single password if it has been pwned."
    password_inst: Password = Password(password)
    if password_inst.is_pwned():
        print("Your password has been pwned {} times.".format(password_inst.pwned_count))


@cli.command()
@click.argument('INPUT_FILE', type=click.File('rb'))
@click.option('-o', '--output-format', help='Output data format.', default='csv')
def scan(input_file: click.File, output_format: str = 'csv') -> None:
    "Scan a file for pwned passwords."
    scanner = Scanner()
    scanner.scan(input_file.name)
    print(scanner.export(output_format))
