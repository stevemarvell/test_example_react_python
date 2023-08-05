import pytest

from infrastructure.rest.api import api


@pytest.fixture
def client():
    with api.test_client() as client:
        yield client


def test_invalid_endpoint(client):
    response = client.get('/')
    assert response.status_code == 404

    response = client.get('/boink')
    assert response.status_code == 404
