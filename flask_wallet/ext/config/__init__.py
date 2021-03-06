def init_app(app):
    app.config["SECRET_KEY"]= "xxx"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flask_wallet.db"

    if app.debug:
        app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
        app.config['DEBUG_TB_PROFILER_ENABLED'] = True
        app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False