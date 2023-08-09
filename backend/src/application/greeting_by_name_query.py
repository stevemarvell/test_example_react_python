from domain.greeting_repository import GreetingRepository

def handle(greeting_repository: GreetingRepository, name: str) -> str:
    return greeting_repository.get_greeting_by_name(name)