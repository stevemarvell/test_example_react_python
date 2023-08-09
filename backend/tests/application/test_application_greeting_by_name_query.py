import pytest

from di import dependency_manager

from application.greeting_by_name_query import handle


@pytest.mark.parametrize("name, expected_greeting", [("Bob", "Hello"), ("Alice", "Hi")])
def test_handle_greeting_query(name, expected_greeting):
    greeting_repository = dependency_manager.greeting_repository()
    result = handle(greeting_repository, name)
    assert result == expected_greeting
