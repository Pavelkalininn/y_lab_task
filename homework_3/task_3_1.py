# Homework 2 task 1

class CyclicIterator:
    def __init__(self, stop_value: int):
        self.current = -1
        self.stop_value = stop_value - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.stop_value:
            self.current += 1
        else:
            self.current = 0
        return self.current


if __name__ == '__main__':
    cyclic_iterator = CyclicIterator(3)
    for i in cyclic_iterator:
        print(i)
