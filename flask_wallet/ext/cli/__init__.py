import click
from flask_wallet.ext.db import db
<<<<<<< HEAD
from flask_wallet.ext.db.models import Receipts
=======
>>>>>>> origin/master

def init_app(app):

    @app.cli.command()
    def hello():
        """Comando teste do CLI"""
        click.echo("Olá! o Teste rolou!")

    @app.cli.command()
    def create_db():
        """Comando teste do CLI"""
        db.create_all()

<<<<<<< HEAD
        click.echo("Criei as tabelas necessárias")
    
    @app.cli.command()
    @click.option("--receipts", "-r")
    @click.option("--month", "-m")
    @click.option("--year", "-y")
    def add_receipts(receipts, month, year):
        """fazendo um teste para inserir uma receita com as flags: -r(receita), -m(mês), -y(ano)"""
        receipts_query = Receipts.add_receipts(
                                        receipts_value=receipts, 
                                        receipts_month=month, 
                                        receipts_year=year)

        click.echo(f"Inseri a receita no valor de:{receipts} do mês {month} do ano {year}")
=======
        click.echo("Criei as tabelas necessárias")
>>>>>>> origin/master
