import pytest
from devlivery.app import create_app


@pytest.fixture(scope="module")
def app():
    """
    Fixture to create a flask app for tests.
    :return: A flask app object.
    """
    return create_app()
