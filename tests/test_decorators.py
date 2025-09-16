import pytest
import os
from src.decorators import log


# Тестируемые функции
@log()
def add(a, b):
    return a + b

@log()
def divide(a, b):
    return a / b


# Тесты
def test_log_to_console(capsys):
    """Тест: Логирование в консоль"""
    add(3, 5)
    captured = capsys.readouterr()  # Перехватываем вывод в консоль
    assert "Calling function 'add' with args: (3, 5), kwargs: {}" in captured.out
    assert "Function 'add' completed successfully. Result: 8" in captured.out

def test_log_to_file():
    """Тест: Логирование в файл"""
    # Создаём временный файл
    log_file = "test_log.txt"
    @log(filename=log_file)
    def multiply(a, b):
        return a * b

    multiply(4, 6)

    # Читаем содержимое файла
    with open(log_file, "r") as f:
        content = f.read()

    # Проверяем, что логи содержат ожидаемые строки
    assert "Calling function 'multiply' with args: (4, 6), kwargs: {}" in content
    assert "Function 'multiply' completed successfully. Result: 24" in content

    # Удаляем временный файл
    os.remove(log_file)

def test_error_handling():
    """Тест: Обработка ошибок"""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_other_exception_handling():
    """Тест: Обработка других типов исключений"""
    @log()
    def raise_error():
        raise ValueError("Custom error message")

    with pytest.raises(ValueError):
        raise_error()

def test_log_with_kwargs(capsys):
    """Тест: Логирование с kwargs"""
    @log()
    def greet(name):
        return f"Hello, {name}!"

    greet(name="Alice")
    captured = capsys.readouterr()
    assert "Calling function 'greet' with args: (), kwargs: {'name': 'Alice'}" in captured.out
    assert "Function 'greet' completed successfully. Result: Hello, Alice!" in captured.out

def test_log_to_file_with_kwargs():
    """Тест: Логирование в файл с kwargs"""
    log_file = "test_log_kwargs.txt"
    @log(filename=log_file)
    def greet(name):
        return f"Hello, {name}!"

    greet(name="Bob")

    with open(log_file, "r") as f:
        content = f.read()

    assert "Calling function 'greet' with args: (), kwargs: {'name': 'Bob'}" in content
    assert "Function 'greet' completed successfully. Result: Hello, Bob!" in content

    os.remove(log_file)

def test_successful_execution_with_args_and_kwargs(capsys):
    """Тест: Успешное выполнение с args и kwargs"""
    @log()
    def concatenate(a, b, c):
        return f"{a}-{b}-{c}"

    concatenate(1, 2, c=3)
    captured = capsys.readouterr()
    assert "Calling function 'concatenate' with args: (1, 2), kwargs: {'c': 3}" in captured.out
    assert "Function 'concatenate' completed successfully. Result: 1-2-3" in captured.out

