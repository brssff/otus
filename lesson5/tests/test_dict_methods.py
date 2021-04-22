import pytest


class TestDict:
    data = dict(age=25, car='mazda', favorite=True, has_dog=False, has_cat=True, city='Ontario', phone='+79991103317')

    def test_pop_method(self):
        new_dict = self.data
        assert new_dict.pop('phone') == '+79991103317'
        assert 'phone' not in new_dict

    @pytest.mark.parametrize('key, value', [('age', 25), ('car', 'mazda'), ('error_key', None)])
    def test_get_method(self, key, value):
        assert self.data.get(key) == value

    def test_values_method(self):
        assert 'Ontario' in self.data.values()

    def test_update_method(self):
        temp_dict = self.data
        temp_dict.update({'country': 'Russia'})
        assert temp_dict['country'] == 'Russia'

    def test_copy_method(self):
        temp_dict = self.data.copy()
        assert temp_dict == self.data
