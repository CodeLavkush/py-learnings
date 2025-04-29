
def log_calls(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(map(str, args))
        kwargs_value = ', '.join(map(str, kwargs.items()))
        result = func(*args, **kwargs)
        print(f"{func.__name__} has been called with {args_value} args, {kwargs_value} kwargs")
        return result
    return wrapper

@log_calls
def add(x, y):
    return x + y

@log_calls
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(add(10, 5))

print(greet("Lavkush",greeting="hi"))