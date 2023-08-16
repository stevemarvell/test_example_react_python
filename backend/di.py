from functools import wraps

from injector import Injector

from domain.greeting_repository import GreetingRepository
from dependencies.greeting_module import GreetingModule  # Import your existing module
from infrastructure.repositories.greeting_repository_array import GreetingRepositoryArray


class DependencyManager:
    def __init__(self):
        self.injector = Injector(modules=[GreetingModule()])

    def greeting_repository(self):
        return self.injector.get(GreetingRepository)


# Create a single instance of DependencyManager
dependency_manager = DependencyManager()

def configure(binder):
    # if test, dev, prod, etc
    repository = GreetingRepositoryArray()
    binder.bind(GreetingRepository, to=repository)