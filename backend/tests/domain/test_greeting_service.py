from unittest.mock import Mock
import pytest

from domain import greeting_service

@pytest.fixture
def mock_greeting_repository():
    return Mock()

def test_get_greeting_for_name(mock_greeting_repository):

    name = "Alice"
    expected_greeting = "Good day, Alice!"

    mock_greeting_repository.get_greeting_by_name.return_value = expected_greeting

    actual_greeting = greeting_service.greeting_by_name(mock_greeting_repository, name)

    assert expected_greeting == actual_greeting
