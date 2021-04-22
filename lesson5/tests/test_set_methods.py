import pytest


class TestSet:

    @pytest.mark.parametrize('value', ['9', 'X'])
    def test_add_method(self, value, common_set):
        temp_set = common_set
        assert value not in temp_set
        temp_set.add(value)
        assert value in temp_set

    def test_clear_method(self, common_set):
        set_to_clear = common_set
        assert set_to_clear
        set_to_clear.clear()
        assert not set_to_clear

    def test_discard_method(self, common_set):
        temp_set = common_set
        temp_set.discard('J')
        assert 'J' not in temp_set

    def test_isdisjoint_method(self, common_set):
        temp_set = set('Кириллица_внутри')
        assert temp_set.isdisjoint(common_set)

    @pytest.mark.parametrize('value', ['John', ' ', 'said', '20'])
    def test_issubset_method(self, common_set, value):
        temp_set = set(value)
        assert temp_set.issubset(common_set)
