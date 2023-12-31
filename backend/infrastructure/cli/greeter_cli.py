import sys

import click
from schema import SchemaError

from application import greeting_by_name_query
import di

@click.command()
@click.argument('name')
def main(name):
    greeting_repository = di.get_greeting_repository()

    try:
        greeting = greeting_by_name_query.handle(greeting_repository, {"name": name})
        click.echo(f'{greeting}, {name}!')
    except SchemaError as e:
        click.echo(f"Well that didn't validate!")
        sys.exit(1)
    except Exception as e:
        click.echo(f"Well, that didn't work at all!")
        sys.exit(2)


if __name__ == '__main__':
    main()
