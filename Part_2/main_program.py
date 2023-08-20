import program_functions
from config import QUESTION_PATH, GAME_STATISTIC_PATH

# Подгружаем данные из файла JSON и формируем список вопросов
data_from_file = program_functions.load_questions_from_file(QUESTION_PATH)
questions = program_functions.get_questions(data_from_file)

# Приветствуем пользователя
name = input("Добро пожаловать в игру с ответами на вопросы, пожалуйста, представьтесь: ")
print("\nИгра начинается!")

# Словарь словарей - статистика игры для пользователя
user_statistic = {
    name: {
        "score": 0,
        "correct_answers": 0,
        "incorrect_answers": 0
    }
}

# Перебираем все вопросы из списка
for question in questions:
    print(question.build_questions())

    question.user_answer = input("Ответ: ").capitalize()

    # Если ответ на вопрос верный, но увеличиваем счет и кол-во правильных ответов,
    # иначе только увеличиваем количество неправильных ответов
    if question.is_correct():
        user_statistic[name]["score"] += question.score
        user_statistic[name]["correct_answers"] += 1
    else:
        user_statistic[name]["incorrect_answers"] += 1

    print(question.build_feedback())

# Выводим статистику текущей игры и сохраняем данные статистики в файл JSON
print("Вот и все!")
program_functions.save_result_to_file(GAME_STATISTIC_PATH, user_statistic)
print(program_functions.show_stats(user_statistic))
