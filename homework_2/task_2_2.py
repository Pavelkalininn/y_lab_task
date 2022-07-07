from random import choice
from tkinter import Tk, Button, Frame, messagebox


class Reversed_Game(Tk):

    def __init__(self):
        super().__init__()
        self.title("Обратные крестики-нолики")
        self.button_frame = Frame(self)
        self.button_frame.pack(fill='both', expand=True)
        self.__init_data()

    def __init_data(self):
        self.buttons: list = []
        self.matrix = [
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None]
        ]
        self.free_slots = list(range(100))
        self.danger_slots = []

        for row in range(10):
            buttons_line = []
            for column in range(10):
                new_button = Button(
                    self.button_frame,
                    text='',
                    font=('Verdana', 20, 'bold'),
                    background='lavender',
                    command=(
                        lambda row_num=row,
                               column_num=column:
                        self.on_click_button(row_num, column_num))
                )
                new_button.config(height=1, width=3)
                new_button.grid(column=column, row=row)
                buttons_line.append(new_button)
            self.buttons.append(buttons_line)

    def on_click_button(self, row, column):
        if self.matrix[row][column] not in ['X', 'O']:
            self.buttons[row][column].config(text='X')
            self.matrix[row][column] = 'X'
            slot_number = int(row + column)
            if slot_number in self.free_slots:
                self.free_slots.remove(slot_number)
            if self.line_detection(row, column, 'X', 3):
                self.danger_slots.append([row, column])
            if self.line_detection(row, column, 'X'):
                if messagebox.askyesno(
                        'Игра окончена',
                        message='Собрана линия из пяти крестов. Начать заново?'
                ):
                    self.__init_data()
            self.computer_intellect()

    def line_detection(self, row, column, char, count=5):
        horizontal = 0
        for current_row in range(row, 10):
            if self.matrix[current_row][column] == char:
                horizontal += 1
            else:
                break
        for current_row in range(row, -1, -1):
            if self.matrix[current_row-1][column] == char:
                horizontal += 1
            else:
                break
        vertical = 0
        for current_column in range(column, 10):
            if self.matrix[row][current_column] == char:
                vertical += 1
            else:
                break
        for current_column in range(column, -1, -1):
            if self.matrix[row][current_column-1] == char:
                vertical += 1
            else:
                break
        diagonal_up_right = 0
        temp_row = row
        temp_column = column
        while temp_column < 10 and temp_row >= 0:

            if self.matrix[temp_row][temp_column] == char:
                diagonal_up_right += 1
                temp_row -= 1
                temp_column += 1
            else:
                break
        temp_row = row
        temp_column = column
        while temp_column >= 0 and temp_row < 10:

            if temp_row < 9 and temp_column > 0 and self.matrix[temp_row + 1][temp_column - 1] == char:
                diagonal_up_right += 1
                temp_row += 1
                temp_column -= 1
            else:
                break

        diagonal_up_left = 0
        temp_row = row
        temp_column = column
        while temp_column < 10 and temp_row < 10:
            if self.matrix[temp_row][temp_column] == char:
                diagonal_up_left += 1
                temp_row += 1
                temp_column += 1
            else:
                break
        temp_row = row
        temp_column = column
        while temp_column >= 0 and temp_row >= 0:

            if temp_row > 0 and temp_column > 0 and self.matrix[temp_row - 1][temp_column - 1] == char:
                diagonal_up_left += 1
                temp_row -= 1
                temp_column -= 1
            else:
                break
        return (horizontal >= count
                or vertical >= count
                or diagonal_up_left >= count
                or diagonal_up_right >= count)

    def computer_intellect(self):
        while self.free_slots:
            random_value = [-2, -1, 0, 1, 2]
            if self.danger_slots:
                for attempts in range(15):
                    row_random = choice(random_value)
                    column_random = choice(random_value)
                    dang_row, dang_column = choice(self.danger_slots)
                    new_row = dang_row + row_random
                    new_column = dang_column + column_random
                    find_value = int(str(new_row) + str(new_column))
                    if (not self.line_detection(new_row, new_column, 'O')
                            and find_value in self.free_slots
                            and self.matrix[new_row][new_column] not in [
                                'X', 'O']
                    ):

                        self.buttons[new_row][new_column].config(text='O')
                        self.matrix[new_row][new_column] = 'O'
                        slot_number = int(new_row + new_column)
                        if slot_number in self.free_slots:
                            self.free_slots.remove(slot_number)
                    return
            new_random = choice(self.free_slots)
            row = new_random // 10
            column = new_random % 10
            find_value = int(str(row) + str(column))
            if (self.line_detection(row, column, 'O')
                    or find_value not in self.free_slots
                            or self.matrix[row][column] in [
                                'X', 'O']
            ):
                if find_value in self.free_slots:
                    self.free_slots.remove(int(row + column))
            else:
                self.buttons[row][column].config(text='O')
                self.matrix[row][column] = 'O'
                slot_number = int(row + column)
                if slot_number in self.free_slots:
                    self.free_slots.remove(slot_number)
                return
        if messagebox.askyesno(
                'Игра окончена',
                message='Победа, компьютеру некуда ходить. Начать заново?'
        ):
            self.__init_data()


if __name__ == '__main__':
    app = Reversed_Game()
    app.mainloop()
