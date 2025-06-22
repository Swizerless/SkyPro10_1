from typing import Iterable, Dict

def filter_by_state(dict_to_filter: Iterable[Dict], state: str = "EXECUTED") -> Iterable[Dict]:
    """Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED'),
    а возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению."""
    filtered_list = []
    for element in dict_to_filter:
        if "state" in element and element["state"] == state:
            filtered_list.append(element)
    return filtered_list


def sort_by_date(dict_to_filter: Iterable[Dict], reverse: bool = True) -> Iterable[Dict]:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание), а возвращает
    новый список, отсортированный по дате (date)."""
    try:
        sorted_list_by_date = sorted(
            dict_to_filter,
            key=lambda x: int(x["date"].split("T")[0].replace("-", "")),
            reverse=reverse,
        )
        return sorted_list_by_date
    except KeyError:
        raise ValueError("Ключ 'date' отсутствует в одном из словарей.")
    except ValueError:
        raise ValueError("Некорректный формат даты.")