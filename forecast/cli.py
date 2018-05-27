# -*- coding: utf-8 -*-

"""Console script for pyforecast."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for pyforecast."""
    click.echo("This is Forecast "
               "pyforecast.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
