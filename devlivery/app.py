from flask import Flask
from devlivery.ext import site
from devlivery.ext import config
from devlivery.ext import toolbar


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    site.init_app(app)
    toolbar.init_app(app)
    return app
