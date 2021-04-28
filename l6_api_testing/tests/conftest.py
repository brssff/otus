import pytest
import json
import requests
from faker import Faker
import random


@pytest.fixture()
def all_dog_breeds():
    with open('../data/all_dogs_breeds.json', 'r') as file:
        j = file.read()
        dogs = json.loads(j)
        return dogs


fake = Faker()


@pytest.fixture()
def data_generator():
    data = {
        'title': fake.name(),
        'body': fake.text(),
        'userid': fake.random_int()
    }
    return data


# возвращает случайный userId из списка существующих
@pytest.fixture()
def random_exist_userid():
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    return random.randrange(0, (len(r.json())), 1)


# считывает id всех пивных (они вроде как меняются каждый день =\) и возвращает строку для конкатенации в URLе
@pytest.fixture()
def random_brewery_id():
    r = requests.get('https://api.openbrewerydb.org/breweries')
    brew_ids = []
    for i in range(len(r.json())):
        brew_ids.append(r.json()[i]['id'])
    return str(random.choice(brew_ids))
