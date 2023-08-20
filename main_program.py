# Приветствие пользователя
print("Привет! Предлагаю тебе проверить твои знания английского.")
print("Расскажи, как тебя зовут?")
name = input("---> ")
print(f"Привет, {name}. Давай начнем тренировку!")
count_answers = 0

# Первый вопрос
print("My name ___ Vova")
answer = input("--->")
if answer == "is":
    print("Правильный ответ! Вы получили 10 баллов!")
    count_answers += 1
else:
    print("Неверно! Правильно: My name is Vova")

# Второй вопрос
print("I ___ a coder")
answer = input("--->")
if answer == "am":
    print("Правильный ответ! Вы получили 10 баллов!")
    count_answers += 1
else:
    print("Неверно! Правильно: I am a coder")

# Третий вопрос
print("I live ___ Moscow")
answer = input("--->")
if answer == "in":
    print("Правильный ответ! Вы получили 10 баллов!")
    count_answers += 1
else:
    print("Неверно! Правильный ответ: I live in Moscow")

# Подведение итогов
print(f"Вот и все, {name}! Вы ответили на {count_answers} вопросов из 3")
print(f"Вы заработали {count_answers * 10} баллов. Это {round(100 * count_answers / 3, 2)} %")
