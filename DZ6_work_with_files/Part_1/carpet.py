def carpet(width, height):
    """
    Функция вывода рисунка ковар
    :param width: ширина ковра
    :param height: высота ковра
    """

    border_line = "▓" + "░" * (width - 2) + "▓"
    middle_line = "▓" + "░" + "▒" * (width - 4) + "░" + "▓"
    print(border_line)
    print((middle_line + "\n") * (height - 2), end="")
    print(border_line)


# Запуск функции вывода ковра
carpet(40, 8)
