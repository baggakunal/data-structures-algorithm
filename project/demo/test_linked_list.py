from ..data_structures.linked_list import LinkedList, LinkedListNode
from ..data_structures.node import print_nodes


def main():
    linked_list = LinkedList()
    linked_list.add_first(LinkedListNode(3))
    linked_list.add_first(LinkedListNode(5))
    linked_list.add_last(LinkedListNode(7))
    linked_list.add_last(LinkedListNode(9))
    linked_list.add_last(LinkedListNode(10))
    linked_list.add_first(LinkedListNode(1))
    print_nodes(linked_list.head)
    print('\n')

    linked_list.remove_first()
    linked_list.remove_last()
    linked_list.remove_last()
    linked_list.remove_first()
    linked_list.remove_first()
    linked_list.remove_first()
    linked_list.add_last(LinkedListNode(100))
    linked_list.add_first(LinkedListNode(200))
    for value in linked_list.enumerate():
        print(value)


if __name__ == '__main__':
    main()
