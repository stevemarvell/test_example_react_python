import pytest
from flask.testing import FlaskClient
from flask_injector import FlaskInjector
from injector import inject
from pytest_bdd import given, when, then, parsers, scenarios

from domain.greeting_repository import GreetingRepository
from infrastructure.flask.app import app, configure

scenarios("greeter.feature")

@pytest.fixture
def client() -> FlaskClient:
    with app.app_context():
        FlaskInjector(app=app, modules=[configure])
        yield app.test_client()

@pytest.fixture
def greeting():
    return "Hi" # for the purposes of the exercise

@given(parsers.parse('{name} is a user'), target_fixture="name")
def step_set_name(name):
    return name

@given(parsers.parse('they have a custom greeting "{greeting}"'), target_fixture="greeting")
def step_set_custom_greeting(greeting):
    return greeting

@when("they are greeted", target_fixture="actual_response")
def step_run_app(client, name, greeting):
    response = client.get(f"/greet?name={name}")
    assert response.status_code == 200
    return response.json['greeting']

#we can't test the actual actual response because we are not front end testing
@then(parsers.parse('the greeting is "{expected_response}"'))
def step_test_response(actual_response, greeting):
    assert actual_response == greeting
