import json
import os
from json import JSONDecodeError
from typing import List, Dict


class BookmarksDAO:
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

    def upload_data_to_file(self, data: Dict[str, str | int | Dict]):
        """
        Метод загрузки данных в файл с обновлением по пути заданному в инициализаторе
        :param data: Данные загружаемые в файл
        :return: ничего не возвращает, либо же выбрасывает ошибку "FileNotFoundError" или "JSONDecodeError"
        """

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                if os.stat(self.file_path).st_size != 0:
                    result = json.load(file)
                    result.append(data)
                else:
                    result = data
        except FileNotFoundError:
            raise FileNotFoundError("Не обнаружен файл с данными, по данному пути!")
        except JSONDecodeError:
            raise JSONDecodeError(msg="Не удается преобразовать JSON в список", doc=f"{self.file_path}", pos=1)

        self.load_data_to_file(result)

    def load_data_to_file(self, result: List[Dict[str, int]]):
        """
        Метод загрузки данных в файл
        :param result:
        """

        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(result, file, ensure_ascii=False)
        except JSONDecodeError:
            raise JSONDecodeError(msg="Не удается преобразовать JSON в список", doc=f"{self.file_path}", pos=1)

    def get_all_bookmarks(self) -> List[Dict[str, str | int | Dict]]:
        """
        Метод получения всех закладок из базы данных
        :return: возвращает закладки
        """

        bookmarks = self.load_data_from_file()
        return bookmarks

    def add_post_to_bookmarks(self, post_id: int) -> None:
        """
        Метод добавления id поста в закладки
        :param post_id: идентификатор поста
        :return: выбрасывает ошибку ValueError или возвращает - None
        """

        bookmarks = self.get_all_bookmarks()

        for bookmark in bookmarks:
            if post_id == bookmark.get("pk"):
                raise ValueError("Закладка уже содержится в бд")

        self.upload_data_to_file({"pk": post_id})

    def del_post_from_bookmarks(self, post_id: int) -> None:
        """
        Метод удаления поста из закладок
        :param post_id: идентификатор поста
        :return: выбрасывает ошибку ValueError или возвращает - None
        """
        bookmarks = self.get_all_bookmarks()

        for count in range(len(bookmarks)):
            if post_id == bookmarks[count].get("pk"):
                bookmarks.pop(count)
                self.load_data_to_file(bookmarks)
                return None

        raise ValueError("Закладка не содержится в бд")
