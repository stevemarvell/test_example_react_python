from abc import ABC, abstractmethod

class GreetingRepository(ABC):
    @abstractmethod
    def get_greeting_by_name(self, name: str) -> str:
        pass