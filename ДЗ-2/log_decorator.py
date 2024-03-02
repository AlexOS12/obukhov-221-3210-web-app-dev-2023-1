import time
from datetime import datetime


def logger(path):
    def wrapper(func):
        def called(*args, **kwargs):
            init_time = datetime.now()
            result = func(*args, **kwargs)
            finish_time = datetime.now()
            work_time = finish_time - init_time

            with open(path, 'a', encoding='utf-8') as file:
                file.write('\n')
                file.write(func.__name__ + '\n')
                file.write(str(init_time) + '\n')
                file.write(str(args) + '\n')
                file.write(str(kwargs) + '\n')
                file.write(str(result) if result else '-' + '\n')
                file.write(str(finish_time) + '\n')
                file.write(str(work_time) + '\n')
        return called
    return wrapper


@logger("logs.txt")
def f(*nums: int) -> int:
    time.sleep(0.5)
    return sum(nums)

f(1, 2, 3)