import os
import json


class DatabaseLoader:
    def __init__(self, file_path):
        """
        Инициализатор загрузчика из баз данных
        :param file_path: значение пути к файлу
        """

        self.file_path = file_path

    def __repr__(self):
        """
        Метод вывода информации о пути к данным
        :return: возвращает путь и его состояние
        """

        return f"Загрузчик Баз Данных по пути: {self.file_path} - {os.path.exists(self.file_path)}"

    def load_data_from_file(self):
        """
        Функция загрузки данных из файла JSON
        :return: возвращает словарь данных или None - если такого файла не существует
        """

        if os.path.exists(self.file_path):
            with open(self.file_path, "rt", encoding="utf-8") as file:
                return json.load(file)
        else:
            return None
