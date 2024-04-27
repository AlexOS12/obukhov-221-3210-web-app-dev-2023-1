def check_pass(password : str) -> tuple[bool, str]:
    if not 8 <= len(password) <= 128 : 
        return tuple([False, "Пароль должен содержать от 8 до 128 символов"])

    lowcase_letters = 0
    upcase_letters = 0
    spec_chars = 0
    digits = 0

    for char in password:
        ord_char = ord(char)
        if 97 <= ord_char <= 122 or 1072 <= ord_char <= 1103 or ord_char == 1105:
            lowcase_letters += 1
        elif 65 <= ord_char <= 90 or 1040 <= ord_char <= 1071 or ord_char == 1025:
            upcase_letters += 1
        elif char in "0123456798":
            digits += 1
        elif char in "~!?@#$%^&*_-+()[]{}/\\|\"'.,:;":
            spec_chars += 1
        else:
            return tuple([False, "В пароле содержатся недопустимые символы"])

    if not lowcase_letters:
        return tuple([False, "Пароль должен содержать хотя бы одну строчную букву"])
    if not upcase_letters:
        return tuple([False, "Пароль должен содержать хотя бы одну заглавную букву"])
    if not spec_chars:
        return tuple([False, "Пароль должен содержать хотя бы один специальный символ"])
    if not digits:
        return tuple([False, "Пароль должен содержать хотя бы одну цифру"])


    return tuple([True, "Пароль соотвествует требованиям"])