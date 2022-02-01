# 1. double_result
# This decorator function should return the result of another function multiplied by two

def double_result(func):
    def inner(a, b):
        return func(a, b) * 2

    return inner


def add(a, b):
    return a + b

print(add(5, 5))


@double_result
def add(a, b):
    return a + b

print(add(5, 5))

# 2. only_odd_parameters
# This decorator function should only allow a function to have odd numbers as parameters,
# otherwise, return the string "Please use only odd numbers!"

def only_odd_parameters(func):
    def inner(*args):
        for i in args:
            if i % 2 == 0:
                print("Please use only odd numbers!")
                break
        else:
            return func(*args)

    return inner


@only_odd_parameters
def add(a, b):
    return a + b


print(add(5, 5)) # 10
print(add(4, 9)) # "Please use only odd numbers!"


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e

print(multiply(1, 7, 9, 11, 5)) #3465
print(multiply(1, 8, 9, 11, 5)) # "Please use only odd numbers!"

# 3.* logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):
from functools import wraps

def logged(func):

    @wraps(func)
    def inner(*args, **kwargs):
        print(f"you called {func.__name__}{args}")
        print(f"It returned {func(*args, **kwargs)}")
    return inner
    # log function arguments and its return value
    # pass


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))



# you called func(4, 4, 4)
# it returned 6


# 4. type_check
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.

def type_check(correct_type):
    def inner(func):
        def wrapper(*args):
            if type(*args) == correct_type:
                return func(*args)
            else:
                print(f"Wrong Type: {type(func)} should be printed, since non-{correct_type} passed to decorated function")
        return wrapper
    return inner


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
times2('Not A Number')  # "Wrong Type: string" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])  # "Wrong Type: list" should be printed, since non-str passed to decorated function
