from classes.database_loader import DatabaseLoader


class Candidates:
    def __init__(self, path):
        """
        Инициализатор класса кандидатов
        :param path: путь к базе данных с кандидатами
        """

        self.candidates = dict()

        data = DatabaseLoader(path).load_questions_from_file()

        for candidate in data:
            self.candidates[candidate.get('id')] = candidate

    def __repr__(self):
        """
        Метод вывода информации о кандидатах
        :return: выводит словарь кандидатов по id
        """

        return f"Кандидаты: {self.candidates}"

    def get_candidate_by_id(self, candidate_id):
        """
        Метод получения данных о кандидате по его id
        :param candidate_id: id кандидата
        :return: возвращает информацию о кандидате - словарь
        """

        return self.candidates.get(candidate_id)

    def get_info(self, candidate_id):
        """
        Метод получения информации о кандидате
        :param candidate_id: id кандидата
        :return: возвращает имя, должность и навыки кандидата в str
        """

        name = self.get_name(candidate_id)
        position = self.get_position(candidate_id)
        skills = self.get_skills(candidate_id)

        return name, position, skills

    def get_info_with_photo(self, candidate_id):
        """
        Метод получения информации о кандидате с фото
        :param candidate_id: id кандидата
        :return: возвращает фото, имя, должность и навыки кандидата в str
        """

        photo = self.get_photo(candidate_id)
        name = self.get_name(candidate_id)
        position = self.get_position(candidate_id)
        skills = self.get_skills(candidate_id)

        return photo, name, position, skills

    def get_name(self, candidate_id):
        """
        Метод получения имени кандидата
        :param candidate_id:
        :return: id кандидата str
        """

        candidate = self.get_candidate_by_id(candidate_id)

        return candidate.get("name")

    def get_position(self, candidate_id):
        """
        Метод получения должности кандидата
        :param candidate_id: id кандидата
        :return: возвращает должность кандидата str
        """

        candidate = self.get_candidate_by_id(candidate_id)

        return candidate.get("position")

    def get_skills(self, candidate_id):
        """
        Метод получения навыков кандидата
        :param candidate_id: id кандидата
        :return: возвращает навыки кандидата str
        """

        candidate = self.get_candidate_by_id(candidate_id)

        return candidate.get("skills")

    def get_photo(self, candidate_id):
        """
        Метод получения фотографии кандидата
        :param candidate_id: id кандидата
        :return: возвращает ссылку на фото str
        """

        candidate = self.get_candidate_by_id(candidate_id)

        return candidate.get("picture")

    def get_count_candidates(self):
        """
        Метод получения количества кандидатов в базе
        :return: возвращает количество кандидатов int
        """

        return len(self.candidates)
