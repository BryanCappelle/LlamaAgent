import logging

from flask import Flask

from app.config import configure_app

logging.basicConfig(level=logging.INFO)


def create_app():
    app = Flask(__name__)
    configure_app(app)

    from app.api.routes import api

    app.register_blueprint(api)
    return app


app = create_app()