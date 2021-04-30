import pytest
import requests

BASE_URL = 'https://jsonplaceholder.typicode.com/'


@pytest.mark.parametrize('uri', ['posts', 'comments', 'albums', 'photos', 'todos', 'users'])
def test_base_routes_accessible(uri):
    r = requests.get(BASE_URL + uri)
    assert r.status_code == 200, f"Expected 200 OK on route \'{uri}\', but got: {r.status_code}"


def test_create_new_post(data_generator):
    r = requests.post(BASE_URL + 'posts', data=data_generator)
    assert r.status_code == 201
    assert int(r.json()['userid']) == data_generator['userid']


def test_put_posts(data_generator):
    r = requests.put(BASE_URL + 'posts/1', data=data_generator)
    assert r.json()['title'] == data_generator['title']
    assert r.status_code == 200


def test_patch_posts():
    r = requests.patch(BASE_URL + 'posts/1', data=({'title': 'patched!'}))
    assert r.status_code == 200
    assert r.json()['title'] == 'patched!'


def test_delete_users():
    r = requests.delete(BASE_URL + 'users/1')
    assert r.status_code == 200


# фильтрация данных по userId для разных роутов, id получаю из фикстуры
@pytest.mark.parametrize('uri', ['posts', 'comments', 'photos', 'albums'])
def test_filter_data_by_userid(uri, random_exist_userid):
    r = requests.get(BASE_URL + f'{uri}?userid={random_exist_userid}')
    assert r.status_code == 200
    assert r.text
