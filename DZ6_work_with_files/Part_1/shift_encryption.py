def shift_encode(sentence):
    """
    Функция кодирования предложения, со сдвигом на 1 букву
    :param sentence: искомое предложение
    :return: возвращает зашифрованное предложение
    """

    encode_sentence = ""

    for char in sentence:
        if ord('а') <= ord(char.lower()) <= ord('я'):
            if ord(char.lower()) != ord('я'):
                encode_sentence += chr(ord(char) + 1)
            else:
                encode_sentence += chr(ord(char) - (ord('я') - ord('а')))
        else:
            encode_sentence += char

    return encode_sentence


def shift_decode(sentence):
    """
    Функция декодирования предложения со сдвигом на 1 букву
    :param sentence: искомое зашифрованное предложение
    :return: расшифрованное предложение
    """

    decode_sentence = ""

    for char in sentence:
        if ord('а') <= ord(char.lower()) <= ord('я'):
            if ord(char.lower()) != ord('а'):
                decode_sentence += chr(ord(char) - 1)
            else:
                decode_sentence += chr(ord(char) + (ord('я') - ord('а')))
        else:
            decode_sentence += char

    return decode_sentence


# Строка для шифрования
string = "Будешь трудиться - будет у тебя и хлеб, и молоко водиться."

# Закодированная и раскодированная строки
encode_string = shift_encode(string)
decode_string = shift_decode(encode_string)

# Вывод результата работы функция shift_encode и shift_decode
print(encode_string)
print(decode_string)
