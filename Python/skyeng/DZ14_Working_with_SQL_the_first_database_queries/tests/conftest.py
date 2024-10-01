import pytest
from main import app
from app.movie.dao.movie_dao import MovieDAO

@pytest.fixture()
def get_movies_dao():
    movies_dao = MovieDAO(app.config.get("NETFLIX_DB_PATH"))
    return movies_dao
