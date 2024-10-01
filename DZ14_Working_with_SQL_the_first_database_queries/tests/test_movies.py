import pytest

# Множество ключей, которые содержатся в БД netflix.db
keys_should_be_by_movies = {"title", "country", "release_year", "genre", "description"}

class TestMovies:
    """Класс тестирования класса MoviesDAO"""

    def test_find_movie_by_title_on_ValueError(self, get_movies_dao):
        """
        Тест на проверку возвращаемой ошибки ValueError в случае отсутствия названия в базе
        :param get_movies_dao: фикстура с данными о фильмах
        """

        with pytest.raises(ValueError):
            assert get_movies_dao.find_movie_by_title(None)

    def test_find_movie_by_title_on_type(self, get_movies_dao):
        """
        Тест на нахождение фильма по названию на возвращаемый тип
        :param get_movies_dao: фикстура с данными о фильмах
        """

        assert type(get_movies_dao.find_movie_by_title("#Roxy")) == dict, "Возвращается не словарь!"

    def test_find_movie_by_title_on_keys(self, get_movies_dao):
        """
        Тест на нахождение фильма по названию на возвращаемый список ключей
        :param get_movies_dao: фикстура с данными о фильмах
        """

        keys = set(get_movies_dao.find_movie_by_title("#Roxy").keys())
        assert keys == keys_should_be_by_movies, "Возвращаются неверные ключи!"
