from praktikum.ingredient import Ingredient
import pytest


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, ingredient_name , ingredient_price',
                             [["котлета", "мясо единорога", 200], ["сыр", "молоко звездной коровы", 300]])
    def test_get_price(self, ingredient_type, ingredient_name, ingredient_price):
        some_bun = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        bun_price = some_bun.get_price()

        assert bun_price == ingredient_price

    @pytest.mark.parametrize('ingredient_type, ingredient_name , ingredient_price',
                             [["котлета", "мясо единорога", 200], ["сыр", "молоко звездной коровы", 300]])
    def test_get_name(self, ingredient_type, ingredient_name, ingredient_price):
        some_bun = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        bun_price = some_bun.get_name()

        assert bun_price == ingredient_name

    @pytest.mark.parametrize('ingredient_type, ingredient_name , ingredient_price',
                             [["котлета", "мясо единорога", 200], ["сыр", "молоко звездной коровы", 300]])
    def test_get_type(self, ingredient_type, ingredient_name, ingredient_price):
        some_bun = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        bun_price = some_bun.get_type()

        assert bun_price == ingredient_type
