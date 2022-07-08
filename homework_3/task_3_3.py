# Homework 3 task 1

cash = {}


def cash_decorator(func):
    def wrapper(value):
        if value in cash:
            return cash[value]
        result = func(value)
        cash[value] = result
        return result
    return wrapper


@cash_decorator
def multiplier(number: int):
    return number * 2


if __name__ == '__main__':
    print(multiplier(3))
    print(multiplier(5))
    print(multiplier(3))
