# нужно для нормального отображения кириллицы в pytest output
def pytest_make_parametrize_id(val):
    return repr(val)
