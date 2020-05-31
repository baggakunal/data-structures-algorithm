from typing import Dict


def bad_match_table(pattern: str):
    default_value = len(pattern)
    distances: Dict[str, int] = {}

    for index in range(len(pattern)):
        distance = default_value - index - 1
        if distance:
            distances[f'{pattern[index]}'] = distance

    return default_value, distances


def search(to_find: str, find_in: str):
    default_value, distances = bad_match_table(to_find)

    index: int = 0
    while index <= len(find_in) - len(to_find):
        characters_left_to_match = len(to_find) - 1

        while characters_left_to_match >= 0 \
                and to_find[characters_left_to_match] == find_in[index + characters_left_to_match]:
            characters_left_to_match -= 1

        if characters_left_to_match < 0:
            yield index, len(to_find)
            index += len(to_find)
        else:
            index += distances.get(find_in[index + len(to_find) - 1]) or default_value
