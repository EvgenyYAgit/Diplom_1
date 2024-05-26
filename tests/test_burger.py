import data.name_variables
import pytest
from unittest.mock import Mock


class TestBurger:
    @pytest.mark.parametrize('name_of_bun', ["чизбургер", "гамбургер"])
    def test_set_buns(self, name_of_bun, some_burger):
        some_burger.set_buns(name_of_bun)
        expected = some_burger.bun

        assert expected == name_of_bun

    @pytest.mark.parametrize('ingredient', ["лунный огурец", "адаманитовый помидор"])
    def test_add_ingredient(self, ingredient, some_burger):
        some_burger.add_ingredient(ingredient)
        expected = some_burger.ingredients

        assert expected == [ingredient]

    @pytest.mark.parametrize('ingredient_one, ingredient_two ',
                             [["лунный огурец", "адаманитовый помидор"], ["марсовый перец", "юпитерский сыр"]])
    def test_remove_ingredient(self, ingredient_one, ingredient_two, some_burger):
        some_burger.add_ingredient(ingredient_one)
        some_burger.add_ingredient(ingredient_two)
        some_burger.remove_ingredient(0)
        expected = some_burger.ingredients

        assert expected == [ingredient_two]

    @pytest.mark.parametrize('ingredient_one, ingredient_two ',
                             [["лунный огурец", "адаманитовый помидор"], ["марсовый перец", "юпитерский сыр"]])
    def test_move_ingredient(self, ingredient_one, ingredient_two, some_burger):
        some_burger.add_ingredient(ingredient_one)
        some_burger.add_ingredient(ingredient_two)
        some_burger.move_ingredient(1, 0)
        expected = some_burger.ingredients
        result = [ingredient_two] + [ingredient_one]

        assert expected == result

    def test_get_price(self, some_burger, mock_bun, mock_ingredient):
        mock_bun.get_price.return_value = data.name_variables.mock_bun_price
        mock_ingredient.get_price.return_value = data.name_variables.mock_ingredient_price
        some_burger.bun = mock_bun
        some_burger.ingredients = [mock_ingredient]
        expected = some_burger.get_price()

        assert expected == 400

    def test_get_receipt(self, some_burger, mock_bun, mock_ingredient):
        mock_bun.get_name.return_value = data.name_variables.mock_bun_name
        mock_ingredient.get_name.return_value = data.name_variables.mock_ingredient_name
        mock_ingredient.get_type.return_value = data.name_variables.mock_ingredient_type
        mock_self = Mock()
        mock_self.get_price.return_value = data.name_variables.mock_self_price
        some_burger.get_price = mock_self.get_price
        some_burger.bun = mock_bun
        some_burger.ingredients = [mock_ingredient]

        expected = some_burger.get_receipt()

        assert expected == "(==== тёмная материя ====)\n= котлета мясо единорога =\n(==== тёмная материя ====)\n\nPrice: 400"
