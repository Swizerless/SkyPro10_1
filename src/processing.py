from typing import Iterable


def filter_by_state(dict_to_filter: Iterable, state: str = "EXECUTED") -> Iterable:
    """Функция принимает список словарей и опционально
    значение для ключа state (по умолчанию 'EXECUTED'),
    а возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    filtered_list = []
    for element in dict_to_filter:
        for key, value in element.items():
            if value == state:
                filtered_list.append(element)
    return filtered_list


def sort_by_date(dict_to_filter: Iterable, reverse: bool = True) -> Iterable:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание), а возвращает
    новый список, отсортированный по дате (date)"""
    sorted_list_by_date = sorted(
        dict_to_filter, key=lambda x: int(x["date"].split("T")[0].replace("-", "")), reverse=reverse
    )
    return sorted_list_by_date
