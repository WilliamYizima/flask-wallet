from flask_migrate import Migrate
from flask_wallet.ext.db import db
from flask_wallet.ext.db import models

migrate = Migrate()

def init_app(app):
    migrate.init_app(app, db)