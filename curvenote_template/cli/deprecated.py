import typer

def show_notice():
  typer.echo(
    """
    *** DEPRECATED ***
    The curvenote-template package has been renamed to JTEX - this package will be no longer be updated.
    Install jtex from pypi to get the latest features and fixes.
    """)