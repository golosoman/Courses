from flask import render_template, request, Blueprint
import picture_loader.config as config
import picture_loader.utils as utils
from json import JSONDecodeError

# Создание Блупринта
picture_loader_blueprint = Blueprint('picture_loader_blueprint', __name__, template_folder='templates')


# Функция формирования страницы веб-страницы с добавлением поста
@picture_loader_blueprint.route('/add_post/', methods=["GET", "POST"])
def post_form_page():
    return render_template(config.POST_FORM_TEMPLATE)


# Функция формирование веб-страницы с ответом о загрузке поста
@picture_loader_blueprint.route('/upload/', methods=["POST"])
def uploads_page():
    picture = request.files.get('picture')
    content = request.form.get('content')

    try:
        picture_path = utils.save_picture_and_content(picture, content)
    except JSONDecodeError as er:
        return f"<h1>Ошибка: {er.msg}</h1><p>Файл: {er.doc}</p>"
    except ValueError:
        return "<h1>Указано неверное расширение файла!</h1>"
    except FileNotFoundError as er:
        return f"<h1>Данные не найдены</h1> <p>{er}</p>"
    else:
        return render_template(config.POST_UPLOADED_TEMPLATE, content=content,
                               picture_path=f"../../{picture_path}")
