import pytest

from application.greeting_by_name_query import handle


@pytest.mark.parametrize("name, expected_greeting", [("Bob", "Hello"), ("Alice", "Hi")])
def test_handle_greeting_query(name, expected_greeting):
    result = handle(name)
    assert result == expected_greeting
