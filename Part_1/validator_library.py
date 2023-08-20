import re


def check_pin(pin):
    """
    Функция проверки формата пин-кода
    :param pin: входной пин-код
    :return: возвращает True, если верно, False - иначе
    """

    if re.fullmatch(r'\d{4}', pin):
        if pin != "1234" and (pin[0] != pin[1] or pin[1] != pin[2] or pin[2] != pin[3]):
            return True
    return False


def check_pass(password):
    """
    Функция проверки формата пароля
    :param password: входной пароль
    :return: возвращает True, если верно, False - иначе
    """

    if re.fullmatch(r'[0-9A-Za-z]{8,}', password):
        return True
    else:
        return False


def check_mail(address):
    """
    Функция проверки формата адреса почты
    :param address: входной адрес
    :return: возвращает True, если верно, False - иначе
    """

    if re.fullmatch(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', address):
        return True
    else:
        return False


def check_name(name):
    """
    Функция проверки формата имени
    :param name: входное имя
    :return: возвращает True, если верно, False - иначе
    """

    if re.fullmatch(r'[А-Яа-я]+[]*[А-Яа-я]*', name):
        return True
    else:
        return False
