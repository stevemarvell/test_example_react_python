from unittest.mock import Mock

import pytest
from fastapi import HTTPException

from infrastructure.fastapi.app import greet


@pytest.fixture()
def mock_greeting_repository():
    return Mock()


@pytest.mark.fastapi
def test_greet_user_valid_name(mock_greeting_repository):
    expected_greeting = "Cabbage"
    mock_greeting_repository.get_greeting_by_name.return_value = expected_greeting
    response = greet("Bob", mock_greeting_repository)

    assert response == {"greeting": expected_greeting}


@pytest.mark.fastapi
def test_greet_user_invalid_name(mock_greeting_repository):
    with pytest.raises(HTTPException):
        greet("X", mock_greeting_repository)


@pytest.mark.fastapi
def test_greet_user_blank_name(mock_greeting_repository):
    with pytest.raises(HTTPException):
        greet(None, mock_greeting_repository)

