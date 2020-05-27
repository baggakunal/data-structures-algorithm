from project.data_structures.avl_tree import AVLTree
from random import randint


def generate_binary_tree() -> AVLTree:
    tree = AVLTree()
    [tree.add(randint(0, 200)) for num in range(0, 150)]
    return tree


def words_sort():
    tree = AVLTree()
    sentence = None

    while True:
        # Read the sentence from the user.
        sentence = input("Enter a sentence ('quit' to exit): ")
        if sentence.lower() == 'quit':
            return

        # Split the line into words (on spaces).
        words = sentence.strip().split(' ')

        # Add each word to the tree
        [tree.add(word) for word in words if word.strip() != '']

        # Printing each word in in-order.
        [print(value) for value in tree.enumerate_in_order_traversal()]
        tree.clear()


def main():
    tree = generate_binary_tree()
    [print(value) for value in tree.enumerate_in_order_traversal()]


if __name__ == '__main__':
    main()
