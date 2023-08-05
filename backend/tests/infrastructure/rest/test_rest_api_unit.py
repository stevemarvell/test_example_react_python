from unittest.mock import Mock

import pytest

from infrastructure.rest.routes.greeter import greet_process


@pytest.fixture
def valid_request():
    request = Mock()
    # irrelevant that it's asking for name
    request.args.get.return_value = "Bob"
    return request


@pytest.fixture
def invalid_request():
    request = Mock()
    request.args.get.return_value = None
    return request


def test_greet_user_valid_name(valid_request):
    response = greet_process(valid_request)
    assert response[1] == 200


def test_greet_user_invalid_name(invalid_request):
    response = greet_process(invalid_request)

    # never test strings!
    # assert response == {"error": "Invalid or missing 'name' parameter"}

    assert response[1] == 400
