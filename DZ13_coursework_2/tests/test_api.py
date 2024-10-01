from main import app

# Список ключей, которые хранятся в JSON
keys_should_be_posts = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


class TestApi:
    """Класс тестирования класса API"""

    def test_get_posts_page_json_on_list(self):
        """
        Тест get_post_page API постов на возвращаемый тип - список
        """

        response = app.test_client().get("/api/posts")

        assert type(response.json) == list, "Возвращается не список"

    def test_get_posts_page_json_by_keys(self):
        """
        Тест get_post_page API постов на возвращаемый список ключей
        """

        response = app.test_client().get("/api/posts")

        assert set(response.json[0].keys()) == keys_should_be_posts

    def test_get_post_page_json_by_post_id_on_list(self):
        """
        Тест get_post_page API поста на возвращаемый тип - словарь
        """

        response = app.test_client().get("/api/posts/1")

        assert type(response.json) == dict, "Возвращается не словарь"

    def test_get_post_page_json_by_post_id_by_keys(self):
        """
        Тест get_post_page API поста на возвращаемый список ключей
        """

        response = app.test_client().get("/api/posts/1")

        assert set(response.json.keys()) == keys_should_be_posts
