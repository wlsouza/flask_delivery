from flask import Flask


def init_app(app: Flask):
    app.config["SECRET_KEY"] = "uma_secret_key_muito_segura"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///devlivery.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["FLASK_ADMIN_SWATCH"] = "darkly"

    if app.debug:
        app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = True
        app.config["DEBUG_TB_PROFILER_ENABLED"] = True
        app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
