import os
import json
from typing import Union, List, Dict


class DatabaseLoader:
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

    def load_data_from_file(self) -> Union[List[Dict[str, str | int]], None]:
        """
        Функция загрузки данных из файла JSON
        :return: возвращает словарь данных или None - если такого файла не существует
        """

        if os.path.exists(self.file_path):
            with open(self.file_path, "rt", encoding="utf-8") as file:
                return json.load(file)
        else:
            return None
