from flask import Flask
from app.work_with_posts.views import work_with_posts_blueprint
from app.api_endpoints.view import api_blueprint

CONFIG_PATH = "./config.py"

app = Flask(__name__)

app.config.from_pyfile(CONFIG_PATH)
# print(app.config.get("POSTS_DATA_PATH"))

app.register_blueprint(work_with_posts_blueprint)
app.register_blueprint(api_blueprint)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Страница не найдена</h1><p>Попробуйте другой запрос</p>", 404

@app.errorhandler(500)
def page_not_found(e):
    return "<h1>Ошибка на стороне сервера</h1><p>Сообщите в тех. поддержку</p>", 500


if __name__ == '__main__':
    app.run()
