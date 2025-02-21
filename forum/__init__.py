"""Initialize flask app"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from forum.config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    csrf = CSRFProtect(app)
    db = SQLAlchemy()
    csrf.init_app(app)

    db.init_app(app)

    with app.app_context():
        from . import routes

        db.create_all()

        return app
