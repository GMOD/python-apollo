import click
from arrow.cli import pass_context, json_loads
from arrow.decorators import apollo_exception, dict_output

@click.command('findAllValues')


@pass_context
@apollo_exception
@dict_output
def cli(ctx):
    """TODO: Undocumented
    """
    return ctx.gi.cannedvalues.findAllValues()
