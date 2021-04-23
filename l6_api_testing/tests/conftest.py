import pytest
import json


@pytest.fixture()
def all_dog_breeds():
    with open('../data/all_dogs_breeds.json', 'r') as file:
        j = file.read()
        dogs = json.loads(j)
        return dogs
