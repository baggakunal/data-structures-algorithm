
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_nodes(node: Node):
    while node is not None:
        print(node.value)
        node = node.next


def main():
    first = Node(3)

    middle = Node(5)
    first.next = middle

    last = Node(7)
    middle.next = last

    print_nodes(first)


if __name__ == '__main__':
    main()
