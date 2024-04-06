def checkPhone(phone: str) -> str:
    """Проверяет номер телефона.\n
    Возвращает True, если длина номера 10 или 11 символов (при начале с +7) и
    если номер телефона состоит только из цифр.
    Возвращает пустую строку, если номер верный, иначе возвращает строку с описанием
    ошибки"""

    for char in "()-.":
        phone = phone.replace(char, "")

    if phone.startswith("+7"):
        print("PW-12")
        phone = phone[2:]
    elif phone.startswith("8"):
        print("PW-15")
        phone = phone[1:]

    if len(phone) != 10:
        return "Неверная длина номера телефона!"

    for char in phone:
        if char not in "0123456798":
            return "В номере содержатся недопустимые символы"

    return ""


def formatPhone(phone: str) -> str:
    """Принимает заранее проверенный номер телефона.
    Возвращает номер телефона, отформатированный под вид:
    8-***-***-**-**"""

    for char in "()-.":
        phone = phone.replace(char, "")

    if phone.startswith("+7"):
        print("PW-12")
        phone = phone[2:]
    elif phone.startswith("8"):
        print("PW-15")
        phone = phone[1:]

    return f"8-{phone[:3]}-{phone[3:6]}-{phone[6:8]}-{phone[8:10]}"
