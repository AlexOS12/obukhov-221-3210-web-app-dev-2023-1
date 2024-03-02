from time import time

def process_list(arr):
    result = []
    for i in arr:
        if i % 2 == 0:
            result.append(i**2)
        else:
            result.append(i**3)
    return result

def process_list_comp(arr : list) -> list:
    return [i ** 3 if i & 1 else i ** 2 for i in arr]

def process_list_gen(arr : list):
    for i in arr:
        yield i ** 3 if i & 1 else i ** 2

if __name__ == "__main__":
    arr_len = int(input("Укажите длину списка: "))
    arr = [i for i in range(1, arr_len + 1)]
    print("Список сгенерирован")

    std_start_time = time()
    processed_list = process_list(arr)
    std_finish_time = time()
    std_time = (std_finish_time - std_start_time) * 1_000
    
    comp_start_time = time()
    processed_list = process_list_comp(arr)
    comp_finish_time = time()
    comp_time = (comp_finish_time - comp_start_time) * 1_000

    gen_start_time = time()
    processed_list_gen = process_list_gen(arr)
    gen_finish_time = time()
    gen_time = (gen_finish_time - gen_start_time) * 1_000

    print("Результаты:")

    print("Оригинальная функция:")
    # print(processed_list)
    print(f"Время вычисления: {std_time} мс")

    print("\nСамописная функция:")
    # print(processed_list_gen)
    print(f"Время вычисления: {comp_time} мс")

    print("\nСамописная функция-генераторр:")
    # print(processed_list_gen)
    print(f"Время вычисления: {gen_time} мс")



    abs_time_diff = abs(comp_time - gen_time)
    if (abs_time_diff > 0):
        rel_time_diff = round(abs_time_diff / (gen_time + comp_time) * 200, 2)
    else:
        rel_time_diff = 0
    print(f"\nРазница во времени: {abs_time_diff} мс ({abs(rel_time_diff)}%)")    

"""
Сравнить скорость работы этих функций проблемно, поскольку функция с list comprehension 
сразу возвращает список, в то время, как функция-генератор возвращает генератор,
который выдаёт значения по факту "запроса".
Однако же эта функция моментально выдаёт этот генератор, благодаря чему,
можно быстрее приступить к обработке значений, которые мы бы получили от list comprehension
"""
