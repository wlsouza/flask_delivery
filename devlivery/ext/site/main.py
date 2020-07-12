import os
import random
from flask import render_template
from flask import Blueprint

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    # todo find a way to use a dynamic path insted of "devlivery/static/img/".
    names = os.listdir("devlivery/static/img/slogan_icons")
    return render_template("index.html", icon_name=random.choice(names))
