# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import click
import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()

@click.group()
@click.version_option()
def main():
    """A sample CLI tool created from a scaffold."""
    pass

@main.command()
@click.option('--name', '-n', default='World', help='Name to greet')
def hello(name):
    """Simple greeting command."""
    click.echo(f"{Fore.GREEN}Hello, {name}!{Style.RESET_ALL}")

@main.command()
def info():
    """Display information about this tool."""
    click.echo(f"{Fore.CYAN}Python CLI Scaffold v0.1.0{Style.RESET_ALL}")
    click.echo("Developed for Anunzio International")

if __name__ == '__main__':
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
