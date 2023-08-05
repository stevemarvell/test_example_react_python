import pytest

from domain.greeting_service import greeting_by_name


@pytest.mark.parametrize("name, expected_greeting", [("Bob", "Hello"), ("Alice", "Hi")])
def test_bob_non_bob(name, expected_greeting):
    result = greeting_by_name(name)
    assert result == expected_greeting


@pytest.mark.parametrize("name, expected_greeting", [("Bob", "Hello"), ("bob", "Hello")])
def test_caseless(name, expected_greeting):
    result = greeting_by_name(name)
    assert result == expected_greeting
