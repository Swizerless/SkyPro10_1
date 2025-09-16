import os
from typing import Any

import pytest

from src.decorators import log


@log()
def add(a: int, b: int) -> int:
    return a + b


@log()
def divide(a: int, b: int) -> float:
    return a / b


def test_log_to_console(capsys: Any) -> None:
    add(3, 5)
    captured = capsys.readouterr()
    assert "Calling function 'add' with args: (3, 5), kwargs: {}" in captured.out
    assert "Function 'add' completed successfully. Result: 8" in captured.out


def test_log_to_file() -> None:
    log_file = "test_log.txt"

    @log(filename=log_file)
    def multiply(a: int, b: int) -> int:
        return a * b

    multiply(4, 6)

    with open(log_file, "r") as f:
        content = f.read()

    assert "Calling function 'multiply' with args: (4, 6), kwargs: {}" in content
    assert "Function 'multiply' completed successfully. Result: 24" in content

    os.remove(log_file)


def test_error_handling() -> None:
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_other_exception_handling() -> None:
    @log()
    def raise_error() -> None:
        raise ValueError("Custom error message")

    with pytest.raises(ValueError):
        raise_error()


def test_log_with_kwargs(capsys: Any) -> None:
    @log()
    def greet(name: str) -> str:
        return f"Hello, {name}!"

    greet(name="Alice")
    captured = capsys.readouterr()
    assert "Calling function 'greet' with args: (), kwargs: {'name': 'Alice'}" in captured.out
    assert "Function 'greet' completed successfully. Result: Hello, Alice!" in captured.out


def test_log_to_file_with_kwargs() -> None:
    log_file = "test_log_kwargs.txt"

    @log(filename=log_file)
    def greet(name: str) -> str:
        return f"Hello, {name}!"

    greet(name="Bob")

    with open(log_file, "r") as f:
        content = f.read()

    assert "Calling function 'greet' with args: (), kwargs: {'name': 'Bob'}" in content
    assert "Function 'greet' completed successfully. Result: Hello, Bob!" in content

    os.remove(log_file)


def test_successful_execution_with_args_and_kwargs(capsys: Any) -> None:
    @log()
    def concatenate(a: int, b: int, c: int) -> str:
        return f"{a}-{b}-{c}"

    concatenate(1, 2, c=3)
    captured = capsys.readouterr()
    assert "Calling function 'concatenate' with args: (1, 2), kwargs: {'c': 3}" in captured.out
    assert "Function 'concatenate' completed successfully. Result: 1-2-3" in captured.out
