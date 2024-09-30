import random
from config import WORDS_PATH, HISTORY_PATH
from utils import read_data, write_rating, print_statistic, shuffle_word

# Входные данные
record = 0
words = read_data(WORDS_PATH)
random.shuffle(words)

# Знакомство с пользователем
name = input("Здравствуйте, введите имя: ")

# Обход 10 слов из файла, пользователь отгадывает перевернутые слова
for i in range(10):
    orig_word = words[i]
    mix_word = shuffle_word(orig_word)
    print(f"Угадайте слово: {''.join(mix_word)}")
    answer = input("---> ")
    if answer == orig_word:
        print("Верно! Вы получаете 10 баллов.")
        record += 10
    else:
        print(f"Неверно! Верный ответ - {orig_word}")

# Запись в рейтинг, вывод статистики
write_rating(name, record, HISTORY_PATH)
state = print_statistic(HISTORY_PATH)
print(f"Всего игр сыграно: {state.get('games_played')}\n"
      f"Максимальный рекорд: {state.get('max_score')}")
