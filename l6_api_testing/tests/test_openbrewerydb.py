import pytest
import requests


BASE_URL = 'https://api.openbrewerydb.org/'


def test_get_all_breweries():
    r = requests.get(BASE_URL + '/breweries')
    assert r.status_code == 200
    assert len(r.json()) == 20


@pytest.mark.parametrize('city', ['Petaluma', 'Castle Rock',
                                  pytest.param('Error city', marks=pytest.mark.xfail)])
def test_get_breweries_by_city_filter(city):
    r = requests.get(BASE_URL + '/breweries', params={'by_city': {city}})
    assert r.status_code == 200
    assert r.json()


def test_get_brewery(random_brewery_id):
    r = requests.get(BASE_URL + 'breweries/' + random_brewery_id)
    # достаточно проверки на 200, т.к. в противном случае будет 404, а не пустой массив и 200 ОК
    assert r.status_code == 200


@pytest.mark.parametrize('value', ['Jessup', 'dog', 'House'])
def test_get_brewery_by_query(value):
    r = requests.get(BASE_URL + 'breweries/search', params={'query': {value}})
    assert r.status_code == 200
    # доп. проверка на наличие тела ответа, если его не будет, то у NoneType не получится взять json()
    assert r.json(), f"Can't find brewery by passed param: {value}"


@pytest.mark.parametrize('value', ['dog', 'boss', 'House'])
def test_autocomplete_method(value):
    r = requests.get(BASE_URL + 'breweries/autocomplete', params={'query': {value}})
    assert r.status_code == 200
    # проверяю что в ответе есть id и name у первого и последнего найденного совпадения
    assert 'id' in r.json()[0]
    assert 'name' in r.json()[-1]
