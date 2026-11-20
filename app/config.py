import os

from dotenv import load_dotenv
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

load_dotenv()
EMBEDDING_MODEL = os.environ["EMBEDDING_MODEL"]


def configure_app(app):
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024

    CORS(
        app,
        origins=os.environ.get("ALLOWED_ORIGINS", "http://localhost:5173").split(","),
        methods=["GET", "POST"],
    )

    if os.environ.get("TRUST_PROXY") == "1":
        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)
