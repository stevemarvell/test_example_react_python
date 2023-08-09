import os
import json

from domain.greeting_repository import GreetingRepository

class GreetingRepositoryArray(GreetingRepository):

    def get_greeting_by_name(self, name: str) -> str:
        module_dir = os.path.dirname(os.path.abspath(__file__))
        config_file_path = os.path.join(module_dir, 'greetings_array.json')

        with open(config_file_path, 'r') as config_file:
            config = json.load(config_file)

        greeting = config['greetings'].get(name.lower(), config['greetings']['default'])
        return greeting
