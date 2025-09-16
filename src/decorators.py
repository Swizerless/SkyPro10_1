from datetime import datetime
from functools import wraps
from typing import Any, Callable, Optional


# Определяем декоратор log
def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования вызовов функции.

    Логирует начало выполнения функции, её аргументы, результат или ошибку.
    Логи могут быть выведены в консоль или записаны в файл.

    Args:
        filename (str, optional): Имя файла для записи логов.
                                  Если не указано, логи выводятся в консоль.

    Поведение:
        - При успешном выполнении функции логируется её результат.
        - При возникновении ошибки логируется тип ошибки и входные параметры.
        - Исключение пробрасывается дальше после логирования.

    Пример использования:
        @log()
        def add(a, b):
            return a + b

        @log(filename="mylog.txt")
        def divide(a, b):
            return a / b

        add(3, 5)       # Логи выводятся в консоль
        divide(10, 2)   # Логи записываются в файл "mylog.txt"
    """

    def decorator(func: Callable[..., Any]) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = datetime.now()
            log_message = f"[{start_time}] Calling function '{func.__name__}' with args: {args}, kwargs: {kwargs}\n"
            exception: Exception  # Объявляем переменную с типом Exception
            try:
                result = func(*args, **kwargs)
                end_time = datetime.now()
                log_message += f"[{end_time}] Function '{func.__name__}' completed successfully. Result: {result}\n"
                success = True
            except ZeroDivisionError as e:
                end_time = datetime.now()
                error_message = (
                    f"[{end_time}] Function '{func.__name__}' raised a ZeroDivisionError. Inputs: {args}, {kwargs}\n"
                )
                log_message += error_message
                success = False
                exception = e  # Присваиваем значение типа ZeroDivisionError
            except Exception as e:
                end_time = datetime.now()
                error_message = f"[{end_time}] Function '{func.__name__}' raised an error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                log_message += error_message
                success = False
                exception = e  # Присваиваем значение типа Exception

            if filename:
                with open(filename, "a") as f:
                    f.write(log_message)
            else:
                print(log_message, end="")

            if not success:
                raise exception  # Пробрасываем сохранённое исключение

            return result

        return wrapper

    return decorator
