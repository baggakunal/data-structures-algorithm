def is_power_of_two(num: int) -> bool:
    return num and (num & (num - 1) == 0)


def count_one(num: int) -> int:
    count = 0
    while num:
        num = num & (num - 1)
        count += 1

    return count


def check_i_bit(num: int, i: int) -> bool:
    if num & (1 << i):
        return True
    else:
        return False
