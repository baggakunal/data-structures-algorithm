from collections import deque


class Queue:
    """A First In First Out (FIFO) collection implemented using linked list."""
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        """Adds the specified item to the back of the queue.

        :param item: The item to push.
        """
        self._items.append(item)

    def dequeue(self):
        """Removes and returns the front item from the queue.

        :return: The front item from the queue.
        :raises IndexError: If no items are present.
        """
        try:
            return self._items.popleft()
        except IndexError:
            raise IndexError("The queue is empty.")

    def peek(self):
        """Returns the front item from the queue without removing it from the queue.

        :return: The front item in the queue.
        :raises IndexError: If no items are present.
        """
        try:
            return self._items[0]
        except IndexError:
            raise IndexError("The queue is empty.")

    def count(self) -> int:
        """Returns the current number of items in the queue.

        :return: The current number of items in the queue.
        """
        return len(self._items)

    def clear(self):
        """Removes all items from the queue."""
        self._items.clear()

    def enumerate(self):
        """Enumerates each item in the queue in FIFO order. The queue remains unaltered.

        :return: The FIFO enumerator.
        """
        for item in self._items:
            yield item
