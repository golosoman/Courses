from typing import Tuple, List, Dict

from Part_2.classes.database_loader import DatabaseLoader


class Candidates:
    def __init__(self, path: str) -> None:
        """
        Инициализатор класса кандидатов
        :param path: путь к базе данных с кандидатами
        """

        self.candidates = dict()

        data = DatabaseLoader(path).load_data_from_file()

        for candidate in data:
            self.candidates[candidate.get('id')] = candidate

    def __repr__(self) -> str:
        """
        Метод вывода информации о кандидатах
        :return: выводит словарь кандидатов по id
        """

        return f"Кандидаты: {self.candidates}"

    def get_list_candidates(self) -> List[Dict[str, str | int]]:
        candidates = list()
        for candidate_id in range(self.get_count_candidates()):
            candidates.append(self.get_candidate_by_id(candidate_id + 1))
        return candidates

    def get_candidate_by_id(self, candidate_id: int) -> Dict[str, str | int]:
        """
        Метод получения данных о кандидате по его id
        :param candidate_id: id кандидата
        :return: возвращает информацию о кандидате - словарь
        """

        return self.candidates.get(candidate_id)

    def get_info(self, candidate_id: int) -> Tuple[str, str, str]:
        """
        Метод получения информации о кандидате
        :param candidate_id: id кандидата
        :return: возвращает имя, должность и навыки кандидата в str
        """

        name = self.get_name(candidate_id).title()
        position = self.get_position(candidate_id)
        skills = self.get_skills(candidate_id)

        return name, position, skills

    def get_info_with_photo(self, candidate_id: int) -> Tuple[str, str, str, str]:
        """
        Метод получения информации о кандидате с фото
        :param candidate_id: id кандидата
        :return: возвращает фото, имя, должность и навыки кандидата в str
        """

        photo = self.get_photo(candidate_id)

        name, position, skills = self.get_info(candidate_id)

        return photo, name, position, skills

    def get_name(self, candidate_id: int) -> str:
        """
        Метод получения имени кандидата
        :param candidate_id:
        :return: id кандидата str
        """

        candidate = self.get_candidate_by_id(candidate_id)

        return candidate.get("name").lower()

    def get_position(self, candidate_id: int) -> str:
        """
        Метод получения должности кандидата
        :param candidate_id: id кандидата
        :return: возвращает должность кандидата str
        """

        candidate = self.get_candidate_by_id(candidate_id)

        return candidate.get("position").lower()

    def get_skills(self, candidate_id: int) -> str:
        """
        Метод получения навыков кандидата
        :param candidate_id: id кандидата
        :return: возвращает навыки кандидата str
        """

        candidate = self.get_candidate_by_id(candidate_id)

        return candidate.get("skills").lower()

    def get_photo(self, candidate_id: int) -> str:
        """
        Метод получения фотографии кандидата
        :param candidate_id: id кандидата
        :return: возвращает ссылку на фото str
        """

        candidate = self.get_candidate_by_id(candidate_id)

        return candidate.get("picture").lower()

    def get_count_candidates(self) -> int:
        """
        Метод получения количества кандидатов в базе
        :return: возвращает количество кандидатов int
        """

        return len(self.candidates)

    def get_candidates_by_name(self, candidate_name: str) -> List[Dict[str, str | int]]:
        """
        Метод получения кандидатов по имени
        :param candidate_name: имя кандидата
        :return: возвращает кандидатов с именем "candidate_name"
        """

        candidates = list()

        for candidate_id in range(self.get_count_candidates()):
            candidate_name_in_data = self.get_name(candidate_id + 1).split(' ')[0]
            if candidate_name_in_data == candidate_name.lower():
                candidates.append(self.get_candidate_by_id(candidate_id + 1))

        return candidates

    def get_candidates_by_skill(self, skill: str) -> List[Dict[str, str | int]]:
        """
        Метод получения кандидатов по навыку
        :param skill: название навыка
        :return: возвращает кандидатов, имеющих навык "skill"
        """

        candidates = list()

        for candidate_id in range(self.get_count_candidates()):
            candidate_skills = self.get_skills(candidate_id + 1).split(", ")
            if skill.lower() in candidate_skills:
                candidates.append(self.get_candidate_by_id(candidate_id + 1))

        return candidates

    def get_all_candidates(self) -> List[Dict[str, str | int]]:
        """
        Метод получения всех кандидатов
        :return: возвращает всех кандидатов
        """

        candidates = list()

        for id_candidate in self.candidates:
            candidates.append(self.candidates[id_candidate])

        return candidates
