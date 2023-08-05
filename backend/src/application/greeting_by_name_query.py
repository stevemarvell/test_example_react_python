from domain.greeting_service import greeting_by_name


def handle(name):
    return greeting_by_name(name)
