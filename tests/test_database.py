import data.name_variables


class TestDatabase:

    def test_available_buns(self, mock_database, some_database):
        mock_database.available_buns.return_value = data.name_variables.mock_db_bun
        some_database.available_buns = mock_database.available_buns
        expected = some_database.available_buns()

        assert expected == ["Булочка с начинкой", "Булочка с грибами"]

    def test_available_ingredients(self, mock_database, some_database):
        mock_database.available_ingredients.return_value = data.name_variables.mock_db_ingredient
        some_database.available_ingredients = mock_database.available_ingredients
        expected = some_database.available_ingredients()

        assert expected == ["Магический помидор", "Космо капуста"]
