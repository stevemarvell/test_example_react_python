import json
import os


def greeting_by_name(name):
    module_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(module_dir, 'greetings_config.json')

    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)

    greeting = config['greetings'].get(name.lower(), config['greetings']['default'])
    return greeting
