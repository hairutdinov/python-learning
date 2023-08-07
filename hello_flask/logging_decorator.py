# Create the logging_decorator() function 👇
def logging_decorator(func):
    def wrapper(*args):
        print('You called {func_name}{func_args}'.format(func_name=func.__name__, func_args=args))
        result = func(*args)
        print(f'It returned: {result}')
        return result
    return wrapper


# Use the decorator 👇
@logging_decorator
def a_function(a, b, c):
    return a + b + c

a_function(1, 2, 3)