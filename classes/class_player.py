class Player:
    def __init__(self, name):
        """
        Инициализатор
        :param name: имя пользователя
        """

        self.name = name
        self.used_words = list()

    def __repr__(self):
        """
        Метод вывода наглядного представления данных класса
        :return: выводит строку с имененм пользователя и использованными словами
        """

        return f'Пользователь: {self.name}. Использованные слова: {self.used_words}'

    def count_used_words(self):
        """
        Метод подсчета количества использованных слов
        :return: возвращает число слов int
        """

        return len(self.used_words)

    def add_word_in_used_words(self, word):
        """
        Метод добавления слова в использованные слова
        :param word: слово, которое хотим добавить
        """

        self.used_words.append(word)

    def check_word_in_used_words(self, word):
        """
        Метод проверки использования данного слова ранее
        :param word: проверяемое слово
        :return: возвращает True, если ранее использовалось, иначе - False
        """

        return word in self.used_words
