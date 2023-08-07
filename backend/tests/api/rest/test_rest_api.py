import pytest
import subprocess
import requests


# @todo fix this
@pytest.fixture(scope="module", autouse=True)
def start_app():
    # Start your FastAPI application as a separate process on port 5000
    app_process = subprocess.Popen(["uvicorn", "infrastructure.rest.api:api", "--host", "127.0.0.1", "--port", "5000"])

    # Wait for the application to start
    requests.get("http://127.0.0.1:5000")  # Make a dummy request to ensure the app is up and running

    yield  # This allows the tests to run

    # Terminate the FastAPI application process after all tests have finished
    app_process.terminate()


def test_invalid_endpoint():
    response = requests.get('http://127.0.0.1:5000/')
    assert response.status_code == 404

    response = requests.get('http://127.0.0.1:5000/boink')
    assert response.status_code == 404
