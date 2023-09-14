import pytest
from main import app

# Список ключей, которые хранятся в JSON для комментариев
keys_should_be_by_comments = {"post_id", "commenter_name", "comment", "pk"}


class TestCommentsDAO:
    """Класс тестирования класса CommentsDAO"""

    def test_get_posts_all_on_type(self, get_comments):
        """
        Тест get_posts_all на возвращаемый тип - список
        :param get_comments: фикстура, содержащая данные из базы комментариев к постам
        """

        comments = get_comments.get_comments_all()

        assert type(comments) == list, "Возвращается не список"

    def test_get_posts_all_on_len(self, get_comments):
        """
        Тест get_posts_all на возвращаемый пустой список
        :param get_comments: фикстура, содержащая данные из базы комментариев к постам
        """

        comments = get_comments.get_comments_all()

        assert len(comments) > 0, "Возвращается пустой список"

    def test_get_posts_all_on_key(self, get_comments):
        """
        Тест get_posts_all на возвращаемые ключи
        :param get_comments: фикстура, содержащая данные из базы комментариев к постам
        :return:
        """

        comments = get_comments.get_comments_all()

        assert set(comments[0].keys()) == keys_should_be_by_comments, "Возвращаются неверные ключи"

    def test_get_comments_by_post_id_on_ValueError(self, get_comments):
        """
        Тест get_comments_by_post_id на возвращаемую ошибку ValueError
        :param get_comments: фикстура, содержащая данные из базы комментариев к постам
        """

        with pytest.raises(ValueError):
            assert get_comments.get_comments_by_post_id(0, app.config.get("POSTS_DATA_PATH"))
