from contextlib import contextmanager
import pytest

@pytest.fixture
@contextmanager
def db_session():
    yield None
