import requests


def test_url(passed_url, passed_status_code):
    r = requests.get(passed_url)
    assert r.status_code == passed_status_code
