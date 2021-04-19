import pytest


# нужно для нормального отображения кириллицы в pytest output
def pytest_make_parametrize_id(val):
    return repr(val)


@pytest.fixture
def common_set():
    return set('John said: I\'m 20 years old')