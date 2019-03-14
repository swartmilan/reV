"""
Generation
"""
import click

from reV.utilities.cli_dtypes import STR
from reV.generation.cli_gen import from_config as run_gen_from_config


@click.group()
@click.option('--name', '-n', default='reV', type=STR,
              help='Job name. Default is "reV".')
@click.option('--config_file', '-c',
              required=True, type=click.Path(exists=True),
              help='reV configuration file json for a single module.')
@click.option('-v', '--verbose', is_flag=True,
              help='Flag to turn on debug logging. Default is not verbose.')
@click.pass_context
def main(ctx, name, config_file, verbose):
    """reV 2.0 config command line interface."""
    ctx.ensure_object(dict)
    ctx.obj['NAME'] = name
    ctx.obj['CONFIG_FILE'] = config_file
    ctx.obj['VERBOSE'] = verbose


@main.command()
@click.option('-v', '--verbose', is_flag=True,
              help='Flag to turn on debug logging.')
@click.pass_context
def generation(ctx, verbose):
    """Run reV 2.0 generation using the config file."""
    config_file = ctx.obj['CONFIG_FILE']
    verbose = any([verbose, ctx.obj['VERBOSE']])
    ctx.invoke(run_gen_from_config, config_file=config_file, verbose=verbose)


if __name__ == '__main__':
    main(obj={})
