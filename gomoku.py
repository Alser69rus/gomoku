class Board:
    def __init__(self, width, height, *, line_to_win=5):
        self.width = width
        self.height = height
        self.line_to_win = line_to_win
        self.cells = [[0] * width for _ in range(height)]
        self.cell_chars = {0: " ", 1: "\033[31mX\033[0m", 2: "\033[32mO\033[0m"}
        self.move_count = 0

    def current_player(self):
        return self.move_count % 2 + 1

    def show(self):
        print(
            f'{f"Ход {self.move_count+1}, ходит игрок {self.cell_chars[self.current_player()]}":^{self.width*4+5}}'
        )
        print("   ", end="")
        for i in range(self.width):
            print(f" {i:^{3}}", end="")
        print("")

        print("  ", "-" * (self.width * 4 + 1))
        for i, row in enumerate(self.cells):
            print(f"{i:<3}", end="")
            for cell in row:
                print(f"| {self.cell_chars[cell]} ", end="")
            print("|")
            print("  ", "-" * (self.width * 4 + 1))

    def aviable_moves(self):
        moves = []
        for i in range(self.height):
            for j in range(self.width):
                if self.cells[i][j] == 0:
                    moves.append((i, j))
        return moves

    def check_win_for_cel(self, row: int, col: int) -> int:
        if self.cells[row][col] == 0:
            return 0

        player = self.cells[row][col]

        start = row
        while start > 0 and self.cells[start - 1][col] == player:
            start -= 1
        end = row
        while end < self.height - 1 and self.cells[end + 1][col] == player:
            end += 1
        if end - start + 1 == self.line_to_win:
            return player

        start = col
        while start > 0 and self.cells[row][start - 1] == player:
            start -= 1
        end = col
        while end < self.width - 1 and self.cells[row][end + 1] == player:
            end += 1
        if end - start + 1 == self.line_to_win:
            return player

        start = 0
        while (
            row - start > 0
            and col - start > 0
            and self.cells[row - start - 1][col - start - 1] == player
        ):
            start += 1
        end = 0
        while (
            row + end < self.height - 1
            and col + end < self.width - 1
            and self.cells[row + end + 1][col + end + 1] == player
        ):
            end += 1

        if end + start + 1 == self.line_to_win:
            return player

        start = 0
        while (
            row + start < self.height - 1
            and col - start > 0
            and self.cells[row + start + 1][col - start - 1] == player
        ):
            start += 1
        end = 0
        while (
            row - end > 0
            and col + end < self.width - 1
            and self.cells[row - end - 1][col + end + 1] == player
        ):
            end += 1

        if end + start + 1 == self.line_to_win:
            return player

        return 0

    def score(self) -> int:
        winner = [
            self.check_win_for_cel(row, col)
            for row in range(self.height)
            for col in range(self.width)
        ]

        score = self.width * self.height - self.move_count + 1

        if any([win == 1 for win in winner]):
            return score
        if any([win == 2 for win in winner]):
            return -score
        return 0

    def move(self, row, col) -> "Board":
        board = Board(self.width, self.height, line_to_win=self.line_to_win)
        board.cells = [row.copy() for row in self.cells]
        board.cells[row][col] = self.current_player()
        board.move_count = self.move_count + 1
        return board


class Player:
    pass


class AiPlayer(Player):
    pass


class HumanPlayer(Player):
    pass


if __name__ == "__main__":
    print("Игра: гомоку")
    print("")
    board = Board(3, 3, line_to_win=3)
    board.show()
    print(board.score())
    board = board.move(1, 1)
    board.show()
    print(board.score())
    board = board.move(1, 0)
    board.show()
    print(board.score())
    board = board.move(0, 0)
    board.show()
    print(board.score())
    board = board.move(2, 0)
    board.show()
    print(board.score())
    board = board.move(2, 2)
    board.show()
    print(board.score())
