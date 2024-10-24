from board import Board
from player import Player, HumanPlayer
from ai import AiPlayer


def choose_player(player_name: str) -> Player:
    while True:
        print(f"Выберите игрока: {player_name}")
        print("1. Человек")
        print("2. Компьютер")
        choice = int(input())
        if choice == 1:
            return HumanPlayer()
        elif choice == 2:
            return AiPlayer()
        else:
            print("Некорректный ввод")


class Game:
    def __init__(self, board: Board, player1: Player, player2: Player):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.winner = None

    def play(self):
        while True:
            self.board.show()
            if self.current_player == self.player1:
                row, col = self.player1.get_move(self.board)
            else:
                row, col = self.player2.get_move(self.board)
            self.board = self.board.move(row, col)
            if self.board.score() > 0:
                self.winner = self.player1
                break
            if self.board.score() < 0:
                self.winner = self.player2
                break

        print("")
        if self.winner is None:
            print("Ничья")
        elif self.winner == self.player1:
            print("Победил игрок X")
        else:
            print("Победил игрок O")


if __name__ == "__main__":
    print("Игра: гомоку")
    print("")

    player1 = choose_player("X")
    player2 = choose_player("O")

    game = Game(Board(3, 3, line_to_win=3), player1, player2)
    game.play()
