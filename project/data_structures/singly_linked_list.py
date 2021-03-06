class LinkedListNode:
    """A node in the singly linked list."""

    def __init__(self, value):
        """Constructs a new node with the specified value."""
        self.value = value  # The value of the node.
        self.next = None    # The next node in the list (None if last node).


class LinkedList:
    """A singly linked list collection capable of basic operations such as
    Add, Remove, Find and Enumerate.
    """
    def __init__(self):
        self._head = None    # The first node in the list or None if empty
        self._tail = None    # The last node in the list or None if empty
        self._count = 0

    def head(self) -> LinkedListNode:
        return self._head

    def tail(self) -> LinkedListNode:
        return self._tail

    def add_first(self, node: LinkedListNode):
        """Adds the specified node to the start of the list.

        :param node: The node to add
        """
        # Save the head node so we don't lose the reference
        old_head = self._head

        # Point head to the new node
        self._head = node

        # Insert the rest of the list behind the head
        node.next = old_head

        if self._count == 0:
            # If the list was empty, head and tail should both
            # point to the new node.
            self._tail = self._head

        self._count += 1

    def add_last(self, node: LinkedListNode):
        """Adds the specified node to the end of the list.

        :param node: The node to add
        """
        if self._count == 0:
            self._head = node
        else:
            self._tail.next = node

        self._tail = node
        self._count += 1

    def add(self, value):
        """Adds the specified value to the start of the list.

        :param value: The value to add.
        """
        self.add_first(LinkedListNode(value))

    def append(self, value):
        """Append the specified value to the end of the list.

        :param value: The value to append.
        """
        self.add_last(LinkedListNode(value))

    def remove_first(self):
        if self._count != 0:
            self._head = self._head.next
            self._count -= 1

            if self._count == 0:
                self._tail = None

    def remove_last(self):
        if self._count != 0:
            if self._count == 1:
                self._head = None
                self._tail = None
            else:
                current: LinkedListNode = self._head
                while current.next is not self._tail:
                    current = current.next

                current.next = None
                self._tail = current

            self._count -= 1

    def remove(self, value) -> bool:
        """Remove the first occurrence of the value from the list
        (searching from Head to Tail).

        :param value: The value to remove.
        :return: True if the value was found and removed, False otherwise.
        """
        previous = None
        current = self._head

        # Cases:
        # 1: Empty list -> do nothing
        # 2: Single node (previous is None)
        # 3: Multiple nodes
        #    a: Node to remove is the first node
        #    b: Node to remove is in the middle
        #    c: Node to remove is the last node
        while current is not None:
            if current.value == value:
                if previous is None:    # Case 2 or 3a
                    self.remove_first()
                else:
                    previous.next = current.next    # Case 3b or 3c
                    if current.next is None:        # Case 3c
                        self._tail = previous

                    self._count -= 1

                return True

            previous = current
            current = current.next

        return False

    def pop(self):
        """Remove a value from the end of the list."""
        self.remove_last()

    def clear(self):
        """Remove all the nodes from the list."""
        self._head = None
        self._tail = None
        self._count = 0

    # def count(self) -> int:
    #     """
    #     :return: The number of items currently in the list.
    #     """
    #     return self._count

    def count(self, value) -> int:
        """
        :param value: The value to count in the list.
        :return: Return number of occurrences of the value.
        """
        value_count = 0
        current = self._head

        while current is not None:
            if current.value == value:
                value_count += 1
            current = current.next

        return value_count

    def contains(self, value) -> bool:
        """Check if the list contains specified value.

        :param value: The item to search
        :return: True if the item is found, False otherwise.
        """
        current = self._head

        while current is not None:
            if current.value == value:
                return True
            current = current.next

        return False

    def enumerate(self):
        """Enumerates over the list values from head to tail.

        :return: A head to tail enumerator.
        """
        current: LinkedListNode = self._head
        while current is not None:
            yield current.value
            current = current.next
