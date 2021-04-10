from factories.application import setup_app
from factories.mongo_db import setup_mongo_db


flask_app = setup_app()
setup_mongo_db(flask_app)


@flask_app.route("/health")
def hello():
    return {"status": "Success"}