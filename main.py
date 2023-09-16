from flask import Flask
from app.movie.view import movie_blueprint

# Путь к фалу конфигураций
CONFIG_PATH = "config.py"

# Создание веб-приложения
app = Flask(__name__)

# Подключение конфигураций в веб-приложение
app.config.from_pyfile(CONFIG_PATH)

# Регистрация булпринтов
app.register_blueprint(movie_blueprint)

# Добавление пару настроек в веб-приложений
app.config['JSON_AS_ASCII'] = False
app.config['DEBUG'] = True


# Функция формирования главной страницы
@app.route("/")
def main_page():
    return "<h1>Я главная страница</h1>"


# Запуск веб-приложения
if __name__ == "__main__":
    app.run()
