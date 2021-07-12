import click
from flask_wallet.ext.db import db

def init_app(app):

    @app.cli.command()
    def hello():
        """Comando teste do CLI"""
        click.echo("Olá! o Teste rolou!")

    @app.cli.command()
    def create_db():
        """Comando teste do CLI"""
        db.create_all()

        click.echo("Criei as tabelas necessárias")