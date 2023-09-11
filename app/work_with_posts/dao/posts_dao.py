import json
import os
from json import JSONDecodeError
from typing import List, Dict


class PostsDAO:
    def __init__(self, file_path: str) -> None:
        """
        Инициализатор загрузчика из баз данных
        :param file_path: значение пути к файлу
        """

        self.file_path = file_path

    def __repr__(self) -> str:
        """
        Метод вывода информации о пути к данным
        :return: возвращает путь и его состояние
        """

        return f"Загрузчик Баз Данных по пути: {self.file_path} - {os.path.exists(self.file_path)}"

    def load_data_from_file(self) -> List[Dict[str, str | int | Dict]]:
        """
        Метод загрузки данных из файла JSON
        :return: возвращает словарь данных или ошибку "FileNotFoundError"
        """

        try:
            with open(self.file_path, "rt", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("Не обнаружен файл с данными, по данному пути!")
        except JSONDecodeError:
            raise JSONDecodeError(msg="Не удается преобразовать JSON в список", doc=f"{self.file_path}", pos=1)

    def get_posts_all(self):
        user_posts = self.load_data_from_file()
        return user_posts

# Нужно придумать как искать всех пользователей!
    def get_posts_by_user(self, user_name: str):
        posts = self.get_posts_all()
        user_posts = list()

        for post in posts:
            if post.get("poster_name") == user_name:
                user_posts.append(post)

        if len(user_posts) > 0:
            return user_posts
        else:
            raise ValueError("Такого поста не существует")

    def post_exist_by_id(self, post_id: int):
        posts = self.get_posts_all()

        if 0 < post_id <= len(posts):
            return True
        else:
            return False

    def search_for_posts(self, query: str):
        posts = self.get_posts_all()
        posts_by_query = list()

        for post in posts:
            if query.lower() in post.get("content").lower():
                posts_by_query.append(post)

        return posts_by_query

    def get_post_by_pk(self, pk):
        posts = self.get_posts_all()

        if not self.post_exist_by_id(pk):
            return ValueError("Такого поста не существует")

        return posts[pk - 1]

p = PostsDAO("../../../data/posts.json")
# posts = p.get_posts_all()
# print(p.get_post_by_pk(1))
#