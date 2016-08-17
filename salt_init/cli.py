import click
from salt_init.init import create_formula

@click.command()
@click.option('-f', help='Name of Salt Formula')
def run(f):
  create_formula(f)
