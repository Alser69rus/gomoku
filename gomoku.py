class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[0] * width for _ in range(height)]
        self.cell_chars = {0: " ", 1: "\033[31mX\033[0m", 2: "\033[32mO\033[0m"}
        self.move_count = 1

    def current_player(self):
        return (self.move_count - 1) % 2 + 1

    def show(self):
        print(
            f'{f"Ход {self.move_count}, ходит игрок {self.cell_chars[self.current_player()]}":^{self.width*4+5}}'
        )
        print('   ',end='')
        for i in range(self.width):
            print(f" {i:^{3}}", end="")
        print("")

        print("  ", "-" * (self.width * 4 + 1))
        for i, row in enumerate(self.cells):
            print(f"{i:<3}", end="")
            for cell in row:
                print(f"| {self.cell_chars[cell]} ", end="")
            print("|")
            print('  ',"-" * (self.width * 4 + 1))

    def aviable_moves(self):
        moves = []
        for i in range(self.height):
            for j in range(self.width):
                if self.cells[i][j] == 0:
                    moves.append((i, j))
        return moves


if __name__ == "__main__":
    print("Игра: гомоку")
    print("")
    board = Board(3,3)
    board.show()

