# Приветствие пользователя
print("Привет! Предлагаю тебе проверить твои знания английского.")
print("Наберите 'ready', чтобы начать!")
state = input("---> ")

# Проверка на готовность приступить к игре
if state != "ready":
    print("Кажется, вы не хотите играть. Очень жаль.")
else:
    # "База данных"
    count_answers = 0
    scores = 0
    questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
    answers = ["is", "am", "in"]

    # Проход по вопросам
    for count in range(len(questions)):
        for attempt in range(1, 4):
            print(questions[count])
            answer = input("---> ")
            if answer == answers[count]:
                print("Ответ верный!\n")
                count_answers += 1
                scores += 4 - attempt
                break
            elif attempt != 3:
                print(f"Неправильно! Осталось попыток: {3 - attempt}\n")
            else:
                print(f"Увы, но нет. Правильный ответ: {answers[count]}\n")

    # Подведение итогов
    print(f"Вот и все! Вы ответили на {count_answers} вопросов из {len(questions)} верно, "
          f"вы набрали {scores} баллов из {len(questions) * 3}")
