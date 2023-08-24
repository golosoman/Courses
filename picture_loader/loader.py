from flask import render_template, request, Blueprint
import picture_loader.config as config
import picture_loader.utils as utils
from json import JSONDecodeError

picture_loader_blueprint = Blueprint('picture_loader_blueprint', __name__, template_folder='templates')


@picture_loader_blueprint.route('/add_post/', methods=["GET", "POST"])
def post_form_page():
    return render_template(config.POST_FORM_TEMPLATE)


@picture_loader_blueprint.route('/upload/', methods=["POST"])
def uploads_page():

    picture = request.files.get('picture')
    content = request.form.get('content')
    try:
        picture_path = utils.save_picture_and_content(picture, content)
    except JSONDecodeError:
        return "<h1>Невозможно преобразовать JSON в список!</h1>"
    except ValueError:
        return "<h1>Указано неверное расширение файла!</h1>"
    except FileNotFoundError as er:
        return f"<h1>Данные не найдены</h1> <p>{er}</p>"
    else:
        # file_name = f'{picture.filename.split(".")[0]}_{current_datetime.day}_{current_datetime.month}_' \
        #             f'{current_datetime.year}_{current_datetime.hour}_{current_datetime.minute}_' \
        #             f'{current_datetime.second}.{picture.filename.split(".")[-1]}'

        # picture_path = f'{config.POST_UPLOADS_PICTURE_PATH}/{file_name}'
        # picture.save(picture_path)
        return render_template(config.POST_UPLOADED_TEMPLATE, content=content,
                               picture_path=f"../../{picture_path}")

