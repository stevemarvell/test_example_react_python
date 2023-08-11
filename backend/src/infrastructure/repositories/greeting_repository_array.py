import os
import json

from domain.greeting_repository import GreetingRepository


class GreetingRepositoryArray(GreetingRepository):

    # dependency injection defaulting to local file
    def __init__(self, greetings_file=f'{os.path.dirname(__file__)}/greetings_array.json'):
        with open(greetings_file, 'r') as config_file:
            self.__greetings_data = json.load(config_file)

    def get_greeting_by_name(self, name: str) -> str:
        greeting = self.__greetings_data['greetings'].get(name.lower(), self.__greetings_data['greetings']['default'])
        return greeting
