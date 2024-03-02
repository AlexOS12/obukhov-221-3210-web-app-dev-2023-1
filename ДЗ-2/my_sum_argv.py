from sys import argv

def my_sum(*nums : float) -> float:
    sm : float = 0.0
    for i in nums:
        sm += i
    return sm

if __name__ == "__main__":
    args = tuple(map(float, argv[1:]))
    print(my_sum(*args))