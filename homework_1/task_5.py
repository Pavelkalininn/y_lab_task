import functools


def count_find_num(primesL, limit):
    def _count_find_num(_value):
        for number in primesL:
            _multiplier = _value * number
            if _multiplier <= limit:
                _count_find_num(_multiplier)
                multiplier_result.add(_multiplier)
    multiplier_result = set()
    start_number_multipling = functools.reduce(lambda a, b: a * b, primesL)
    if start_number_multipling <= limit:
        multiplier_result.add(start_number_multipling)
        _count_find_num(start_number_multipling)
    if not multiplier_result:
        return []
    return [len(multiplier_result), max(multiplier_result)]


if __name__ == "__main__":
    primesL = [2, 3]
    limit = 200
    assert count_find_num(primesL, limit) == [13, 192]

    primesL = [2, 5]
    limit = 200
    assert count_find_num(primesL, limit) == [8, 200]

    primesL = [2, 3, 5]
    limit = 500
    assert count_find_num(primesL, limit) == [12, 480]

    primesL = [2, 3, 5]
    limit = 1000
    assert count_find_num(primesL, limit) == [19, 960]

    primesL = [2, 3, 47]
    limit = 200
    assert count_find_num(primesL, limit) == []
