import pytest
from main import app
from app.items.dao.items_dao import ItemsDAO


# Фикстура с данными из ItemsDAO
@pytest.fixture()
def get_animals_dao():
    animals_dao = ItemsDAO(app.config.get("ANIMAL_DB_PATH"))
    return animals_dao
