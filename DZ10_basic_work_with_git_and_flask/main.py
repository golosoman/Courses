from flask import Flask
from config import CANDIDATES_PATH
from classes.candidates import Candidates


# Подключаем работу с Flask
app = Flask(__name__)

# Получаем кандидатов из базы по пути CANDIDATES_PATH
candidates = Candidates(CANDIDATES_PATH)


# Функция формирования наполнения главной веб-страницы
@app.route('/')
def main_page():
    string = "<pre>\n"

    for id_candidate in range(candidates.get_count_candidates()):
        name, position, skills = candidates.get_info(str(id_candidate + 1))
        
        string += f"Имя кандидата - {name}\n" \
                  f"Позиция кандидата - {position}\n" \
                  f"Навыки через запятую - {skills}\n\n"

    string += "</pre>"

    return string


# Функция формирования наполнения страницы кандидатов
@app.route('/candidate/<candidate_id>/')
def candidate_by_id_page(candidate_id):
    picture, name, position, skills = candidates.get_info_with_photo(candidate_id)

    return f"<img src=\"{picture}\" width=\"500\" height=\"500\">\n\n" \
           f"<pre>Имя кандидата - {name}\n" \
           f"Позиция кандидата - {position}\n" \
           f"Навыки через запятую - {skills}\n</pre>"


# Функция формирования наполнения страницы с кандидатами, имеющими нужные навыки
@app.route('/skill/<necessary_skill>/')
def candidate_necessary_skill_page(necessary_skill):
    string = "<pre>\n"

    for id_candidate in range(candidates.get_count_candidates()):
        candidate_skills = candidates.get_skills(str(id_candidate + 1)).split(", ")

        if necessary_skill in candidate_skills:
            name, position, skills = candidates.get_info(str(id_candidate + 1))

            string += f"Имя кандидата - {name}\n" \
                      f"Позиция кандидата - {position}\n" \
                      f"Навыки через запятую - {skills}\n\n"

    string += "</pre>"

    return string


# Запуск веб-приложения
app.run()
