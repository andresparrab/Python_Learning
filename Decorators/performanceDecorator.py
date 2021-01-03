# Decorator
# Custom made decorator to test the performance of the fucntions

from time import time

def performance(fn):
    def wrapper(*args,**kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f"It took {round(t2-t1, 3)} s")
        return result
    return wrapper



@performance
def long_time():
    for i in range(100000000):
        i*5

long_time()