from injector import Injector

from domain.greeting_repository import GreetingRepository
from infrastructure.repositories.greeting_repository_array import GreetingRepositoryArray


def configure(binder):
    # if test, dev, prod, etc
    binder.bind(GreetingRepository, to=GreetingRepositoryArray)


injector = Injector([configure])


def get_greeting_repository():
    return injector.get(GreetingRepository)
