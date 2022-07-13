# Homework 3 task 2
import time


def repeat_decorator(call_count: int,
                     start_sleep_time: int,
                     factor: int,
                     border_sleep_time: int):
    def actual_decorator(func):
        def wrapper(
            *args, **kwargs
        ):
            yield f'Кол-во запусков = {call_count}. \nНачало работы'
            time_delta = start_sleep_time
            counter = 0
            prev_check_time = 0
            while counter < call_count:
                current_time = int(time.perf_counter())
                if time_delta > border_sleep_time:
                    time_delta = border_sleep_time
                if current_time == time_delta + prev_check_time:
                    time_delta *= factor
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


@repeat_decorator(5, 1, 2, 5)
def multiplier(number: int):
    return number * 2


if __name__ == '__main__':
    result = multiplier(3)
    for string in result:
        print(string)
