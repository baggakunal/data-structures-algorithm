from project.data_structures.binary_tree import BinaryTree
from random import randint


def generate_binary_tree() -> BinaryTree:
    tree = BinaryTree()
    [tree.add(randint(0, 200)) for num in range(0, 50)]
    return tree


def main():
    tree = generate_binary_tree()
    [print(value) for value in tree.enumerate_in_order_traversal()]


if __name__ == '__main__':
    main()