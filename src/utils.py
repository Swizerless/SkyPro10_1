import json
import os

def convert_operations_dict(path: str) -> list:
    """
        Функция принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
        Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """

    # Проверяем, существует ли файл
    if not os.path.exists(path):
        print(f"Файл не найден: {path}")
        return []

    try:
        # Открываем файл и пытаемся загрузить данные
        with open(path, encoding='utf-8') as f:
            data = json.load(f)

        # Проверяем, является ли загруженный объект списком
        if not isinstance(data, list):
            print(f"Файл содержит некорректные данные (ожидался список): {data}")
            return []

        # Возвращаем список словарей
        return data

    except json.JSONDecodeError:
        # Если файл пустой или содержит невалидный JSON
        print(f"Файл пустой или содержит некорректный JSON: {path}")
        return []
