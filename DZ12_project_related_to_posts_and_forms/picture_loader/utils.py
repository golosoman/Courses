from datetime import datetime
from json import JSONDecodeError
import logging
import picture_loader.config as config
import classes.database_loader as database_loader

# Подключение константы с расширениями, которые должен поддерживать файл и логгирования
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
logging.basicConfig(encoding="utf-8", level=logging.INFO)


def save_picture_and_content(picture, content: str):
    """
    Функция сохранения файла-картинки в фай по пути
    :param picture: искомые данные картинки FileStorag
    :param content: комментарий к посту
    :return: путь сохраненной картинки, либо выбрасывает одну из ошибок: "FileNotFoundError", "JSONDecodeError"
    """

    # Используем дату для создания уникального имени файла
    current_datetime = datetime.now()

    name_picture = picture.filename.split(".")[0]
    extension_picture = picture.filename.split(".")[-1]

    # Проверка расширения файла
    if extension_picture not in ALLOWED_EXTENSIONS:
        # Лог на проверку расширения картинки
        logging.info(f"{name_picture}: картинкой не является!")
        raise ValueError("Неверное расширение файла!")

    # Создание уникального имени файла
    file_name = f'{name_picture}_{current_datetime.day}_{current_datetime.month}_' \
                f'{current_datetime.year}_{current_datetime.hour}_{current_datetime.minute}_' \
                f'{current_datetime.second}.{extension_picture}'

    picture_path = f'{config.POST_UPLOADS_PICTURE_PATH}/{file_name}'

    try:
        picture.save(picture_path)
    except FileNotFoundError:
        logging.error("Ошибка при загрузке файла!")
        raise FileNotFoundError("Путь к сохранению картинки не найден!")

    data = {"pic": f"{picture_path}", "content": f"{content}"}

    try:
        database_loader.DatabaseLoader(config.POSTS_PATH).upload_data_to_file(data)
    except FileNotFoundError as er:
        raise FileNotFoundError(er)
    except JSONDecodeError as er:
        raise JSONDecodeError(msg=er.msg, doc=er.doc, pos=er.pos)
    return picture_path
