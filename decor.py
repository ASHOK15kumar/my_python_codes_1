def logger(func):
    def wrapper(*args, **kwargs):
        print("Before function runs")
        result = func(*args, **kwargs)
        print("After function runs")
        return result
    return wrapper

@logger
def say_hello():
    print("Hello")

say_hello()
