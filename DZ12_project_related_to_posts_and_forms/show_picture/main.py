from flask import render_template, request, Blueprint
import logging
from json import JSONDecodeError
import show_picture.config as config
import classes.database_loader as database_loader
import show_picture.utils as utils

# Создание Блупринта и подключение логгирования
logging.basicConfig(encoding="utf-8", level=logging.INFO)
show_picture_blueprint = Blueprint('show_picture_blueprint', __name__, template_folder='templates')


# Функция формирования главной страницы
@show_picture_blueprint.route('/')
def main_page():
    return render_template(config.INDEX_TEMPLATE)


# Функция формирования страницы по запросу пользователя
@show_picture_blueprint.route('/search/')
def search_post_page():
    try:
        data_from_base = database_loader.DatabaseLoader(config.POSTS_PATH).load_data_from_file()
    except FileNotFoundError as er:
        return f"<h1>Данные не найдены</h1> <p>{er}</p>"
    except JSONDecodeError as er:
        return f"<h1>Ошибка: {er.msg}</h1><p>Файл: {er.doc}</p>"
    else:
        key_post = request.args['s']
        logging.info(f'Слово для поиска: {key_post}')
        request_posts = utils.get_posts_on_request(key_post=key_post, data_from_base=data_from_base)
        return render_template(config.POST_LIST_TEMPLATE, key_post=key_post, posts_list=request_posts)
