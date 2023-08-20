import random


def read_data(name_file):
    """
    Функция считывания данных из файла
    :param name_file: название файла
    :return: возвращает список строк из файла
    """

    data = []
    with open(name_file, "r", encoding="utf-8") as file:
        for line in file:
            data.append(line.rstrip())
    return data


def write_rating(user_name, user_rating, name_file):
    """
    Функция записи рейтинга в файл
    :param user_name: имя пользователя
    :param user_rating: рейтинг пользователя
    :param name_file: название файла
    """

    with open(name_file, "a", encoding="utf-8") as file:
        file.write(f'{user_name} {user_rating}\n')


def print_statistic(name_file):
    """
    Функция вывода статистики из файла
    :param name_file: название файла
    :return: возвращает статистику, максимальный рейтинг и количество игр
    """

    scores = list()
    with open(name_file, "r", encoding="utf-8") as file:
        for line in file:
            user_name, user_rating = line.split(" ")
            scores.append(int(user_rating))
    return {"max_score": max(scores), "games_played": len(scores)}


def shuffle_word(word):
    """
    Функция изменения положения букв в слове
    :param word: входное слово
    :return: возвращает слово с измененным положением букв
    """

    mixed_word = list(word)

    while True:
        random.shuffle(mixed_word)
        if ''.join(mixed_word) != word:
            break

    return mixed_word
