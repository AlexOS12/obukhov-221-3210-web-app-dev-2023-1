def sum_and_sub(a : float, b : float) -> tuple[float, float]:
    """Принимает два действительных числа
    Возвращает кортеж из суммы и разности этих чисел"""
    return a + b, a - b

if __name__ == "__main__":
    a = float(input("Введите действительное число A: "))
    b = float(input("Введите действительное число B: "))

    sum, sub = sum_and_sub(a, b)
    print(f"{a} + {b} = {sum}")
    print(f"{a} - {b} = {sub}")
    