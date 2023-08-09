import click

from di import dependency_manager

from application import greeting_by_name_query


@click.command()
@click.argument('name')
def main(name):
    greeting_repository = dependency_manager.greeting_repository()
    greeting = greeting_by_name_query.handle(greeting_repository, name)
    click.echo(f'{greeting}, {name}!')


if __name__ == '__main__':
    main()
