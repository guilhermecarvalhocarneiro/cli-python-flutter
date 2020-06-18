import click

from .parser import Parser

# Criando os grupos para permitir agrupar diversos comando

@click.group('flutter')
def flutter():
    """Grupo de comandos do Flutter
    """

@flutter.command()
@click.argument('app_name', type=click.STRING)
def parser(app_name):
    try:
        Parser(app_name).parse()
    except Exception as erro:
        print(f"Ocorreu um erro -> {erro}")
