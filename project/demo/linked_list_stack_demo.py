from ..data_structures.linked_list_stack import Stack


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    for item in stack.enumerate():
        print(item)
    print('\n')

    stack.pop()
    stack.pop()
    stack.push(4)
    for item in stack.enumerate():
        print(item)
    print('\n')

    print('Count:', stack.count(), '\n')


if __name__ == '__main__':
    main()
