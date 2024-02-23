# для увеличения глубины рекурсии
from sys import setrecursionlimit
import time

def fact_it(n : int) -> int:
    """Итерационная функция вычисления факториала"""
    res = 1

    for i in range(2, n + 1):
        res *= i
    
    return res

def fact_rec(n : int) -> int:
    """Рекурсивная функция вычисления факториала"""
    return 1 if n == 1 else fact_rec(n - 1) * n

setrecursionlimit(10**5 + 1)

if __name__ == "__main__":
    n = int(input("Укажите число (от 1 до 10^5) для вычисления факториала: "))

    it_start_time = time.time()
    n_fact_it = fact_it(n)
    it_finish_time = time.time()
    it_time = int((it_finish_time - it_start_time) * 1_000)

    rec_start_time = time.time()
    n_fact_rec = fact_rec(n)
    rec_finish_time = time.time()
    rec_time = int((rec_finish_time - rec_start_time) * 1_000)

    print("Результаты:")

    print("Итерационная функция:")
    try:
        print(f"{n}! = {n_fact_it}")
    except ValueError:
        print("Слишком большое число")
    print(f"Время вычисления: {it_time} мс")

    print("\nИтерационная функция:")
    try:
        print(f"{n}! = {n_fact_rec}")
    except ValueError:
        print("Слишком большое число")
    print(f"Время вычисления: {rec_time} мс")

    abs_time_diff = abs(it_time - rec_time)
    if (abs_time_diff > 0):
        rel_time_diff = round(abs_time_diff / (rec_time + it_time) * 200, 2)
    else:
        rel_time_diff = 0
    print(f"\nРазница во времени: {abs_time_diff} мс ({abs(rel_time_diff)}%)")