from flask import Flask
from app.work_with_posts.views import work_with_posts_blueprint
from app.api_endpoints.view import api_blueprint
from app.bookmarks.views import bookmarks_blueprint

CONFIG_PATH = "./config.py"

# Создание приложения
app = Flask(__name__)

# Подключение конфигураций из файла с конфигами
app.config.from_pyfile(CONFIG_PATH)

# Регистрация блюпринтов
app.register_blueprint(work_with_posts_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(bookmarks_blueprint)


# Функция вывода страницы с ошибкой 404, если она не найдена
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Страница не найдена</h1><p>Попробуйте другой запрос</p>", 404


# Функция вывода страны с ошибкой 500 по вине сервера
@app.errorhandler(500)
def page_not_found(e):
    return "<h1>Ошибка на стороне сервера</h1><p>Сообщите в тех. поддержку</p>", 500


# Запуск веб-приложения
if __name__ == '__main__':
    app.run()
