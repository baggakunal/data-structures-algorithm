from project.data_structures.deque_based_queue import Queue


def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    [print(item) for item in queue.enumerate()]
    print('\n')

    queue.dequeue()
    queue.dequeue()
    queue.enqueue(4)
    [print(item) for item in queue.enumerate()]
    print('\n')

    print('Count:', queue.count(), '\n')


if __name__ == '__main__':
    main()
