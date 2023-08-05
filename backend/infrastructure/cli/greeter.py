import click

from application import greeting_by_name_query


@click.command()
@click.argument('name')
def main(name):
    greeting = greeting_by_name_query.handle(name)
    click.echo(f'{greeting}, {name}!')


if __name__ == '__main__':
    main()
