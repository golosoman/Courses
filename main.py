import random


def morse_encode(sentence):
    """Кодирует предложение в алфавит азбуки Морзе"""

    alf_morze = {
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "!": "-.-.--",
        "-": "-....-",
        "/": "-..-.",
        "@": ".--.-.",
        "(": "-.--.",
        ")": "-.--.-"
    }
    l_morze_words = list()

    l_words = sentence.split(" ")
    for word in l_words:
        code_word = ""
        for letter in word.lower():
            code_word += alf_morze.get(letter, "")
        l_morze_words.append(code_word)

    return " ".join(l_morze_words)


def get_sentence():
    """Возвращает предложение из списка подготовленных слов"""

    l_fraze = [
        "Code", "Bit", "List", "Soul", "Next", "I am a coder", "I have a car",
        "Giv me please one paper", "I code for 2 hours everyday"
    ]

    return random.choice(l_fraze)


def print_statistics(statistics):
    """Выводит на экран небольшую статистику"""

    bad_statistics = 0
    good_statistics = 0

    for value in statistics:
        if statistics[value]:
            good_statistics += 1
        else:
            bad_statistics += 1

    print(f"\nВсего задачек: {len(statistics)}\nОтвечено верно: {good_statistics}\n"
          f"Отвечено неверно:{bad_statistics}\n")


# Словарик ответов пользователя
answers = dict()

# Приглашение пользователя начать работу программы
print("Сегодня мы потренируемся расшифровывать морзянку.")
while True:
    print("Нажмите Enter и начинаем.")
    choice = input("---> ")
    if choice != "":
        print("Повторяю, нажмите Enter\n")
    else:
        print("\nНачали!")
        break

# Перебор закодированных предложений и предложение их расшифровать
for count in range(3):
    # Участок кода необходимый для отбора уникальных предложений из списка
    while True:
        sentence = get_sentence()
        if sentence not in answers:
            break

    morze_sentence = morse_encode(sentence)

    print(f"Слово {count + 1} {morze_sentence}")
    answer = input("---> ")

    if answer.lower() == sentence.lower():
        print(f"Верно, {sentence}!")
        answers[sentence] = True
    else:
        print(f"Неверно, {sentence}!")
        answers[sentence] = False

    print()

# Вывод статистики ответов пользователя
print_statistics(answers)
