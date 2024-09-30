import json
import os
import re


def load_questions(path):
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


def show_field(data_for_field):
    """
    Функция вывода игрового поля
    :param data_for_field: словарь с вопросами
    :return: возвращает текстовое игровое поле
    """

    field_string = "\n"

    for category in data_for_field:
        string_price = ""
        for price in data_for_field[category]:
            if data_for_field[category][price]['asked']:
                string_price += f"{'':4}\t"
            else:
                string_price += f"{price:4}\t"
        field_string += f"{category:10}\t{string_price.rstrip()}\n"

    return field_string


def parse_input(string, data_for_field):
    """
    Функция деления ввода пользователя на категорию и число
    :param string: строка с вводом пользователя
    :param data_for_field: словарь вопросов
    :return: возвращает категорию и стоимость вопроса или None, если есть ошибки во вводе пользователя
    """

    if re.fullmatch(r'\w+\s\d+', string):
        category, number = string.capitalize().split(" ")
        if category in data_for_field:
            if number in data_for_field[category] and not data_for_field[category][number]["asked"]:
                return [category, number]

    return None


def show_questions(category, number, data_for_field):
    """
    Функция вывода вопроса на экран
    :param category: категория вопроса
    :param number: стоимость вопрос
    :param data_for_field: словарь вопросов
    :return: возвращает строку с вопросом
    """

    eng_word = data_for_field[category][number]["question"]

    return f'Слово {eng_word} в переводе означает ...'


def process_answer(category, number, data_for_field, user_answer):
    """
    Функция обработки ответа пользователя на вопрос
    :param category: категория вопроса
    :param number: стоимость вопрос
    :param data_for_field: словарь вопросов
    :param user_answer: ответ пользователя на вопрос
    :return: возвращает число очков, начисленных за ответ на вопрос
    """

    data_for_field[category][number]["asked"] = True

    if data_for_field[category][number]["answer"] == user_answer.lower():
        return int(number)
    else:
        return -int(number)


def show_stats(statistic):
    """
    Функция вывода статистики за текущую игру
    :param statistic: Словарь, словарей - с данными статистики из игры
    :return: возвращает строку с количеством очков и правильных/неправильных ответов
    """
    for name in statistic.keys():
        score = statistic[name]["points"]
        true_answers = statistic[name]["correct"]
        false_answers = statistic[name]["incorrect"]
        return f'{name}, ваш счет: {score}\nВерных ответов: {true_answers}\nНеверных ответов: {false_answers}'


def count_questions(data_for_field):
    """
    Функция подсчета вопросов в игре
    :param data_for_field: словарь вопросов
    :return: возвращает число доступных вопросов
    """

    counter = 0

    for category in data_for_field:
        for number in data_for_field[category]:
            if not data_for_field[category][number]["asked"]:
                counter += 1

    return counter


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
