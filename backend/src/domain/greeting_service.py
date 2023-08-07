import json
import os


# @todo DI a repo
def greeting_by_name(name):

    # this is a hack for demo purposes
    # the os should not be in the domain
    # this is all to be done with an injected repo
    
    module_dir = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(module_dir, 'greetings_config.json')

    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)

    greeting = config['greetings'].get(name.lower(), config['greetings']['default'])
    return greeting
