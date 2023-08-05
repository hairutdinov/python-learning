import time

def decorator_func(func):
    def wrapper_func(*args):
        time.sleep(1)
        # print(wrapper_func.__name__)
        return func(*args)
    return wrapper_func

@decorator_func
def say(something):
    print(something)


say("hello")
