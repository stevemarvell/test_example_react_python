from injector import Binder, Module

from domain.greeting_repository import GreetingRepository
from infrastructure.repositories.greeting_repository_array import GreetingRepositoryArray


class GreetingModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(GreetingRepository, to=GreetingRepositoryArray)
