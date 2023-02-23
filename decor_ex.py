from typing import List
from collections import deque
import time

def mean_deco(k):
    mean_deq = deque(maxlen=k)
    def count_time(func):
        def wrap(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            mean_deq.append(time.time() - start)
            print(sum(mean_deq) / len(mean_deq))
            return res
        return wrap
    return count_time
            


# @mean_deco(10)
# def foo(arg1):
#     return 10

@mean_deco(2)
def boo(a, b):
    return a + b

for _ in range(100):
    foo("Walter")  # при каждом вызове выводится среднее по k=10 последним вызовам
    # boo(1, 2)