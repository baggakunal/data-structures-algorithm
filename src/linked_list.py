from src.node import Node


def main():
    first = Node(3)

    middle = Node(5)
    first.next = middle

    last = Node(7)
    middle.next = last


if __name__ == '__main__':
    main()
