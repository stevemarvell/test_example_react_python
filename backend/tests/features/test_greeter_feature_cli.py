import pytest
from click.testing import CliRunner
from pytest_bdd import given, when, then, parsers, scenarios

from infrastructure.cli.greeter_cli import main as command

scenarios("greeter.feature")

@pytest.fixture
def name():
    return "Hi" # for the purposes of the exercise
@given(parsers.parse('{name} is a user'), target_fixture="name")
def step_set_name(name):
    return name

@given(parsers.parse('they have a custom greeting "{greeting}"'), target_fixture="response")
def step_set_custom_greeting(greeting):
    return greeting

@when("they are greeted", target_fixture="actual_response")
def step_run_app(name):
    runner = CliRunner()
    result = runner.invoke(command, [name])
    assert result.exit_code == 0
    return result.output.strip()


@then(parsers.parse('the greeting is "{expected_response}"'))
def step_test_response(actual_response, expected_response):
    assert actual_response == expected_response
