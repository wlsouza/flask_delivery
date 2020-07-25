from flask import Flask
from devlivery.ext import site
from devlivery.ext import config
from devlivery.ext import toolbar
from devlivery.ext import db
from devlivery.ext import migrate
from devlivery.ext import cli


def create_app():
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app

