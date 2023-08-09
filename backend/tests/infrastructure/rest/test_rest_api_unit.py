import pytest
from fastapi import HTTPException
from unittest.mock import Mock, patch

from infrastructure.rest.routes.greeter import greet


def test_greet_user_valid_name():

    expected_greeting = "Cabbage"

    mock_greeting_repository = Mock()
    mock_greeting_repository.get_greeting_by_name.return_value = expected_greeting

    response = greet("Bob", mock_greeting_repository)
    assert response == {"greeting": expected_greeting}


def test_greet_user_invalid_name():
    with pytest.raises(HTTPException) as exc_info:
        greet(None)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Invalid or missing 'name' parameter"
