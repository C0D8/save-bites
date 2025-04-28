from flask import Flask
from save_bites.extensions import configuration
import dotenv # type: ignore
dotenv.load_dotenv()


def minimal_app(**config):
    app = Flask(__name__)
    configuration.init_app(app, **config)

    return app


def create_app(**config):
    app = minimal_app(**config)
    configuration.load_extensions(app)
    
    return app