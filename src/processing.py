from typing import Iterable

def filter_by_state(dict_to_filter: Iterable, state='EXECUTED') -> Iterable:
    """ Функция принимает список словарей и опционально
    значение для ключа state (по умолчанию 'EXECUTED'),
    а возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    filtered_list = []
    for element in dict_to_filter:
        for key, value in element.items():
            if value == state:
                filtered_list.append(element)
    return filtered_list
