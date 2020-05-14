from collections import deque
from typing import TypeVar, Deque, List, Union, Generator
from math import fabs

TKey = TypeVar('TKey')
TValue = TypeVar('TValue')


class HashTableNodePair:
    """A node in the hash table array."""

    def __init__(self, key: TKey, value: TValue):
        """Constructs a key/value pair for storage in the hash table.

        :param key: The key of the key/value pair.
        :param value: The value of the key/value pair.
        """
        self._key: TKey = key
        self._value: TValue = value

    @property
    def key(self) -> TKey:
        return self._key

    @property
    def value(self) -> TValue:
        return self._value

    @value.setter
    def value(self, value: TValue):
        self._value = value


class HashTableArrayNode:
    """The hash table data chain"""

    """This list contains the actual data in the hash table.  It chains together
    data collisions.  It would be possible to use a list only when there is a collision
    to avoid allocating the list unnecessarily but this approach makes the
    implementation easier to follow for this sample.
    """
    _items: Deque[HashTableNodePair] = None

    def add(self, key: TKey, value: TValue):
        """Adds the key/value pair to the node.

        :param key: The key of the item being added.
        :param value: The value of the item being added.
        :raises KeyError: If the key already exists in the list.
        """
        if self._items is None:
            # Lazy init the linked list
            self._items = deque()
        else:
            # Multiple items might collide and exist in this list - but each
            # key should only be once in the list once.
            found, _ = self.get_value(key)
            if found:
                raise KeyError("The collection already contains the key")

        # If we made it this far - add the item
        self._items.appendleft(HashTableNodePair(key, value))

    def update(self, key: TKey, value: TValue):
        """Updates the value of the existing key/value pair in the list.

        :param key: The key of the item being updated.
        :param value: The updated value.
        :raises KeyError: If the key does not exist in the list.
        """
        try:
            _, item = self._get_item(key)
            item.value = value
        except KeyError:
            raise

    def remove(self, key: TKey) -> bool:
        """Removes the item from the list whose key matches
        the specified key.

        :param key: The key of the item to remove.
        :return: True if the item was removed, false otherwise.
        """
        try:
            _, item = self._get_item(key)
            self._items.remove(item)
            return True
        except KeyError:
            return False

    def get_value(self, key: TKey) -> (bool, TValue):
        if self._items is None or len(self._items) == 0:
            return False, None

        found: bool = False
        value: TValue = None
        for item in self._items:
            if item.key == key:
                found = True
                value = item.value
                break

        return found, value

    def _get_item(self, key: TKey) -> (bool, HashTableNodePair):
        if self._items is not None:
            for item in self._items:
                if item.key == key:
                    return True, item

        raise KeyError("The collection does not contain the key")

    def clear(self):
        if self._items is not None:
            self._items.clear()

    def keys(self) -> Generator[TKey, None, None]:
        """Returns an enumerator for all of the keys in the list."""
        if self._items is not None:
            for item in self._items:
                yield item.key

    def values(self) -> Generator[TValue, None, None]:
        """Returns an enumerator for all of the values in the list."""
        if self._items is not None:
            for item in self._items:
                yield item.value

    def items(self) -> Generator[HashTableNodePair, None, None]:
        """Returns an enumerator for all the key/value pairs in the list."""
        if self._items is not None:
            for item in self._items:
                yield item


class HashTableArray:
    """The fixed size array of the nodes in the hash table"""
    _array: List[Union[HashTableArrayNode, None]] = None

    def __init__(self, capacity: int):
        """Constructs a new hash table array with the specified capacity.

        :param capacity: The capacity of the array.
        """
        self._array = capacity * [None]
        for i in range(capacity):
            self._array[i] = HashTableArrayNode()

    @staticmethod
    def get_index(key: TKey) -> int:
        """Maps a key to the array index based on hash code.

        :param key: The key to be mapped.
        :return: array index.
        """
        return int(fabs(hash(key) % 1000))

    def add(self, key: TKey, value: TValue):
        """Adds the key/value pair to the node.

        :param key: The key of the item being added.
        :param value: The value of the item being added.
        :raises KeyError: If the key already exists in the node array.
        """
        self._array[HashTableArray.get_index(key)].add(key, value)

    def update(self, key, value):
        """Updates the value of the existing key/value pair in the node array.

        :param key: The key of the item being updated.
        :param value: The updated value.
        :raises KeyError: If the key does not exist in the node array.
        """
        self._array[HashTableArray.get_index(key)].update(key, value)

    def remove(self, key) -> bool:
        """Removes the item from the node array whose key matches
        the specified key.

        :param key: The key of the item to remove.
        :return: True if the item was removed, false otherwise.
        """
        return self._array[HashTableArray.get_index(key)].remove(key)

    def get_value(self, key: TKey) -> (bool, TValue):
        """Finds and returns the value for the specified key.

        :param key: The key whose value is sought.
        :return: Tuple containing boolean denoting if the item is found in the array
        and the value associated with the specified key.
        """
        return self._array[HashTableArray.get_index(key)].get_value(key)

    def capacity(self):
        """The capacity of the hash table array."""
        return len(self._array)

    def clear(self):
        """Removes every item from the hash table array."""
        [node.clear() for node in self._array]

    def keys(self) -> Generator[TKey, None, None]:
        """Returns an enumerator for all of the keys in the node array."""
        for node in self._array:
            for key in node.keys():
                yield key

    def values(self) -> Generator[TValue, None, None]:
        """Returns an enumerator for all of the values in the node array."""
        for node in self._array:
            for value in node.values():
                yield value

    def items(self) -> Generator[HashTableNodePair, None, None]:
        """Returns an enumerator for all of the Items in the node array."""
        for node in self._array:
            for item in node.items():
                yield item


