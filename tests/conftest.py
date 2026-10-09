import pytest
from src.db_connection import get_connection


@pytest.fixture
def db_connection():
    connection = get_connection()

    yield connection

    connection.close()
    