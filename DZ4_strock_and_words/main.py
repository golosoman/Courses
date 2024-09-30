# Слова по сложности с переводом
dict_easy = {
    "monkey": "обезьяна",
    "dog": "собака",
    "zebra": "зебра",
    "duck": "утка",
    "cow": "корова",
}
dict_medium = {
    "pig": "свинья",
    "turtle": "черепаха",
    "chicken": "курица",
    "bee": "пчела",
    "fish": "рыба",

}
dict_hard = {
    "bird": "птица",
    "ladybug": "божья коровка",
    "octopus": "осьминог",
    "sheep": "овца",
    "whale": "кит",
}

dict_difficulty = {
    "легкий": dict_easy,
    "средний": dict_medium,
    "сложный": dict_hard,
}

# Уровни в зависимости от отгаданных слов
levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Нормально",
    4: "Хорошо",
    5: "Отлично"
}

# Словари: ответы пользователя, результаты отгаданных слов
words = {}
result = {}

# Приглашение пользователя начать игру
while True:
    print("\nДобро пожаловать в игру угадай слово. Пожалуйста, выберите уровень сложности."
          "\nЛегкий, средний, сложный")
    choice = input("---> ")
    if choice.lower() not in dict_difficulty.keys():
        print("Нет такого варианта, повторите попытку!")
    else:
        print("\nНачинаем игру!")
        words = dict_difficulty[choice.lower()]
        break

# Проходим по словарю с ответами, сверяясь с ответами пользователя
for en_word, ru_word in words.items():
    print(f"{en_word.title()}, {len(ru_word)} букв, начинается на {ru_word[0]}...")
    choice = input("---> ")
    if choice.lower() != ru_word:
        print(f"Неверно! {en_word.title()} - это {ru_word}.\n")
        result[en_word] = False
    else:
        print(f"Верно! {en_word.title()} - это {ru_word}.\n")
        result[en_word] = True

# Подведение итогов игры
good_answers = list()
bad_answers = list()
for key in result:
    if result[key]:
        good_answers.append(key)
    else:
        bad_answers.append(key)

print("Правильно отвеченные слова:")
if len(good_answers) == 0:
    print("Пусто")
else:
    print("\n".join(good_answers))
print()

print("Неправильно отвеченные слова:")
if len(bad_answers) == 0:
    print("Пусто")
else:
    print("\n".join(bad_answers))
print()

print(f"Ваш ранг:\n{levels[len(good_answers)]}")
