import json
import os
import requests
import random
from classes.class_basic_word import BasicWord


def load_random_word_from_internet(url_path):
    """
    Функция загрузки данных слова и набора слов к нему из интернета в форме JSON
    :param url_path: ссылка на ресурс в интернете
    :return: возвращает объект класса BasicWord, если ответ не пришел, то ничего
    """

    url = url_path
    response = requests.get(url, verify=False)

    if response.status_code == 200:
        data_words = response.json()
        word_and_subwords = random.sample(data_words, 1)[0]
        return BasicWord(word=word_and_subwords["word"], set_of_words=word_and_subwords["subwords"])
    else:
        return None


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
