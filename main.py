import game_func
from config import QUESTIONS_PATH, GAME_STATISTIC_PATH

# Загрузка вопросов по пути QUESTIONS_PATH
data_questions = game_func.load_questions(QUESTIONS_PATH)

# Проверка ввода пользовательского имени
while True:
    user_name = input("Пожалуйста представьтесь: ")
    if user_name != "":
        break
    else:
        print("Повторите попытку!")

# Словарь статистики пользователя
answers = {
    user_name: {
        "points": 0,
        "correct": 0,
        "incorrect": 0,
    },
}

# Подсчет количества доступных вопросов, приглашение пользователя начать игру
count_questions = game_func.count_questions(data_questions)
print(f"{user_name}, добро пожаловать в \"Свою Игру\".")

# Основная логика работы игры. Выход происходит при условии, что на все вопросы пользователь ответил
while count_questions > answers[user_name]["correct"] + answers[user_name]["incorrect"]:
    print(game_func.show_field(data_questions))

    user_choice = input("Выберите категорию: ")

    data_from_input = game_func.parse_input(user_choice, data_questions)

    # Проверка на существование вопроса
    if data_from_input is not None:
        true_answer = data_questions[data_from_input[0]][data_from_input[1]]["answer"]

        print(game_func.show_questions(*data_from_input, data_questions))

        user_choice = input("---> ")

        points = game_func.process_answer(*data_from_input, data_questions, user_choice)

        answers[user_name]["points"] += points

        # Если количество очков > 0, то это правильный ответ
        if points > 0:
            print(f"Правильно это {true_answer}. +{points} баллов. Ваш счет = {answers[user_name]['points']}")

            answers[user_name]["correct"] += 1
        else:
            print(f"Неверно это {true_answer}. {points} баллов. Ваш счет = {answers[user_name]['points']}")

            answers[user_name]["incorrect"] += 1
    else:
        print("Такой категории нет!")

# Сохранение статистики пользователя в файл, вывод результатов игры
game_func.save_result_to_file(GAME_STATISTIC_PATH, answers)
print(f"\nВопросы закончились!\n{game_func.show_stats(answers)}")
