from functools import wraps
from datetime import datetime

# Определяем декоратор log
def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Получаем текущее время
            start_time = datetime.now()

            # Логируем начало выполнения
            log_message = f"[{start_time}] Calling function '{func.__name__}' with args: {args}, kwargs: {kwargs}\n"

            try:
                # Вызываем оригинальную функцию
                result = func(*args, **kwargs)

                # Логируем успешное выполнение
                end_time = datetime.now()
                log_message += f"[{end_time}] Function '{func.__name__}' completed successfully. Result: {result}\n"
                success = True
            except ZeroDivisionError as e:
                # Логируем ошибку деления на ноль
                end_time = datetime.now()
                error_message = f"[{end_time}] Function '{func.__name__}' raised a ZeroDivisionError. Inputs: {args}, {kwargs}\n"
                log_message += error_message
                success = False
                exception = e  # Сохраняем объект исключения
            except Exception as e:
                # Логируем другие ошибки
                end_time = datetime.now()
                error_message = f"[{end_time}] Function '{func.__name__}' raised an error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                log_message += error_message
                success = False
                exception = e  # Сохраняем объект исключения

            # Определяем, куда выводить логи
            if filename:
                # Записываем логи в файл
                with open(filename, "a") as f:
                    f.write(log_message)
            else:
                # Выводим логи в консоль
                print(log_message, end="")

            # Если была ошибка, пробрасываем исключение дальше
            if not success:
                raise exception  # Пробрасываем сохранённое исключение

            return result

        return wrapper

    return decorator

