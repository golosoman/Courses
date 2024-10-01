import json
import os
from json import JSONDecodeError
from typing import List, Dict
from app.work_with_posts.dao.posts_dao import PostsDAO


class CommentsDAO:
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

    def get_comments_all(self) -> List[Dict[str, str | int | Dict]]:
        """
        Метод получения комментариев из БД
        :return: комментарии
        """

        user_comments = self.load_data_from_file()

        return user_comments

    def get_comments_by_post_id(self, post_id: int, path: str) -> List[Dict[str, str | int | Dict]]:
        """
        Метод получения комментариев к посту по его id
        :param post_id: идентификатор поста
        :param path: путь к базе данных с постами
        :return: возвращает комментарии к определенному посту или выбрасывает ошибку ValueError
        """
        posts_data = PostsDAO(path)

        if not posts_data.post_exist_by_id(post_id):
            raise ValueError("Такого поста не существует")

        comments = self.get_comments_all()

        post_comments = list()

        for comment in comments:
            if comment.get("post_id") == post_id:
                post_comments.append(comment)

        return post_comments
