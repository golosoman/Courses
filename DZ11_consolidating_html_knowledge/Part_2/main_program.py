from flask import Flask, render_template
from classes.candidates import Candidates
import config

# Подключаем работу с Flask
app = Flask(__name__)

# Получаем кандидатов из базы по пути CANDIDATES_PATH
candidates = Candidates(path=config.CANDIDATES_PATH)

print(candidates.get_candidate_by_id(1))
print(candidates.get_name(8))

@app.route('/')
def main_page():
    """
    Функция формирования главной страницы веб-приложения
    :return: возвращает шаблон "LIST_TEMPLATE"
    """

    list_candidates = candidates.get_all_candidates()

    return render_template(config.LIST_TEMPLATE, candidates=list_candidates)


#
@app.route('/candidate/<candidate_id>/')
def candidate_page(candidate_id: str):
    """
    Функция формирования страницы кандидата
    :param candidate_id: id кандидата
    :return: возвращает шаблон "SINGLE_TEMPLATE"
    """

    photo, name, position, skills = candidates.get_info_with_photo(candidate_id=int(candidate_id))

    return render_template(config.SINGLE_TEMPLATE, name=name, position=position, photo=photo, skills=skills)


@app.route('/search/<candidate_name>/')
def candidates_by_name(candidate_name: str):
    """
    Функция формирования страницы кандидатов с похожими именами
    :param candidate_name: имя кандидата
    :return: возвращает шаблон "SEARCH_TEMPLATE"
    """

    list_candidates_by_name = candidates.get_candidates_by_name(candidate_name=candidate_name)
    number_of_candidates = len(list_candidates_by_name)

    return render_template(config.SEARCH_TEMPLATE, candidates=list_candidates_by_name,
                           number_of_candidates=number_of_candidates)


@app.route('/skill/<skill_name>/')
def candidates_by_skill(skill_name: str):
    """
    Функция формирования страницы кандидатов с нужным навыком
    :param skill_name: название навыка
    :return: возвращает шаблон SKILL_TEMPLATE
    """

    list_candidates_by_name = candidates.get_candidates_by_skill(skill=skill_name)
    number_of_candidates = len(list_candidates_by_name)

    return render_template(config.SKILL_TEMPLATE, skill=skill_name,
                           number_of_candidates=number_of_candidates, candidates=list_candidates_by_name)


# Запуск веб-приложения
app.run()
