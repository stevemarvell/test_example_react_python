import pytest
from fastapi import Query, HTTPException

from infrastructure.rest.routes.greeter import greet


def test_greet_user_valid_name():
    response = greet("Bob")
    assert response == {"greeting": "Hello"}


def test_greet_user_invalid_name():
    with pytest.raises(HTTPException) as exc_info:
        greet(None)

    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Invalid or missing 'name' parameter"
