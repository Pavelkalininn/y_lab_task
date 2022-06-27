
def zeros(n):
    result = 0
    deleter = 5
    while n // deleter > 0:
        result += n // deleter
        deleter *= 5
    return result


if __name__ == "__main__":
    assert zeros(0) == 0
    assert zeros(6) == 1
    assert zeros(30) == 7
