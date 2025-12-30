# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

from click.testing import CliRunner
from mypackage.cli import main

def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(main, ['hello'])
    assert result.exit_code == 0
    assert 'Hello, World!' in result.output

def test_hello_name():
    runner = CliRunner()
    result = runner.invoke(main, ['hello', '--name', 'Anunzio'])
    assert result.exit_code == 0
    assert 'Hello, Anunzio!' in result.output

def test_info():
    runner = CliRunner()
    result = runner.invoke(main, ['info'])
    assert result.exit_code == 0
    assert 'Python CLI Scaffold' in result.output

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
