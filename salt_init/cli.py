import click
from salt_init.creation import create_formula

@click.command()
@click.option('-f', help='Name of Salt Formula', required=True)
def run(f):
  create_formula(f)
