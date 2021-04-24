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
