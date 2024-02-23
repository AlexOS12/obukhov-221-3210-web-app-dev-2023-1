def my_sum(*nums : float) -> float:
    sm : float = 0
    for i in nums:
        sm += i
    return sm

if __name__ == "__main__":
    nums = list(map(float, input("Укажите список действительных чисел: ").split()))
    sm = my_sum(*nums)
    print(f"Сумма введённых чисел: {sm}")
