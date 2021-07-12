from flask import Flask

from flask_wallet.ext import site
from flask_wallet.ext import cli

def create_app():
    app = Flask(__name__)

    cli.init_app(app)
    site.init_app(app)
    
    return app