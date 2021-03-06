from collections import deque


class Stack:
    """A Last In First Out (LIFO) collection implemented as a linked list."""
    def __init__(self):
        self._list = deque()

    def push(self, item):
        """Adds the specified item to the stack.

        :param item: The item to push.
        """
        self._list.appendleft(item)

    def pop(self):
        """Removes and returns the top item from the stack.

        :return: The top-most item in the stack.
        :raises IndexError: If no items are present.
        """
        try:
            return self._list.popleft()
        except IndexError:
            raise IndexError("The stack is empty.")

    def peek(self):
        """Returns the top item from the stack without removing it from the stack.

        :return: The top-most item in the stack.
        :raises IndexError: If no items are present.
        """
        try:
            return self._list[0]
        except IndexError:
            raise IndexError("The Stack is empty.")

    def count(self) -> int:
        """Returns the current number of items in the stack.

        :return: The current number of items in the stack.
        """
        return len(self._list)

    def clear(self):
        """Removes all items from the stack."""
        self._list.clear()

    def enumerate(self):
        """Enumerates each item in the stack in LIFO order. The stack remains unaltered.

        :return: The LIFO enumerator.
        """
        for item in self._list:
            yield item
