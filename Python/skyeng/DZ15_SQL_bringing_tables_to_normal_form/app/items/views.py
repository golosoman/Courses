from flask import Blueprint, jsonify
from app.items.dao.items_dao import ItemsDAO
from config import ANIMAL_DB_PATH

# Объект класса работы с БД по поиску животных
animals_dao = ItemsDAO(ANIMAL_DB_PATH)

# Создание блупринта для прохода по маршруту movies
animals_blueprint = Blueprint("animals_blueprint", __name__, template_folder="templates")


# Функция загрузки страницы c json по id животного
@animals_blueprint.route("/animals/<id>")
def animal_page_by_id(id):
    animal = animals_dao.get_animal_data(id=id)
    return jsonify(animal)
