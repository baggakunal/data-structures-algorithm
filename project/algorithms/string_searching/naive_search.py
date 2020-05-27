def search(to_find: str, find_in: str):
    """

    :param to_find: string to find
    :param find_in: string to find from
    :return:
    """
    if to_find is None or len(to_find) == 0:
        print('String to find is empty.')
        return

    if find_in is None or len(find_in) == 0:
        print('String to find in is empty.')

    start_index = 0
    end_index = len(find_in) - len(to_find) + 1
    if end_index < 0:
        return

    for index in range(start_index, end_index):
        match_count = 0

        while find_in[index + match_count] == to_find[match_count]:
            match_count += 1
            if len(to_find) == match_count:
                yield index, match_count
                break
