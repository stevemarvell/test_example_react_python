from click.testing import CliRunner

from infrastructure.cli.greeter_cli import main


def test_greeting_by_name_query():
    runner = CliRunner()

    result = runner.invoke(main, ['Bob'])
    assert result.exit_code == 0
    assert result.output.strip() == 'Hello, Bob!'
