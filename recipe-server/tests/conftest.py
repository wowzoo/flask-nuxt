import pytest
import os

from app import create_app
from app.extensions import db

from sqlalchemy import text

# populate test data
with open(os.path.join(os.path.dirname(__file__), "data.sql"), "rb") as f:
    raw_sql = f.read().decode("utf8")


@pytest.fixture(scope='session')
def app():
    app = create_app(config_name='test')

    with app.app_context():
        db.create_all()
        db.engine.execute(text(raw_sql))

        yield app

        db.drop_all()
        db.session.commit()


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()
