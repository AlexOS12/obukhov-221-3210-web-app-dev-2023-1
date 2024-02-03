n = int(input("Введите число (от 0 до 100) >> "))

if n % 2:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")