class HashTable:
    """A key/value associative collection."""

    # If the array exceeds this fill percentage, it will grow.
    # In this example, the fill factor is the total number of items
    # regardless of whether they are collisions or not.
    _fill_factor: float = 0.75

    # The maximum number of items to store before growing.
    # This is just cached value of the fill factor calculation.
    _max_items_at_current_size: int = 0

    # The number of items in the hash table.
    _count: int = 0

    # The array where the items are stored.
    _array: HashTableArray = None

    def __init__(self, capacity: int = 1000):
        """Constructs a hash table with the specified capacity.
        Default capacity is 1000.
        """
        self._array = HashTableArray(capacity)

        # When the count exceeds this value, the next add will cause the
        # array to grow.
        self._max_items_at_current_size = int(self._fill_factor * self._array.capacity()) + 1

    # TODO: Need to implement iterator protocol.
    # TODO: __iter__() and __getitem__().

    def add(self, key: TKey, value: TValue):
        """Adds the key/value pair to the hash table.

        :param key: The key of the item being added.
        :param value: The value of the item being added.
        :raises KeyError: If the key already exists in the hash table.
        """

        # If we are at capacity, the array needs to grow.
        if self.count() >= self._max_items_at_current_size:
            # Allocate a larger array
            larger_array = HashTableArray(self._array.capacity() * 2)

            # And re-add each item to the new array.
            [larger_array.add(node.key, node.value) for node in self._array.items()]

            # The larger array is now the hash table storage.
            self._array = larger_array

            # Update the new max items cached value.
            self._max_items_at_current_size = int(self._fill_factor * self._array.capacity()) + 1

        self._array.add(key, value)
        self._count += 1

    def update(self, key: TKey, value: TValue):
        """Removes the item from the hash table whose key matches
        the specified key.

        :param key: The key of the item being updated.
        :param value: The updated value.
        :raises KeyError: If the key does not exist in the hash table.
        """
        try:
            self._array.update(key, value)
        except KeyError:
            raise

    def remove(self, key: TKey) -> bool:
        """Removes the item from the hash table whose key matches
        the specified key.

        :param key: The key of the item to remove.
        :return: True if the item was removed, false otherwise.
        """
        removed = self._array.remove(key)
        if removed:
            self._count -= 1

        return removed

    def get_value(self, key: TKey) -> (bool, TValue):
        """Finds and returns the value for the specified key.

        :param key: The key whose value is sought.
        :return: Tuple containing boolean denoting if the item is found in the hash table
        and the value associated with the specified key.
        """
        return self._array.get_value(key)

    def contains_value(self, value: TValue) -> bool:
        """Returns a Boolean indicating if the hash table contains the specified value.

        :param value: The value whose existence is being tested.
        :return: True if the value exists in the hash table, false otherwise.
        """
        for map_value in self._array.values():
            if map_value == value:
                return True

        return False

    def keys(self) -> Generator[TKey, None, None]:
        """Returns an enumerator for all of the keys in the hash table."""
        return self._array.keys()

    def values(self) -> Generator[TValue, None, None]:
        """Returns an enumerator for all of the values in the hash table."""
        return self._array.values()

    def items(self) -> Generator[HashTableNodePair, None, None]:
        """Returns an enumerator for all of the Items in the hash table."""
        return self._array.items()

    def clear(self):
        """Removes all items from the hash table."""
        self._array.clear()
        self._count = 0

    def count(self) -> int:
        """The number of items currently in the hash table."""
        return self._count
