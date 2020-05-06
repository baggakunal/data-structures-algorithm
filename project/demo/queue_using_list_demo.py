from project.data_structures.queue_using_list import Queue


def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.print()
    print()

    queue.dequeue()
    queue.dequeue()
    queue.enqueue(4)
    queue.print()
    print()

    print('Count:', queue.count(), '\n')

    queue.clear()
    queue.print()
    print('Count:', queue.count(), '\n')


if __name__ == '__main__':
    main()
