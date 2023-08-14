from schema import Schema

from domain import greeting_service
from domain.greeting_repository import GreetingRepository


def validate(query):
    schema = Schema({
        'name': lambda n: isinstance(n, str) and len(n) >= 2
    })

    schema.validate(query)


def handle(greeting_repository: GreetingRepository, query: dict) -> str:
    validate(query)
    return greeting_service.greeting_by_name(greeting_repository, query['name'])
