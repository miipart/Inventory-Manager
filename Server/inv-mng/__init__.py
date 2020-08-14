
from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        """
        Returns the SPA web-client
        """
        return "TEMP THIS IS NOT A CLIENT"

    from .Blueprints import api_blueprint, poc_blueprint

    api_blueprint.RegisterBlueprint(app)
    poc_blueprint.RegisterBlueprint(app)

    return app
