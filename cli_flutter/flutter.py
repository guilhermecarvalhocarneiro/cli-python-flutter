import click

from .parser import Parser

# Criando os grupos para permitir agrupar diversos comando

@click.group('flutter')
def flutter():
    """Grupo de comandos do Flutter
    """

@flutter.command()
@click.argument('app_name', type=click.STRING)
@click.argument('state_manager', type=click.STRING)
@click.argument('replace', type=click.BOOL, default=False)
def parser(app_name, state_manager, replace):
    """Método para gerar a app flutter

    Args:
        app_name (String): Nome da App no formato NomeApp
        state_manager (String): Tipo do gerenciador de estado a ser utilizado, provider ou mobx cubit
    """
    try:
        Parser(app_name, state_manager, replace).parse()
    except Exception as erro:
        print(f"Ocorreu um erro -> {erro}")