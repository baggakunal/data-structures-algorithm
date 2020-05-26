from __future__ import annotations
from collections import deque
from enum import Enum
from typing import TypeVar, Optional

TNode = TypeVar('TNode')


class TreeState(Enum):
    LeftHeavy = 'LeftHeavy'
    RightHeavy = 'RightHeavy'
    Balanced = 'Balanced'


class AVLTreeNode:
    """An AVL tree node class."""
    def __init__(self, value: TNode, parent: Optional[AVLTreeNode], tree: AVLTree):
        self._value: TNode = value
        self.left: Optional[AVLTreeNode] = None
        self.right: Optional[AVLTreeNode] = None
        self.parent: AVLTreeNode = parent
        self._tree: AVLTree = tree

    # region Properties and Methods
    @property
    def value(self) -> TNode:
        return self._value

    @property
    def tree(self) -> AVLTree:
        return self._tree

    def _max_child_height(self, node: AVLTreeNode) -> int:
        if node:
            return 1 + max(self._max_child_height(node.left), self._max_child_height(node.right))
        return 0

    @property
    def _left_height(self) -> int:
        return self._max_child_height(self.left)

    @property
    def _right_height(self) -> int:
        return self._max_child_height(self.right)

    @property
    def _state(self) -> TreeState:
        left_height = self._left_height
        right_height = self._right_height

        if left_height - right_height > 1:
            return TreeState.LeftHeavy
        if right_height - left_height > 1:
            return TreeState.RightHeavy
        return TreeState.Balanced

    @property
    def _balance_factor(self) -> int:
        return self._right_height - self._left_height
    # endregion

    def compare_to(self, other: AVLTreeNode) -> int:
        """Compares the current node to the provided value.

        :param other: The node value to compare to.
        :return: 1 if the instance value is greater than provided value, -1 if less or 0 if equal.
        """
        if self._value == other.value:
            return 0
        elif self._value > other.value:
            return 1
        else:
            return -1

    def compare_to_value(self, value: TNode) -> int:
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

    # region Balancing Methods
    def _balance(self):
        tree_state = self._state

        if tree_state == TreeState.RightHeavy:
            if self.right and self.right._balance_factor < 0:
                self._left_right_rotation()
            else:
                self._left_rotation()
        elif tree_state == TreeState.LeftHeavy:
            if self.left and self.left._balance_factor > 0:
                self._right_left_rotation()
            else:
                self._right_rotation()

    def _left_rotation(self):
        """
            a (self)
             \
              b
             / \
            d   c

        becomes
              b
             / \
            a   c
             \
              d
        """
        new_root = self.right

        # Replace the current root with the new root
        self._replace_root(new_root)

        # Take ownership of right's left child as right (now parent)
        self.right = new_root.left

        # The new root takes self as it's left
        new_root.left = self

    def _right_rotation(self):
        """
            c (self)
           /
          b
         / \
        a   d

        becomes
              b
             / \
            a   c
               /
              d
        """
        new_root = self.left

        # Replace the current root with the new root
        self._replace_root(new_root)

        # Take ownership of left's right child as left (now parent)
        self.left = new_root.right

        # The new root takes self as it's right
        new_root.right = self

    def _left_right_rotation(self):
        self.right._right_rotation()
        self._left_rotation()

    def _right_left_rotation(self):
        self.left._left_rotation()
        self._right_rotation()

    def _replace_root(self, new_root: AVLTreeNode):
        if self.parent:
            if self.parent.left == self:
                self.parent.left = new_root
            elif self.parent.right == self:
                self.parent.right = new_root
        else:
            self._tree.head = new_root

        new_root.parent = self.parent
        self.parent = new_root
    # endregion


class AVLTree:
    def __init__(self):
        self.head: Optional[AVLTreeNode] = None
        self._count = 0

    # region Add
    def add(self, value: TNode):
        """Adds the provided value to the binary tree.

        :param value: Value to add to the tree.
        """
        if self.head is None:
            # Case 1: The tree is empty - allocate the head.
            self.head = AVLTreeNode(value, None, self)
        else:
            # Case 2: The tree is not empty so find the right location to insert.
            self._add_to(self.head, value)

        self._count += 1

    def _add_to(self, node: AVLTreeNode, value: TNode):
        """Recursion add algorithm."""
        if node.compare_to_value(value) > 0:
            # Case 1: value is less than the current node value.
            if node.left is None:
                # If there is no left child, make this the new left.
                node.left = AVLTreeNode(value, node, self)
            else:
                self._add_to(node.left, value)
        else:
            # Case 2: value is greater than or equal to the current node value.
            if node.right is None:
                # If there is no right child, make this the new right.
                node.right = AVLTreeNode(value, node, self)
            else:
                self._add_to(node.right, value)
    # endregion

    def contains(self, value: TNode) -> bool:
        """Determines if the specified value exists in the binary tree.

        :param value: The value to search for.
        :return: True if the tree contains the value, false otherwise.
        """
        node, parent = self._find_with_parent(value)
        return node is not None

    def _find_with_parent(self, value: TNode) -> (AVLTreeNode, AVLTreeNode):
        """Finds and returns the first node containing containing the specified value.
        If the value is not found, returns None.
        Also returns the parent of the found node (or None), which is used in Remove.

        :param value: The value to search for.
        :return: Tuple of The found node (or None) and the parent of the found node.
        """
        current: AVLTreeNode = self.head
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

    def remove(self, value: TNode):
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
                self.head = current.left
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
                self.head = current.right
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
                self.head = left_most
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
        self._pre_order_traversal(action, self.head)

    def _pre_order_traversal(self, action, node: AVLTreeNode):
        if node is not None:
            action(node.value())
            self._pre_order_traversal(action, node.left)
            self._pre_order_traversal(action, node.right)
    # endregion

    # region Post-Order Traversal
    def post_order_traversal(self, action):
        """Performs the provided action on each binary tree value in post-order traversal order."""
        self._post_order_traversal(action, self.head)

    def _post_order_traversal(self, action, node: AVLTreeNode):
        if node is not None:
            self._post_order_traversal(action, node.left)
            self._post_order_traversal(action, node.right)
            action(node.value())
    # endregion

    # region In-Order Traversal
    def in_order_traversal(self, action):
        """Performs the provided action on each binary tree value in in-order traversal order."""
        self._in_order_traversal(action, self.head)

    def _in_order_traversal(self, action, node: AVLTreeNode):
        if node is not None:
            self._in_order_traversal(action, node.left)
            action(node.value())
            self._in_order_traversal(action, node.right)

    def enumerate_in_order_traversal(self):
        """Enumerates the values contained in the binary tree in in-order traversal order.

        :return: The enumerator.
        """
        if self.head is not None:
            """This is a non-recursive algorithm using a stack to demonstrate
            enumeration in in-order traversal order."""

            # Store the nodes we've skipped in this stack.
            stack = deque()

            current: AVLTreeNode = self.head

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
                yield current.value

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
        self.head = None
        self._count = 0

    def count(self) -> int:
        """Returns the number of items currently contained in the tree.

        :return: Returns the count of items in the tree.
        """
        return self._count
