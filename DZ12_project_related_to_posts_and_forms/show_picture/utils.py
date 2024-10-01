import os
from typing import List, Dict


def get_posts_on_request(key_post: str, data_from_base: List[Dict[str, str | int | Dict]]) -> List[
    List[Dict[str, str | int | Dict] | bool]]:
    """
    Функция получения поста из базы данных по запросу пользователя
    :param key_post: ключ-запрос
    :param data_from_base: данные из базы
    :return: возвращает все посты найденные по такому запросу
    """

    posts = list()

    for post_info in data_from_base:
        if post_info.get('content').lower().find(key_post.lower()) != -1:
            if os.path.exists(post_info.get('pic')):
                posts.append([post_info, True])
            else:
                posts.append([post_info, False])
    return posts
