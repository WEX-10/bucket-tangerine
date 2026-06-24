import pytest
from flask import Flask


@pytest.fixture
def app():
    """Create a test Flask app shared across all REST route tests."""
    app = Flask(__name__)
    app.config['TESTING'] = True
    return app


@pytest.fixture
def client(app):
    """Create a test client from the shared Flask app."""
    with app.test_request_context():
        return app.test_client()
