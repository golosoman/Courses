from classes.class_player import Player
from utils import load_random_word_from_internet
from config import URL_WORDS, WORDS_PATH


# Ввод имени пользователя и получение данных слова и набора слов в JSON
name = input("Введите имя игрока: ")
user = Player(name=name)
basic_word = load_random_word_from_internet(URL_WORDS)

# Приветствие пользователя, приглашение начать игру
print(f"Привет, {user.name}!\n Составьте {basic_word.count_subword()} слов из слова {basic_word.word.upper()}\n"
      f"Слова должны быть не короче 3 букв\nЧтобы закончить игру, угадайте все слова или напишите \"stop\"\n"
      f"Поехали, ваше первое слово?")

# цикл, работающий пока количество угаданных слов не сравнится с количеством слов, которые можно составить
user_choice = ""
while user.count_used_words() != basic_word.count_subword():
    user_choice = input("---> ").lower()

    # Выход из цикла, если использовано ключевое слово "stop"
    if user_choice == "stop":
        break

    # Несколько проверок на правильность введенного пользователем слова
    if len(user_choice) < 3:
        print("Слишком короткое слово!")
    elif not basic_word.check_input_word(input_word=user_choice):
        print("Нет, неверно!")
    elif user.check_word_in_used_words(word=user_choice):
        print("Слово уже использовалось")
    else:
        print("Верно!")
        user.add_word_in_used_words(word=user_choice)

# Вывод результата игры
print(f"Программа завершена, вы угадали {user.count_used_words()} слов из {basic_word.count_subword()}!")
