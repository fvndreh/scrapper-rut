from flask import Flask
from app.routes.rut_validator import rut_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(rut_blueprint, url_prefix="/rut")
    return app
