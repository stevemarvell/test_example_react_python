import pytest

from infrastructure.rest.api import api


@pytest.fixture
def client():
    with api.test_client() as client:
        yield client


def test_default_greeting(client):
    response = client.get('/greet?name=Alice')
    assert response.status_code == 200
    assert response.json == {"greeting": "Hi"}


def test_custom_greeting_for_bob(client):
    response = client.get('/greet?name=Bob')
    assert response.status_code == 200
    assert response.json == {"greeting": "Hello"}


def test_invalid_endpoint(client):
    response = client.get('/')
    assert response.status_code == 404

    response = client.get('/boink')
    assert response.status_code == 404


def test_invalid_args(client):
    response = client.get('/greet')
    assert response.status_code == 400

    response = client.get('/greet?name=')
    assert response.status_code == 400

    response = client.get('/greet?cabbage=')
    assert response.status_code == 400

