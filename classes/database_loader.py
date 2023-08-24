import os
import json
from json import JSONDecodeError

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

    def load_data_from_file(self):
        """
        Функция загрузки данных из файла JSON
        :return: возвращает словарь данных или None - если такого файла не существует
        """

        try:
            with open(self.file_path, "rt", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("Не обнаружен файл с данными, по данному пути!")

        # if os.path.exists(self.file_path):
        #     with open(self.file_path, "rt", encoding="utf-8") as file:
        #         return json.load(file)
        # else:
        #     return None

    def upload_data_to_file(self, data):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                if os.stat(self.file_path).st_size != 0:
                    result = json.load(file)
                    result.append(data)
                else:
                    result = data
        except FileNotFoundError:
            raise FileNotFoundError("Не обнаружен файл с данными, по данному пути!")

        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(result, file, ensure_ascii=False)
        except JSONDecodeError:
            raise JSONDecodeError



        # if os.path.exists(self.file_path):
        #     with open(self.file_path, "r", encoding="utf-8") as file:
        #         if os.stat(self.file_path).st_size != 0:
        #             result = json.load(file)
        #             result.append(data)
        #         else:
        #             result = data
        #
        # with open(self.file_path, "w", encoding="utf-8") as file:
        #     json.dump(result, file, ensure_ascii=False)
