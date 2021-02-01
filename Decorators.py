# Decorators

from time import time


def my_decorator(func):
    def wrap_func():
        print('**********')
        func()
        print('**********')

    return wrap_func


@my_decorator
def hello():
    print('Good Morning')


hello()

# below code uses time module to calculate the execution time


def performance(func):
    def wrapper_func(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        end_time = time()
        print(f'processing time : {end_time - start_time}')
        return
    return wrapper_func


@performance
def multiply_by2():
    for counter in range(100000):
        counter * 2


multiply_by2()
