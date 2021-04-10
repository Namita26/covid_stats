import os
import pytest

from factories.application import setup_app
from factories.mongo_db import setup_mongo_db


@pytest.fixture(scope="session")
def app():
    os.putenv("ENVIRONMENT", "testing")
    app = setup_app()
    setup_mongo_db(app)

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
