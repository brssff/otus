import requests
import pytest


BASE_URL = "https://dog.ceo/"


@pytest.mark.parametrize('uri, expected_status', [('api/breeds/list/all', 200), ('api/incorrect/uri', 404)],
                         ids=('positive', 'negative'))
def test_list_all(uri, expected_status):
    r = requests.get(BASE_URL + uri)
    assert r.status_code == expected_status
    assert r.headers['content-type'] == 'application/json'


# пример DDT: тест на корректное кол-во пород в ответе. В json файле лежит полный список
def test_count_all_breeds(all_dog_breeds):
    r = requests.get(BASE_URL + 'api/breeds/list/all')
    assert len(all_dog_breeds) == len(r.json()['message'])


def test_get_single_random_image():
    # проверяю работу основного метода
    r = requests.get(BASE_URL + 'api/breeds/image/random')
    assert r.status_code == 200

    # получаю урл к картинке собаки из ответа, опрашиваю его и проверяю на 200 и content-type
    img_url = r.json()['message']
    req = requests.get(img_url)
    assert req.status_code == 200
    assert req.headers['content-type'] == 'image/jpeg'


@pytest.mark.parametrize('breed', ['hound', 'husky', 'mix'])
def test_getting_array_of_breeds(breed):
    r = requests.get(f"{BASE_URL}api/breed/{breed}/images/random/3")
    assert r.status_code == 200


@pytest.mark.parametrize('breed, subbreed', [('hound', 'walker'), ('bulldog', 'french')])
def test_list_all_subbreeds(breed, subbreed):
    r = requests.get(f"{BASE_URL}api/breed/{breed}/list")
    assert r.status_code == 200
    assert subbreed in r.json()['message']