from typing import Tuple
class Player:
    def get_move(self, board) -> Tuple[int, int]: ...  # type: ignore


class HumanPlayer(Player):
    def get_move(self, board) -> Tuple[int, int]:
        while True:
            row = int(input("Введите строку: "))
            col = int(input("Введите столбец: "))
            if (
                0 <= row < board.height
                and 0 <= col < board.width
                and board.cells[row][col] == 0
            ):
                return row, col
            print("Некорректный ввод")
