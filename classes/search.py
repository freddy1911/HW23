from typing import Iterator, List, Iterable, Set, Union


class Search:

    def filter(self: Iterator, string_to_search: str) -> Iterable:
        """Получить данные, которые содержат указанный текст"""
        if not isinstance(string_to_search, str):
            raise TypeError("В функцию фильтра переданы неверные данные, разрешены только строки")
        return filter(lambda line: string_to_search in line, self)

    def sort(self: Iterator, order: str = 'asc') -> List:
        """Сортировка данных в порядке возрастания или убывания"""
        if order not in ('asc', 'desc'):
            raise ValueError('В функцию сортировки передан неверный аргумент, разрешено использовать '
                             'только по возрастанию или по убыванию')
        if order == 'desc':
            return sorted(self, reverse=True)
        return sorted(self, reverse=False)

    def map(self: Iterator, column: Union[str, int]) -> Iterable:
        """Получить только указанный столбец"""
        if not str(column).isdigit():
            raise TypeError('Нужно передавать цифру в качестве номера столбца в функцию карты')
        return map(lambda line: line.split(' ')[int(column)] + '\n', self)

    def limit(self: Iterator, number: Union[str, int]) -> List:
        """Кол-во строк, возвращаемые переданным числом"""
        if not str(number).isdigit():
            raise TypeError('Разрешены только цифры')
        return list(self)[:int(number)]

    def unique(self: Iterator, *args) -> Set:
        """Возвращать только уникальные строки"""
        return set(self)
