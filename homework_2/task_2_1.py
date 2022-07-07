from typing import List


class Route:
    optimal_len: int = 100000000
    better_way: list = []

    def __init__(self, incoming_data):
        self.incoming_data = incoming_data
        self.len_incoming_data = len(self.incoming_data)

    def get_result(self):
        def _get_result(
                __incoming_data: list,
                __queue: list,
                __length: float,
                counter: int):
            if len(__incoming_data) == self.len_incoming_data:
                new_data = [*__incoming_data]
                new_data.remove(self.incoming_data[0])
                new_x, new_y = [
                    int(coordinate) for coordinate in __incoming_data[0].split(
                        '–')[-1].strip('( )').split(', ')]
                _get_result(new_data, [[new_x, new_y, 0.0]], 0.0, counter - 1)
            elif counter == -1:
                if __length < self.optimal_len:
                    self.optimal_len = __length
                    self.better_way = __queue
                return
            elif counter == 0:
                new_x, new_y = [
                    int(coordinate) for coordinate in self.incoming_data[
                        0].split('–')[-1].strip('( )').split(', ')]
                new_distance = 0.0
                if len(__queue) >= 1:
                    old_x, old_y, old_distance = __queue[-1]

                    distance = ((new_x - old_x) ** 2 + (
                            new_y - old_y) ** 2) ** 0.5
                    new_distance = distance + old_distance
                _get_result(
                    [],
                    __queue + [[new_x, new_y, new_distance]],
                    new_distance,
                    counter - 1
                )
            else:
                for __line in __incoming_data:

                    new_data = [*__incoming_data]
                    new_data.remove(__line)
                    new_x, new_y = [
                        int(coordinate) for coordinate in __line.split(
                            '–')[-1].strip('( )').split(', ')]
                    new_distance = 0.0
                    if len(__queue) >= 1:
                        old_x, old_y, old_distance = __queue[-1]

                        distance = ((new_x - old_x) ** 2
                                    + (new_y - old_y) ** 2) ** 0.5
                        new_distance = distance + old_distance
                    _get_result(
                        new_data,
                        __queue + [[new_x, new_y, new_distance]],
                        new_distance,
                        counter - 1
                    )

        _get_result(self.incoming_data, [], 0, len(self.incoming_data))
        return self.better_way, self.optimal_len


def read_input() -> List[str]:
    data_line = input()
    data = []
    while data_line:
        data.append(data_line)
        data_line = input()
    return data


if __name__ == "__main__":
    print('Введите координаты точек в формате:',
          'Почтовое отделение – (0, 2)',
          'Ул. Грибоедова, 104/25 – (2, 5)',
          'Ул. Бейкер стрит, 221б – (5, 2)',
          'Ул. Большая Садовая, 302-бис – (6, 6)',
          'Вечнозелёная Аллея, 742 – (8, 3)',
          '_________________________________',
          sep='\n')
    input_data = read_input()
    if input_data:
        routes = Route(input_data)
        best_routs, optimal_length = routes.get_result()
        print(*best_routs, ' = ', optimal_length)
    else:
        print("Введен пустой запрос")
