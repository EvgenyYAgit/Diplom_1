from praktikum.bun import Bun
import pytest


class TestBun:
    @pytest.mark.parametrize('name_of_bun, price_of_bun ', [["Чизбургер", 200], ["Гамбургер", 300]])
    def test_get_name_bun(self, name_of_bun, price_of_bun):
        some_bun = Bun(name_of_bun, price_of_bun)
        excepted = some_bun.get_name()

        assert excepted == name_of_bun

    @pytest.mark.parametrize('name_of_bun, price_of_bun ', [["Чизбургер", 200], ["Гамбургер", 300]])
    def test_get_price_bun(self, name_of_bun, price_of_bun):
        some_bun = Bun(name_of_bun, price_of_bun)
        excepted = some_bun.get_price()

        assert excepted == price_of_bun
