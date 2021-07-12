import click

def init_app(app):

    @app.cli.command()
    def hello():
        """Comando teste do CLI"""
        click.echo("Olá! o Teste rolou!")