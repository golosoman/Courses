DICT_ERRORS = {
    "out": "Вы вышли из системы",
    "no-access": "У вас нет доступа в этот раздел",
    "unknown": "Неизвестная ошибка",
    "timeout": "Система долго не отвечает",
    "robot": "Ваши действия похожи на робота",
}


def get_errors(*en_errors):
    """
    Функция получения ошибок
    :param en_errors: набор ошибок на английском
    :return: возвращает набор ошибок списком
    """

    ru_errors = list()

    for error in en_errors:
        if error not in DICT_ERRORS:
            ru_errors.append("Неизвестная ошибка")
        else:
            ru_errors.append(DICT_ERRORS[error])

    return ru_errors


# Пользовательский ввод набора ошибок
errors = input("Введите набор ошибок через пробел: ").split(" ")

# Вывод набора ошибок
print(get_errors(*errors))
