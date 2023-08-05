from pytest_bdd import given, when, then, parsers, scenarios
from click.testing import CliRunner
from infrastructure.cli.greeter import main as command

scenarios("greeter.feature")


@given(parsers.parse('they have a custom greeting "{greeting}"'))
def step_set_greeting(greeting):
    return greeting


@given(parsers.parse('{name} is a user'), target_fixture="name")
def step_set_name(name):
    return name


@when("they run the greeter application", target_fixture="response")
def step_run_app(name):
    runner = CliRunner()
    result = runner.invoke(command, [name])
    assert result.exit_code == 0
    return result.output.strip()


@then(parsers.parse('the application should respond with "{expected_response}"'))
def step_test_response(response, expected_response):
    assert expected_response == response
