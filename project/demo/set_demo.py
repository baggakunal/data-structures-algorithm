from project.data_structures.set import Set


def print_set(set_data: Set):
    for item in set_data:
        print(item, ' ', end='')
    print()


def main():
    set1 = Set()
    set1.add_range((1, 2, 3))
    print("Set 1:\t\t\t\t\t\t\t", end='')
    print_set(set1)

    set2 = Set((3, 4, 5, 6))
    print("Set 2:\t\t\t\t\t\t\t", end='')
    print_set(set2)
    print()

    union_result = set1.union(set2)
    print("Union result:\t\t\t\t\t", end='')
    print_set(union_result)

    intersection_result = set1.intersection(set2)
    print("Intersection result:\t\t\t", end='')
    print_set(intersection_result)

    difference_result = set1.difference(set2)
    print("Difference result:\t\t\t\t", end='')
    print_set(difference_result)

    symmetric_difference_result = set1.symmetric_difference(set2)
    print("Symmetric difference result:\t", end='')
    print_set(symmetric_difference_result)


if __name__ == '__main__':
    main()
