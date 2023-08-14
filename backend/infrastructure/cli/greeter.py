import sys

import click
from schema import SchemaError

from di import dependency_manager

from application import greeting_by_name_query


@click.command()
@click.argument('name')
def main(name):
    greeting_repository = dependency_manager.greeting_repository()

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
