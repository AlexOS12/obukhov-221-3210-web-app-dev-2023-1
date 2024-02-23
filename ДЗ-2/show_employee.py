def show_employee(name : str, salary : int = 100_000) -> str:
    return f"{name}: {salary} ₽"

if __name__ == "__main__":
    name = input("Укажите имя сотрудника: ")
    salary = input("Укажите з/п сотрудника: ")
    if (salary):
        print(show_employee(name, int(salary)))
    else:
        print(show_employee(name))