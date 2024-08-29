def my_decorator(func):
    def wrapper():
        print("Начало выполнения функции.")
        func()
        print("Завершение выполнения функции.")
    return wrapper

@my_decorator
def say_hello():
    print("Привет, мир!")


say_hello()