import click
from flask import Flask
from devlivery.ext.db import db


def init_app(app: Flask):

    @app.cli.command()
    def create_db():
        """This method initializes the database"""
        db.create_all()

    @app.cli.command()
    def list_orders():
        """This method list all orders"""
        click.echo("list of orders")

    @app.cli.command()
    def list_users():
        """This method list all users"""
        click.echo("list of users")

