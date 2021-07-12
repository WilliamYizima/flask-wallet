from flask import Flask

from flask_wallet.ext import config
from flask_wallet.ext import site
from flask_wallet.ext import db
from flask_wallet.ext import migrate
from flask_wallet.ext import cli
<<<<<<< HEAD
from flask_wallet.ext import api
=======
>>>>>>> origin/master

def create_app():
    app = Flask(__name__)

    config.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    cli.init_app(app)
<<<<<<< HEAD
    api.init_app(app)
=======
>>>>>>> origin/master
    site.init_app(app)

    return app