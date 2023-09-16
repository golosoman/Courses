from flask import Blueprint, jsonify
from app.movie.dao.movie_dao import MovieDAO
from config import NETFLIX_DB_PATH

# Создание блупринта для прохода по маршруту movies
movie_blueprint = Blueprint("movie_blueprint", __name__, template_folder="templates")

# Объект класса работы с БД по поиску фильмов
movies_dao = MovieDAO(NETFLIX_DB_PATH)

# Функция загрузки страницы c json по названию фильма
@movie_blueprint.route("/movie/<title>")
def movie_title_page(title):
    movie = movies_dao.find_movie_by_title(title)
    return jsonify(movie)


@movie_blueprint.route("/movie/<first_year>/to/<second_year>")
def movie_year_to_year_page(first_year, second_year):
    movies = movies_dao.find_movies_by_year_to_year(first_year, second_year)
    return jsonify(movies)

@movie_blueprint.route("/rating/<value_rating>")
def movie_by_rating_page(value_rating):
    movies = movies_dao.find_movies_by_rating(value_rating)
    return jsonify(movies)