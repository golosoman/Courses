import validator_library


# Считываем набор данных из data.txt и проверяем их на валидность через Validator_Library
with open("data.txt", "rt", encoding="utf-8") as file:
    for line in file:
        pin, password, mail, name = line.rstrip().split(":")
        print(f"Правильность введенных данных для: {line}"
              f"Пин-код: {validator_library.check_pin(pin)}\n"
              f"Пароль: {validator_library.check_pass(password)}\n"
              f"Почта: {validator_library.check_mail(mail)}\n"
              f"Имя: {validator_library.check_name(name)}\n")
