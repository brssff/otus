import pytest


class TestString:

    string = 'Какая-то строка для тестов'

    def test_islower_method(self):
        assert self.string.islower() == False

    def test_replace_method(self):
        tmp = self.string.replace('тестов', 'теста')
        assert tmp == 'Какая-то строка для теста'

    def test_startswith_method(self):
        assert not self.string.startswith('Неправильный текст')

    @pytest.mark.parametrize('value, expected', [('К', 0), ('в', 25)])
    def test_index_method(self, value, expected):
        assert self.string.index(value) == expected

    @pytest.mark.parametrize('start, end, expected', [(0, 8, 'кАКАЯ-ТО'), (-6, 26, 'ТЕСТОВ')])
    def test_swapcase_method(self, start, end, expected):
        substring = self.string[start:end].swapcase()
        assert substring == expected
