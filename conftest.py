import pytest

from settings import reader


@pytest.fixture()
def open_and_close_connection():
    reader.initializeConnection()
    yield
    reader.close()
