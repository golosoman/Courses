from flask import Flask, render_template
from config import INDEX_TEMPLATE

# Подключаем работу с Flask
app = Flask(__name__)


@app.route('/')
def main_page():
    """
    Функция формирования главной веб-страницы
    :return: возвращает шаблон "INDEX_TEMPLATE"
    """

    return render_template(INDEX_TEMPLATE, name="Пневмослон")

# Запуск веб-приложения
app.run()
