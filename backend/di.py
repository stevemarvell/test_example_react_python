from injector import Injector, Module, Binder

from domain.greeting_repository import GreetingRepository
from infrastructure.repositories.greeting_repository_array import GreetingRepositoryArray

def configure(binder):
    # if test, dev, prod, etc
    binder.bind(GreetingRepository, to=GreetingRepositoryArray)

class DependencyManager:
    def __init__(self):
        self.injector = Injector([configure])

    def greeting_repository(self):
        return self.injector.get(GreetingRepository)

# Create a single instance of DependencyManager
dependency_manager = DependencyManager()

