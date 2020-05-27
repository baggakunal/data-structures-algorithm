from project.data_structures.binary_tree import BinaryTree
from project.data_structures.avl_tree import AVLTree
from project.utility.binary_tree_utility import display
from random import randint


def display_options():
    print('Provide input as per below options:')
    print('number\t\t- value to be added to the tree')
    print('r\t\t- Add 50 random values to the tree')
    print('b\t\t- Add 50 pathologically bad values to the tree')
    print('c\t\t- Remove all the values from the tree')
    print('d\t\t- Display Unbalanced and Balanced tree')
    print('o\t\t- Display options')
    print('q or quit\t- Quit')


def add_random_values(unbalanced_tree: BinaryTree, balanced_tree: AVLTree):
    print('Adding 50 random values between 0 and 200')
    for _ in range(0, 50):
        random_value = randint(0, 200)
        unbalanced_tree.add(random_value)
        balanced_tree.add(random_value)


def add_pathologically_bad_values(unbalanced_tree: BinaryTree, balanced_tree: AVLTree):
    random_index = randint(0, 200)
    print(f'Adding 50 pathologically bad values starting from {random_index}')
    for num in range(random_index, random_index+50):
        unbalanced_tree.add(num)
        balanced_tree.add(num)


def main():
    unbalanced_tree = BinaryTree()
    balanced_tree = AVLTree()

    display_options()
    while 1:
        user_input = input('> ')

        if user_input == 'q' or user_input == 'quit':
            break
        elif user_input == 'o':
            display_options()
        elif user_input == 'd':
            if unbalanced_tree.head is None or balanced_tree.head is None:
                print('Both trees are empty')
                continue

            print('\nUnbalanced Tree:\n')
            display(unbalanced_tree.head)
            print()

            print('Balanced Tree:\n')
            display(balanced_tree.head)
            print()
        elif user_input == 'c':
            unbalanced_tree.clear()
            balanced_tree.clear()
        elif user_input == 'b':
            add_pathologically_bad_values(unbalanced_tree, balanced_tree)
        elif user_input == 'r':
            add_random_values(unbalanced_tree, balanced_tree)
        else:
            try:
                num = int(user_input)
                unbalanced_tree.add(num)
                balanced_tree.add(num)
            except ValueError:
                print('Invalid input')


if __name__ == '__main__':
    main()
