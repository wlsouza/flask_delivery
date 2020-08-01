from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from devlivery.ext.db import db
from devlivery.ext.db import models
from devlivery.ext.admin.userview import UserView


admin = Admin()


def init_app(app: Flask):
    admin.name = "Devlivery"
    admin.template_mode = "bootstrap3"
    admin.init_app(app)

    # Initializing admin views
    admin.add_views(UserView(models.User, db.session))
    admin.add_views(ModelView(models.Category, db.session))
    admin.add_views(ModelView(models.Items, db.session))
    admin.add_views(ModelView(models.Store, db.session))
    admin.add_views(ModelView(models.Checkout, db.session))
