from domain.greeting_repository import GreetingRepository
from domain.greeting_service import greeting_by_name
def handle(greeting_repository: GreetingRepository, name: str) -> str:
    return greeting_by_name(greeting_repository, name)