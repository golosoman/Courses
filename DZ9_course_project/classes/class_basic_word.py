class BasicWord:
    def __init__(self, word, set_of_words):
        """
        Инициализатор
        :param word: исходное слово
        :param set_of_words: набор допустимых подслов
        """

        self.word = word
        self.set_of_words = set_of_words

    def __repr__(self):
        """
        Метод вывода наглядного представления данных класса
        :return: возвращает строку с текущим словом и набором слов из тех же букв
        """

        return f'Текущее слово: {self.word}. Производный набор слов из тех же букв: {self.set_of_words}'

    def check_input_word(self, input_word):
        """
        Метод проверки введенного слова в списке допустимых подслов
        :param input_word: введенное пользователем слово
        :return: возвращает True, если это подслово, иначе - False
        """

        return input_word in self.set_of_words

    def count_subword(self):
        """
        Метод подсчета количества подслов
        :return: возвращает число подслов int
        """

        return len(self.set_of_words)
