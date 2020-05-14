from project.data_structures.hash_table import HashTable


def print_hash_table(hash_table: HashTable):
    for item in hash_table.items():
        print(f"{item.key}:\t\t\t{item.value}")
    print()


def main():
    map = HashTable()
    map.add('test', 'test')
    map.add('test1', 'test')
    map.add('test2', 'test')
    map.add('test3', 'test')
    print_hash_table(map)

    map.clear()
    map.add('Kunal', 'Kunal')
    map.add('Bagga', 'Bagga')
    map.add('njh sdgfsdajfbsd fbsdf', 'jk fljksdagkjsd ljksdafljkasd')
    print_hash_table(map)


if __name__ == '__main__':
    main()
