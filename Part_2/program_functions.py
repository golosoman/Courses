import os
import json
import random
from class_question import Question


def load_questions_from_file(path):
    """
    Функция загрузки вопросов из файла JSON
    :param path: путь к файлу с вопросами
    :return: возвращает словарь вопросов или None - если такого файла не существует
    """

    if os.path.exists(path):
        with open(path, "rt", encoding="utf-8") as file:
            return json.load(file)
    else:
        return None


def get_questions(file_questions):
    """
    Функция получения списка вопросов из данных, считанных из файла
    :param file_questions: данные считанные из файла
    :return: возвращает список вопросов
    """

    questions = list()
    for dict_question in file_questions:
        question = dict_question['question']
        answer = dict_question['answer']
        level = dict_question['level']
        questions.append(Question(question, int(level), answer))
    random.shuffle(questions)
    return questions


def show_stats(statistic):
    """
    Функция вывода статистики за текущую игру
    :param statistic: Словарь, словарей - с данными статистики из игры
    :return: возвращает строку с количеством очков и правильных/неправильных ответов
    """

    for name in statistic.keys():
        score = statistic[name]["score"]
        true_answers = statistic[name]["correct_answers"]
        false_answers = statistic[name]["incorrect_answers"]
        return f'{name}, ваш счет: {score}\nОтвечено вопросов {true_answers} из {true_answers + false_answers}'


def save_result_to_file(path, statistic):
    """
    Функция сохранения результата игры в файл JSON
    :param path: путь, в который сохраняются данные
    :param statistic: словарь словарей - данные статистики игры
    """

    with open(path, "r", encoding="utf-8") as file:
        if os.stat(path).st_size != 0:
            result = json.load(file)
            result.update(statistic)
        else:
            result = statistic

    with open(path, "w", encoding="utf-8") as file:
        json.dump(result, file)
