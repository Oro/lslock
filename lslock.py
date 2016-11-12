#!/usr/bin/env python
import click

@click.command()
@click.argument('path', type=click.Path(exists=True))
def display_locked_files(path):
    """Displays all locked files underneath path."""
    click.echo(click.format_filename(path))
