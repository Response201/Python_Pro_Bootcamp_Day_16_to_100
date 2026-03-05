
def logging_decorator(func):
    def wrapper(*args) :
        result = func(*args)
        print(f"You called {func.__name__}{args}"
              f"\nIt returned: {result}")
        return result

    return wrapper

@logging_decorator
def a_function(*args):
    return sum(args)



a_function(1, 2, 3)