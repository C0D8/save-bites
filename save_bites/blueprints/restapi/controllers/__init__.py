from flask import Blueprint
from flask_restx import Api
from .hello import api as hello_api
from .alimento import api as alimento_api
from .user import api as user_api
from flask import redirect, url_for
bp = Blueprint("api", __name__, url_prefix="/api")

api = Api(
    bp,
    title="FLASK RESTPLUS API FOR ACCPC",
    version="1.0",
    doc="/docs",
)

api.add_namespace(hello_api)
api.add_namespace(alimento_api)
api.add_namespace(user_api)

def init_app(app):
    app.register_blueprint(bp)

    @app.route('/')
    def index():
        return redirect(url_for('api.doc'))

    return app
