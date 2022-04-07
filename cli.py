import click
import pathlib
import sys

@click.group()
def cli():
    """A utility for organizing folders on computers"""

    pass

@cli.command()
@click.option(
    "-r",
    "--recursive",
    default=False,
    type=click.BOOL,
    help="Run the process recursively",
)
@click.option(
    "-v",
    "--verbose",
    default=False,
    count=True,
    help= "Run the process verbosely"
)
@click.option(
    "-d",
    "--directory",
    default=pathlib.Path.cwd(),
    type=click.Path(exists=True),
    help="Directory to run the process in"
)
def run(recursive, verbose, directory):
    click.echo(f"{recursive}, {verbose}, {directory}")

if __name__ == "__main__":
    run()
