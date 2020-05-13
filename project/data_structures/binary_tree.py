from __future__ import annotations
from collections import deque


class BinaryTreeNode:
    """A binary tree node class - encapsulates the value and left/right pointers."""
    def __init__(self, value):
        self._value = value
        self.left = None
        self.right = None

    def value(self):
        return self._value

    def compare_to(self, other: BinaryTreeNode) -> int:
        """Compares the current node to the provided value.

        :param other: The node value to compare to.
        :return: 1 if the instance value is greater than provided value, -1 if less or 0 if equal.
        """
        if self._value == other.value():
            return 0
        elif self._value > other.value():
            return 1
        else:
            return -1

    def compare_to_value(self, value) -> int:
        """Compares the current node to the provided value.

        :param value: The value to compare to.
        :return: 1 if the instance value is greater than provided value, -1 if less or 0 if equal.
        """
        if self._value == value:
            return 0
        elif self._value > value:
            return 1
        else:
            return -1


class BinaryTree:
    def __init__(self):
        self._head = None
        self._count = 0

    # region Add
    def add(self, value):
        """Adds the provided value to the binary tree.

        :param value: Value to add to the tree.
        """
        if self._head is None:
            # Case 1: The tree is empty - allocate the head.
            self._head = BinaryTreeNode(value)
        else:
            # Case 2: The tree is not empty so find the right location to insert.
            self._add_to(self._head, value)

        self._count += 1

    def _add_to(self, node: BinaryTreeNode, value):
        """Recursion add algorithm."""
        if node.compare_to_value(value) > 0:
            # Case 1: value is less than the current node value.
            if node.left is None:
                # If there is no left child, make this the new left.
                node.left = BinaryTreeNode(value)
            else:
                self._add_to(node.left, value)
        else:
            # Case 2: value is greater than or equal to the current node value.
            if node.right is None:
                # If there is no right child, make this the new right.
                node.right = BinaryTreeNode(value)
            else:
                self._add_to(node.right, value)
    # endregion

    def contains(self, value) -> bool:
        """Determines if the specified value exists in the binary tree.

        :param value: The value to search for.
        :return: True if the tree contains the value, false otherwise.
        """
        node, parent = self._find_with_parent(value)
        return node is not None

    def _find_with_parent(self, value) -> (BinaryTreeNode, BinaryTreeNode):
        """Finds and returns the first node containing containing the specified value.
        If the value is not found, returns None.
        Also returns the parent of the found node (or None), which is used in Remove.

        :param value: The value to search for.
        :return: Tuple of The found node (or None) and the parent of the found node.
        """
        current: BinaryTreeNode = self._head
        parent = None

        while current is not None:
            result: int = current.compare_to_value(value)

            if result > 0:
                # If value is less than current, go left.
                parent = current
                current = current.left
            elif result < 0:
                # If value is greater than current, go right.
                parent = current
                current = current.right
            else:
                # We have a match.
                break

        return current, parent

    # region Remove

    def remove(self, value):
        """Removes the first occurrence of the specified value from the tree.

        :param value: The param to remove.
        :return: True if value was removed, False otherwise.
        """
        current, parent = self._find_with_parent(value)
        if current is None:
            return False

        if current.right is None:
            # Case 1: If current has no right child, then current's left replaces current.
            if parent is None:
                self._head = current.left
            else:
                if parent.compare_to(current) > 0:
                    # If parent value is greater than current value,
                    # make the current left child a left child of parent.
                    parent.left = current.left
                else:
                    # If parent value is less than or equal to current value,
                    # make the current left child a right child of parent.
                    parent.right = current.left
        elif current.right.left is None:
            # Case 2: If current's right has no left child, then current's right child replaces current.
            current.right.left = current.left

            if parent is None:
                self._head = current.right
            else:
                if parent.compare_to(current) > 0:
                    # If parent value is greater than current value,
                    # make the current left right a left child of parent.
                    parent.left = current.right
                else:
                    # If parent value is less than or equal to current value,
                    # make the current left right a right child of parent.
                    parent.right = current.right
        else:
            # Case 3: If current's right child has a left child, then replace current with current's
            # right child's left most child.

            # Find the right child's left most node and its parent.
            left_most = current.right.left
            left_most_parent = current.right

            while left_most.left is not None:
                left_most_parent = left_most
                left_most = left_most.left

            # The parent's left subtree becomes the leftmost's right subtree.
            left_most_parent.left = left_most.right

            # Assign leftmost's left and right to current's left and right children.
            left_most.left = current.left
            left_most.right = current.right

            if parent is None:
                self._head = left_most
            else:
                if parent.compare_to(current) > 0:
                    # If parent value is greater than current value,
                    # make leftmost the left child of parent.
                    parent.left = left_most
                else:
                    # If parent value is less than or equal to current value,
                    # make leftmost the right child of parent.
                    parent.right = left_most

        self._count -= 1
        return True
    # endregion

    # region Pre-Order Traversal
    def pre_order_traversal(self, action):
        """Performs the provided action on each binary tree value in pre-order traversal order."""
        self._pre_order_traversal(action, self._head)

    def _pre_order_traversal(self, action, node: BinaryTreeNode):
        if node is not None:
            action(node.value())
            self._pre_order_traversal(action, node.left)
            self._pre_order_traversal(action, node.right)
    # endregion

    # region Post-Order Traversal
    def post_order_traversal(self, action):
        """Performs the provided action on each binary tree value in post-order traversal order."""
        self._post_order_traversal(action, self._head)

    def _post_order_traversal(self, action, node: BinaryTreeNode):
        if node is not None:
            self._post_order_traversal(action, node.left)
            self._post_order_traversal(action, node.right)
            action(node.value())
    # endregion

    # region In-Order Traversal
    def in_order_traversal(self, action):
        """Performs the provided action on each binary tree value in in-order traversal order."""
        self._in_order_traversal(action, self._head)

    def _in_order_traversal(self, action, node: BinaryTreeNode):
        if node is not None:
            self._in_order_traversal(action, node.left)
            action(node.value())
            self._in_order_traversal(action, node.right)

    def enumerate_in_order_traversal(self):
        """Enumerates the values contained in the binary tree in in-order traversal order.

        :return: The enumerator.
        """
        if self._head is not None:
            """This is a non-recursive algorithm using a stack to demonstrate
            enumeration in in-order traversal order."""

            # Store the nodes we've skipped in this stack.
            stack = deque()

            current: BinaryTreeNode = self._head

            # When removing recursion we need to keep a track of whether or not
            # we should be going to the left nodes or the right nodes next.
            go_left_next = True

            # Start by pushing the head onto the stack.
            stack.append(current)

            while len(stack):
                # If we are going left.
                if go_left_next:
                    while current.left:
                        # Push everything but the left most node to the stack.
                        # We'll yield leftmost node after this block
                        stack.append(current)
                        current = current.left

                # In-order is left -> yield -> right
                yield current.value()

                # If we can go right then do so.
                if current.right:
                    current = current.right

                    # Once we have gone right once, we need to start going left again.
                    go_left_next = True
                else:
                    # If we can't go right then we need to pop off the parent node
                    # so we can process it and then go to its right node.
                    current = stack.pop()
                    go_left_next = False
    # endregion

    def clear(self):
        """Removes all the items from the tree."""
        self._head = None
        self._count = 0

    def count(self) -> int:
        """Returns the number of items currently contained in the tree.

        :return: Returns the count of items in the tree.
        """
        return self._count
