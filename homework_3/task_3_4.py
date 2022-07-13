# Homework 3 task 2
import time

cash = {}


def cash_decorator(func):
    def wrapper(value):
        if value in cash:
            return cash[value]
        cash_result = func(value)
        cash[value] = cash_result
        return cash_result

    return wrapper


def repeat_decorator(call_count: int,
                     start_sleep_time: int,
                     factor: int,
                     border_sleep_time: int):
    def actual_decorator(func):
        def wrapper(
            *args, **kwargs
        ):
            yield 'Начало работы'
            time_delta = start_sleep_time
            counter = 0
            prev_check_time = 0
            while counter < call_count:
                current_time = int(time.perf_counter())
                if counter:
                    time_delta *= 2 ** factor
                if time_delta > border_sleep_time:
                    time_delta = border_sleep_time
                if current_time == time_delta + prev_check_time:
                    counter += 1
                    func_result = func(*args, **kwargs)
                    waiting_time = current_time - prev_check_time
                    yield (f'Запуск номер {counter}. '
                           f'Ожидание: {waiting_time} секунд. '
                           f'Результат декорируемой функций = {func_result}.')
                    prev_check_time = current_time
            yield 'Конец работы'

        return wrapper
    return actual_decorator


@repeat_decorator(3, 2, 2, 7)
@cash_decorator
def multiplier(number: int):
    return number * 2


if __name__ == '__main__':
    result = multiplier(3)
    for string in result:
        print(string)
