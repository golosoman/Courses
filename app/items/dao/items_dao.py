import os
import sqlite3
from typing import List, Dict, Tuple


class ItemsDAO:
    """Класс для работы с данными из БД - animals"""

    def __init__(self, path: str):
        """
        Инициализатор класса работы с данными - кино
        :param path: путь к БД
        """

        self.file_path = path

    def __repr__(self):
        """
        Представление для объектов класса
        :return: возвращает путь и его состояние
        """
        return f"Загрузчик Баз Данных по пути: {self.file_path} - {os.path.exists(self.file_path)}"

    def database_connect(self, query: str) -> List[Tuple[str | int]]:
        """
        Метод подключения к базе данных по запросу query
        :param query: запрос к БД
        :return: возвращает список кортежей с данными
        """
        with sqlite3.connect(self.file_path) as connect:
            cursor = connect.cursor()
            cursor.execute(query)
            return cursor.fetchall()

    def database_connect_with_values(self, query: str, values: Tuple[str | int]) -> List[Tuple[str | int]]:
        """
        Метод подключения к базе данных по запросу query и добавлению параметров values
        :param query: запрос к БД
        :param values: кортеж применяемых значений в запросе
        :return: возвращает список кортежей с данными
        """
        with sqlite3.connect(self.file_path) as connect:
            cursor = connect.cursor()
            cursor.execute(query, values)
            return cursor.fetchall()

    def create_and_insert_data_in_db(self):
        """
        Метод создание таблиц в БД и заполнения их
        """
        query = """
        CREATE TABLE IF NOT EXISTS colors(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            color VARCHAR(50)
        );
        """
        self.database_connect(query)
        query = """
                INSERT INTO colors (color)
                SELECT DISTINCT * FROM(
                    SELECT DISTINCT
                    color1 AS color
                    FROM animals
                    UNION ALL
                    SELECT DISTINCT
                        color2 AS color
                    FROM animals
                )
                 WHERE color IS NOT NULL;
                """
        self.database_connect(query)
        query = """
                CREATE TABLE IF NOT EXISTS outcome(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                subtype VARCHAR(50),
                "type" VARCHAR(50),
                "month" VARCHAR(50),
                "year" VARCHAR(50)
                );
                """
        self.database_connect(query)
        query = """
                CREATE TABLE animal_type(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                animal_type VARCHAR(50)
                );
                """
        self.database_connect(query)
        query = """
                INSERT INTO animal_type(animal_type)
                SELECT DISTINCT animal_type
                FROM animals;
                """
        self.database_connect(query)
        query = """
                CREATE TABLE animal_breed(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                breed VARCHAR(50)
                );
                """
        self.database_connect(query)
        query = """
                INSERT INTO animal_breed(breed)
                SELECT DISTINCT breed
                FROM animals;
                """
        self.database_connect(query)
        query = """
                CREATE TABLE IF NOT EXISTS animals_final(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                age_upon_outcome VARCHAR(50),
                animal_id VARCHAR(50),
                animal_type_id INTEGER,
                name VARCHAR(50),
                breed_id INTEGER,
                date_of_birth VARCHAR(50),
                outcome_id INTEGER,
                FOREIGN KEY (outcome_id) REFERENCES outcome(id),
                FOREIGN KEY (animal_type_id) REFERENCES animal_type(id),
                FOREIGN KEY (breed_id) REFERENCES animal_breed(id)
                );
                """
        self.database_connect(query)
        query = """
                INSERT INTO outcome(subtype, "type", "month", "year")
                SELECT DISTINCT
                    animals.outcome_subtype,
                    animals.outcome_type,
                    animals.outcome_month,
                    animals.outcome_year
                FROM animals;
                """
        self.database_connect(query)
        query = """
                INSERT INTO animals_final(
                age_upon_outcome,
                animal_id,
                animal_type_id,
                name,
                breed_id,
                date_of_birth,
                outcome_id)
                SELECT
                    animals.age_upon_outcome,
                    animals.animal_id,
                    animals.animal_type,
                    animals.name,
                    animals.breed,
                    animals.date_of_birth,
                    outcome.id
                FROM animals
                INNER JOIN outcome
                ON outcome.subtype = animals.outcome_subtype
                AND outcome."type" = animals.outcome_type
                AND outcome."month" = animals.outcome_month
                AND outcome."year" = animals.outcome_year;
                """
        self.database_connect(query)
        query = """
                CREATE TABLE IF NOT EXISTS animals_colors(
                animals_id INTEGER,
                colors_id INTEGER,
                FOREIGN KEY (animals_id) REFERENCES animals_final(id),
                FOREIGN KEY (colors_id) REFERENCES colors(id)
                );
                """
        self.database_connect(query)
        query = """
                INSERT INTO animals_colors (animals_id, colors_id)
                SELECT DISTINCT animals_final.id, colors.id
                FROM animals
                    JOIN colors ON colors.color = animals.color1
                    JOIN animals_final ON animals_final.animal_id = animals.animal_id
                UNION ALL
                SELECT DISTINCT animals_final.id, colors.id
                FROM animals
                    JOIN colors ON colors.color = animals.color2
                    JOIN animals_final ON animals_final.animal_id = animals.animal_id;
                """
        self.database_connect(query)

    def get_animal_data(self, id: int) -> List[Tuple[str | int]]:
        """
        Метод получения данных о животном по его id из таблицы animals_final
        :param id: идентификатор животного
        :return: возвращает список кортежей с данными о животном
        """
        query = """
        SELECT animals_final.name, animals_final.animal_type_id, animals_final.breed_id
        FROM animals_final
        WHERE animals_final.id = ?
        """
        return self.database_connect_with_values(query, (id,))
