from __future__ import annotations
from typing import TypeVar, NoReturn, Deque, Iterable, Iterator, Generator
from collections import deque

T = TypeVar('T')


class Set:
    def __init__(self, items: Iterable[T] = None):
        self._items: Deque[T] = deque()
        if items is not None:
            self.add_range(items)

    def __contains__(self, item: T) -> bool:
        return self._items.__contains__(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        return self._items.__iter__()

    def add(self, item: T) -> NoReturn:
        if self.contains(item):
            raise ValueError(f'Item {item} already exists in the Set')

        self._items.append(item)

    def add_range(self, items: Iterable[T]) -> NoReturn:
        [self.add(item) for item in items]

    def _add_range_skip_duplicates(self, items: Iterable[T]) -> NoReturn:
        for item in items:
            try:
                self.add(item)
            except ValueError:
                pass

    def remove(self, item: T) -> bool:
        try:
            self._items.remove(item)
            return True
        except ValueError:
            return False

    def contains(self, item: T) -> bool:
        return self.__contains__(item)

    def count(self) -> int:
        return len(self)

    def union(self, other: Set) -> Set:
        result = Set(self._items)
        result._add_range_skip_duplicates(other.enumerate())

        return result

    def intersection(self, other: Set) -> Set:
        result = Set()

        for item in self:
            if other.contains(item):
                result.add(item)

        return result

    def difference(self, other: Set) -> Set:
        result = Set(self._items)

        for item in other:
            result.remove(item)

        return result

    def symmetric_difference(self, other: Set) -> Set:
        union_result = self.union(other)
        intersection_result = self.intersection(other)

        return union_result.difference(intersection_result)

    def enumerate(self) -> Generator[T]:
        for item in self._items:
            yield item
