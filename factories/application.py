import os
from flask import Flask

from app.blueprints.error_handler.errors import errors
from app.blueprints.covid_cases.api import covid_cases_blueprint
from app.settings import config


def setup_app():
    app = Flask(__name__)
    app.register_blueprint(errors)
    app.register_blueprint(covid_cases_blueprint, url_prefix="/v1/covid_cases")

    config_name = os.getenv('ENVIRONMENT')
    if not config_name:
        raise Exception("Environment Not Found")
    app.config.from_object(config.app_config[config_name])

    @app.after_request
    def set_default_content_type(response):
        response.headers['content-type'] = "application/json"
        return response

    return app
