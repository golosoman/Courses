class Question:
    def __init__(self, question, level, correct_answer):
        """
        Инициализатор
        :param question: строка - вопрос
        :param level: сложность вопроса из 5
        :param correct_answer: правильный ответ на вопрос
        """

        self.question = question

        self.level = level

        self.correct_answer = correct_answer

        self.is_answer = False

        self.user_answer = None

        self.score = self.get_points()

    def __repr__(self):
        """
        Вывод объекта класса
        :return: возвращает строку со всеми полями класса
        """

        return f"Вопрос: {self.question}\nСложность: {self.level}/5\n" \
               f"Верный ответ: {self.correct_answer}\n\nЗадан ли вопрос: {self.is_answer}\n" \
               f"Ответ пользователя:{self.user_answer}\nБаллы за вопрос: {self.score}\n"

    def get_points(self):
        """
        Метод получения количества баллов
        :return: возвращает баллы путем умножения level на 10
        """

        return self.level * 10

    def is_correct(self):
        """
        Метод проверки ответа пользователя на вопрос
        :return: возвращает Ture, если ответ верны, иначе - False
        """

        self.is_answer = True

        if self.user_answer == self.correct_answer:
            return True
        else:
            return False

    def build_questions(self):
        """
        Метод формирования вопроса
        :return: возвращает строку с вопросом и его сложностью
        """

        return f"Вопрос: {self.question}\nСложность: {self.level}/5"

    def build_feedback(self):
        """
        Метод комментария для пользователя при ответе на вопрос
        :return: возвращает строку верно, если верно, иначе - неверно
        """

        if self.is_correct():
            return f"Ответ верный, получено {self.score} баллов\n"
        else:
            return f"Ответ неверный, верный ответ - {self.correct_answer}\n"
