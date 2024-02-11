from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from config import Config
from app.plans.api import plans_bp

config = Config()


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = config.db_url
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(plans_bp)
    return app


app = create_app()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)