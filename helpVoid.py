def decorator_with_args(decorator_arg1, decorator_arg2):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Декоратор получил следующие аргументы: {decorator_arg1}, {decorator_arg2}")
            # Вы можете использовать аргументы декоратора здесь
            result = func(*args, **kwargs)
            # Или здесь
            return result

        return wrapper

    return my_decorator


# Использование декоратора с аргументами
@decorator_with_args("значение1", "значение2")
def say_hello(name):
    print(f"Привет, {name}!")


say_hello("Алиса")
