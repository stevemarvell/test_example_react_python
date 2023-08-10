import pytest
from fastapi import HTTPException
from unittest.mock import Mock, patch

from infrastructure.rest.routes.greeter import greet

@pytest.fixture()
def mock_greeting_repository():
    return Mock()
def test_greet_user_valid_name(mock_greeting_repository):

    expected_greeting = "Cabbage"

    mock_greeting_repository.get_greeting_by_name.return_value = expected_greeting

    response = greet("Bob", mock_greeting_repository)
    assert response == {"greeting": expected_greeting}


def test_greet_user_invalid_name(mock_greeting_repository):
    with pytest.raises(HTTPException) as exc_info:
        greet("X", mock_greeting_repository)

    assert exc_info.value.status_code == 400

def test_greet_user_blank_name():
    with pytest.raises(HTTPException) as exc_info:
        greet(None)

    assert exc_info.value.status_code == 400
