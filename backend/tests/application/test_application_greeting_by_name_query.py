from unittest.mock import Mock

import pytest

from application.greeting_by_name_query import handle


@pytest.fixture
def mock_greeting_repository():
    return Mock()
@pytest.mark.parametrize("name, expected_greeting", [("Bob", "Hello"), ("Alice", "Hi")])
def test_handle_greeting_query(name, expected_greeting, mock_greeting_repository):
    mock_greeting_repository.get_greeting_by_name.return_value = expected_greeting
    result = handle(mock_greeting_repository, name)
    assert result == expected_greeting
