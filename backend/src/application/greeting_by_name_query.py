from domain.greeting_service import greeting_by_name


def handle(name: str):
    return greeting_by_name(name)
