import pytest


class TestList:
    test_list = ['BMW', 'FORD', 'Lexus', 'BMW', 'Suzuki']

    @pytest.mark.parametrize('value, expected', [('BMW', 2), ('Lexus', 1), ('Mitsubishi', 0)])
    def test_count_method(self, value, expected):
        assert self.test_list.count(value) == expected

    def test_reverse_method(self):
        temp = self.test_list
        temp.reverse()
        assert temp == ['Suzuki', 'BMW', 'Lexus', 'FORD', 'BMW']

    def test_clear_method(self):
        temp = [1, 2, 3, 'Text', 'City']
        temp.clear()
        assert not temp

    @pytest.mark.parametrize('value', ['Suzuki', 'Lexus', 'FORD'])
    def test_remove_method(self, value):
        temp = self.test_list
        temp.remove(value)
        assert value not in temp

    @pytest.mark.parametrize('value', ['Volvo', 'Lada'])
    def test_insert_method(self, value):
        temp = self.test_list
        temp.insert(2, value)
        assert temp[2] == value



