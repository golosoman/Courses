import pytest

keys_should_be_by_posts = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


class TestPostsDAO:

    def test_get_posts_all_on_len(self, get_posts):
        posts = get_posts.get_posts_all()
        assert len(posts) > 0, "Возвращается пустой список"

    def test_get_posts_all_on_type(self, get_posts):
        posts = get_posts.get_posts_all()
        assert type(posts) == list, "Возвращается не список"

    def test_get_posts_all_on_key(self, get_posts):
        posts = get_posts.get_posts_all()
        assert set(posts[0].keys()) == keys_should_be_by_posts, "Возвращаются неверные ключи"

    def test_get_posts_by_user_by_ValueError(self, get_posts):
        with pytest.raises(ValueError):
            assert get_posts.get_posts_by_user(None)

    @pytest.mark.parametrize("current_value, expected_value", [
        (0, False),
    ])
    def test_post_exist_by_id(self, get_posts, current_value, expected_value):
        assert get_posts.post_exist_by_id(current_value) == expected_value, "Неверное значение"

    def test_search_for_posts(self):
        pass

    def test_get_post_by_pk(self, get_posts):
        assert get_posts.get_post_by_pk(1) == get_posts.get_posts_all()[0], "Найден не тот пост"

