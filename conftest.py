import pytest
from praktikum.burger import Burger
from unittest.mock import Mock
from praktikum.database import Database


@pytest.fixture
def some_burger():
    some_burger = Burger()
    return some_burger


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    return mock_bun


@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    return mock_ingredient


@pytest.fixture
def mock_database():
    mock_database = Mock()
    return mock_database


@pytest.fixture
def some_database():
    some_database = Database()
    return some_database
