from flask import Flask
from .main import bp


def init_app(app: Flask):
    app.register_blueprint(bp)
