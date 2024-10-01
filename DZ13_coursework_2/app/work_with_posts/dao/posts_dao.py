import json
import os
import re
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

    def get_posts_all(self) -> List[Dict[str, str | int | Dict]]:
        """
        Метод получения постов из БД
        :return: посты
        """

        posts = self.load_data_from_file()

        for post in posts:
            post_content = post.get("content")
            if "#" in post_content:
                result = re.sub(r'#(\w+)', r'<a href="/tag/\1">#\1<a>', post_content)
                post["content"] = result

        return posts

    def get_posts_by_user(self, user_name: str) -> List[Dict[str, str | int | Dict]]:
        """
        Метод получения постов по имени пользователя
        :param user_name: имя пользователя
        :return: список постов для определенного пользователя или ValueError - если поста не существует
        """

        posts = self.get_posts_all()

        user_posts = list()

        for post in posts:
            if post.get("poster_name") == user_name:
                user_posts.append(post)

        if len(user_posts) > 0:
            return user_posts
        else:
            raise ValueError("Такого поста не существует")

    def post_exist_by_id(self, post_id: int) -> True | False:
        """
        Метод проверяющий есть ли пост с таким id в постах
        :param post_id: идентификатор поста
        :return: True - если есть, False - если нет
        """

        posts = self.get_posts_all()

        if 0 < post_id <= len(posts):
            return True
        else:
            return False

    def search_for_posts(self, query: str) -> List[Dict[str, str | int | Dict]]:
        """
        Метод поиска постов по запросу
        :param query: параметр запроса
        :return: возвращает все найденные посты по запросу
        """

        posts = self.get_posts_all()

        posts_by_query = list()

        for post in posts:
            if query.lower() in post.get("content").lower():
                posts_by_query.append(post)

        return posts_by_query

    def get_post_by_pk(self, pk: int) -> Dict[str, str | int | Dict]:
        """
        Метод получения поста по его id
        :param pk: идентификатор поста
        :return: возращает пост
        """

        posts = self.get_posts_all()

        if not self.post_exist_by_id(pk):
            raise ValueError("Такого поста не существует")

        return posts[pk - 1]

    def get_posts_by_tag(self, tag: str) -> List[Dict[str, str | int | Dict]]:
        """
        Метод получения постов по тегу
        :param tag: тег
        :return: возвращает посты
        """
        posts = self.get_posts_all()

        posts_by_tag = list()

        for post in posts:
            tag_list_from_content = re.findall(r'#\w+', post.get("content"))
            if len(tag_list_from_content) != 0:
                if '#' + tag in tag_list_from_content:
                    posts_by_tag.append(post)

        return posts_by_tag
