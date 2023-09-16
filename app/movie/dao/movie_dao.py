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

    def find_movies_by_rating(self, rating: str):
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

            film = self.database_connect(sqlite_query)

            # Проверка на возвращаемы пустой список
            if len(film) != 0:
                json_data = list()
                for film in film:
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


