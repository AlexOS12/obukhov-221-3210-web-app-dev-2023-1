cube = lambda x: x ** 3

def fibonacci(n : int) -> list[int]:
    # return a list of fibonacci numbers
    fibs = [0, 1]
    if n == 1:
        return [0]
    
    for i in range(n - 2):
        fibs.append(fibs[-1] + fibs[-2])

    return fibs


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

