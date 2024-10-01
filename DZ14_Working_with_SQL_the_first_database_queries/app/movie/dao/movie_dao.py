import os
import sqlite3
from typing import List, Dict, Tuple


class MovieDAO:
    """Класс для работы с данными из БД - кино"""

    def __init__(self, path: str):
        """
        Инициализатор класса работы с данными - кино
        :param path: путь к БД
        """

        self.file_path = path

    def __repr__(self):
        """
        Представление для объектов класса
        :return: возвращает путь и его состояние
        """
        return f"Загрузчик Баз Данных по пути: {self.file_path} - {os.path.exists(self.file_path)}"

    def database_connect(self, query: str) -> List[Tuple[str, str, str, str, str]]:
        """
        Метод подключения к базе данных по запросу query
        :param query: запрос к БД
        :return: возвращает список кортежей с данными
        """
        with sqlite3.connect(self.file_path) as connect:
            cursor = connect.cursor()
            cursor.execute(query)
            return cursor.fetchall()

    def find_movie_by_title(self, film_title: str) -> Dict[str, str | int]:
        """
        Метод нахождения самого нового фильма по его названию
        :param film_title: название фильма
        :return: возвращает словарь с данными title, country,
        release_year, genre, description или выбрасывает ошибку ValueError
        """

        # Запрос к базе данных, получаем данные про фильм по названию
        sqlite_query = f"""
        SELECT title, country, release_year, listed_in AS genre, description 
        FROM netflix
        WHERE title = "{film_title}"
        ORDER BY release_year DESC 
        LIMIT 1
        """

        film = self.database_connect(sqlite_query)

        # Проверка на возвращаемы пустой список
        if len(film) != 0:
            film = film[0]
            return {
                "title": film[0],
                "country": film[1],
                "release_year": film[2],
                "genre": film[3],
                "description": film[4].strip(),
            }
        else:
            raise ValueError("Нет данных в базе!")

    def find_movies_by_year_to_year(self, first_year: int, second_year: int) -> List[Dict[str, str | int]]:
        """
        Метод поиска фильмов по диапазону годов выпуска
        :param first_year: первый год
        :param second_year: второй год
        :return: возвращает список с фидльмами по атрибутам: title и release_year, либо выбрасывает ошибку ValueError
        """

        # Запрос к базе данных, получаем данные про фильмы по диапазону годов выпуска
        sqlite_query = f"""
        SELECT title, release_year
        FROM netflix
        WHERE release_year BETWEEN "{first_year}" AND "{second_year}"
        ORDER BY release_year DESC
        LIMIT 100
        """

        films = self.database_connect(sqlite_query)

        # Проверка на возвращаемы пустой список
        if len(films) != 0:
            json_data = list()
            for film in films:
                json_data.append({
                    "title": film[0],
                    "release_year": film[1]
                })
            return json_data
        else:
            raise ValueError("Нет данных в базе!")

    def find_movies_by_rating(self, rating: str) -> List[Dict[str, str]]:
        """
        Метод нахождения фильмов по возрастным ограничениям
        :param rating: название возрастного ограничения
        :return: возвращает фильмы с атрибутами: title, rating, description, либо же ошибку ValueError
        """
        # Словарь с возрастными ограничениями по фильмам в БД
        rating_list = {"children": ['G'], "family": ["G", "PG", "PG-13"], "adult": ["R", "NC-17"]}

        if rating_list.get(rating) is not None:
            # Код для правильного запроса в БД
            film_rating = "\", \"".join(rating_list.get(rating))
            film_rating = f"\"{film_rating}\""

            # Запрос к базе данных, получаем данные про фильмы по возрастным ограничениям
            sqlite_query = f"""
            SELECT title, rating, description
            FROM netflix
            WHERE rating IN ({film_rating})
            LIMIT 100
            """

            films = self.database_connect(sqlite_query)

            # Проверка на возвращаемы пустой список
            if len(films) != 0:
                json_data = list()
                for film in films:
                    json_data.append({
                        "title": film[0],
                        "rating": film[1],
                        "description": film[2].strip(),
                    })
                return json_data
            else:
                raise ValueError("Нет данных в базе!")
        else:
            raise ValueError("Нет такого ограничения в базе!")

    def find_films_by_genre(self, genre: str) -> List[Dict[str, str]]:
        """
        Метод нахождения фильмов по жанру
        :param genre: название жанра
        :return: возвращает список словарей с атрибутами: title, description, либо же ValueError
        """

        # Запрос к базе данных, получаем данные про фильмы по жанру
        sqlite_query = f"""
            SELECT title, description, listed_in as genre, release_year
            FROM netflix
            WHERE genre LIKE "%{genre}%"
            ORDER BY release_year DESC
            LIMIT 10
        """

        films = self.database_connect(sqlite_query)

        # Проверка на возвращаемы пустой список
        if len(films) != 0:
            json_data = list()
            for film in films:
                json_data.append({
                    "title": film[0],
                    "description": film[1].strip(),
                })
            return json_data
        else:
            raise ValueError("Нет данных в базе!")

    def find_actors_which_play_with_two_actors(self, first_actor: str, second_actor: str) -> List[str]:
        """
        Метод поиска актеров, которые играют с двумя определенными актерами больше двух раз
        :param first_actor: первый актер
        :param second_actor: второй актер
        :return: возвращает список актеров, которые играют вместе с двумя другими
        """

        # Запрос к базе данных, получаем данные про фильмы по именам актеров, которые в них участвуют
        sqlite_query = f"""
        SELECT title, "cast" AS actor, description
        FROM netflix
        WHERE actor LIKE "%{first_actor}%"
        AND actor LIKE "%{second_actor}%"
        """

        films = self.database_connect(sqlite_query)

        # Находим всех актеров, которые участвую в фильмах (могут повторяться)
        actors = list()
        for film in films:
            actors.extend(film[1].split(", "))

        # Пробегаемся по списку актеров, если актер не является актером из данных выше и
        # если актер встречается в списке > 2 раз, то добавляем его в результирующий список
        result = list()
        for actor in actors:
            if actor not in [first_actor, second_actor]:
                if actors.count(actor) > 2:
                    result.append(actor)

        # Делаем список множеством - уникализируем актеров
        result = set(result)

        return list(result)

    def find_movies_by_type_year_and_genre(self, type_movie: str, release_year: int, genre: str) -> List[Dict[str, str]]:
        """
        Метод нахождения кино по типу, году и жанру
        :param type_movie: тип кино
        :param release_year: год релиза
        :param genre: жанр
        :return: возвращает список словарей с атрибутами: title, description, либо же выбрасывает ошибку ValueError
        """

        # Запрос к базе данных, получаем данные про фильмы по типу, дате и жанру
        sqlite_query = f"""
        SELECT title, description
        FROM netflix
        WHERE type = "{type_movie}"
        AND release_year = "{release_year}"
        AND listed_in LIKE "%{genre}%"
        LIMIT 100
        """

        films = self.database_connect(sqlite_query)

        # Проверка на возвращаемы пустой список
        if len(films) != 0:
            json_data = list()
            for film in films:
                json_data.append({
                    "title": film[0],
                    "description": film[1].strip(),
                })
            return json_data
        else:
            raise ValueError("Нет данных в базе!")
