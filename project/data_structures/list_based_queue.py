class Queue:
    """A First In First Out (FIFO) collection implemented using list."""
    def __init__(self):
        self._list = list()
        self._size = 0      # The number of items in the queue
        self._head = 0      # The index of the first (oldest) item in the queue
        self._tail = -1     # The index of the last (newest) item in the queue

    def _double_size(self):
        if len(self._list) == 0:
            self._list = 4 * [None]
        else:
            if self._tail < self._head:
                new_list = self._list[self._head:] + self._list[:self._head]
            else:
                new_list = self._list[self._head:]
            new_list += self._size * [None]

            self._list = new_list
            self._head = 0
            self._tail = self._size - 1
            self._size = len(self._list)

    def enqueue(self, item):
        """Adds the specified item to the back of the queue.

        :param item: The item to push.
        """
        if len(self._list) == self._size:
            self._double_size()

        # If tail is at the end of the array, we need to wrap around
        if self._tail == len(self._list) - 1:
            self._tail = 0
        else:
            self._tail += 1

        self._list[self._tail] = item
        self._size += 1

    def dequeue(self):
        """Removes and returns the front item from the queue.

        :return: The front item from the queue.
        :raises IndexError: If no items are present.
        """
        if self._size == 0:
            raise IndexError("The queue is empty.")

        item = self._list[self._head]
        self._list[self._head] = None
        self._size -= 1

        if self._head == self._tail:                # If head is at the same index as tail, move both to 0 index
            self._head = self._tail = 0
        elif self._head == len(self._list) - 1:     # If head is at the last index in the array, wrap around
            self._head = 0
        else:                                       # Mode to the next value
            self._head += 1

        return item

    def peek(self):
        """Returns the front item from the queue without removing it from the queue.

        :return: The front item in the queue.
        :raises IndexError: If no items are present.
        """
        if self._size == 0:
            raise IndexError("The queue is empty.")

        return self._list[self._head]

    def count(self) -> int:
        """Returns the current number of items in the queue.

        :return: The current number of items in the queue.
        """
        return self._size

    def clear(self):
        """Removes all items from the queue."""
        # self._list = list()
        self._size = 0
        self._head = 0
        self._tail = -1

    def enumerate(self):
        """Enumerates each item in the queue in FIFO order. The queue remains unaltered.

        :return: The FIFO enumerator.
        """
        if self._size == 0:
            return []

        if self._tail < self._head:
            print_list = self._list[self._head:] + self._list[:self._tail + 1]
        else:
            print_list = self._list[self._head:self._tail + 1]

        for item in print_list:
            yield item

    def print(self):
        [print(item) for item in self.enumerate() if item is not None]

    def _print_array(self):
        """This is to check how the queue items are stored in the array"""
        print(self._list)
