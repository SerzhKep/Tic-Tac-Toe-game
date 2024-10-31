class Cell:
    def __init__(self, num):
        self.num = num
        self.mark = None

    def is_taken(self):
        return self.mark is not None

    def set_mark(self, mark):
        if not self.is_taken():
            self.mark = mark
            return True

        return False


class Board:

    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def get_cell_mark(self, index):
        return self.cells[index].mark if self.cells[index].mark else str(self.cells[index].num)

    def display(self):
        for i in range(3):
            print('{}|{}|{}'.format(
                self.get_cell_mark(i * 3), self.get_cell_mark(i * 3 + 1), self.get_cell_mark(i * 3 + 2)
            ))

    def make_move(self, cell_num, mark):
        if 1 <= cell_num <= 9:
            return self.cells[cell_num - 1].set_mark(mark)
        return False

    def check_winner(self):
        win_comb = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for combo in win_comb:
            if (self.cells[combo[0]].mark == self.cells[combo[1]].mark == self.cells[combo[2]].mark
                    and self.cells[combo[0]].mark is not None):
                return self.cells[combo[0]].mark
        return None

    def is_full(self):
        return all(cell.is_taken() for cell in self.cells)


class Player:

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def get_move(self):
        while True:
            try:
                move = int(input('{} ({}), введите номер клетки (1-9): '.format(
                    self.name, self.mark
                )))
                if 0 <= move <= 9:
                    return move
                else:
                    print('Введите номер клетки от 1-9.')
            except ValueError:
                print('Введите число!')


class Game:

    def __init__(self):
        self.board = Board()
        self.players = []

    def add_players(self):
        name1 = input("Введите имя первого игрока: ")
        mark1 = input(f"{name1}, выберите X или O: ").upper()
        while mark1 not in ["X", "O"]:
            print("Неверный символ. Выберите X или O.")
            mark1 = input(f"{name1}, выберите X или O: ").upper()

        name2 = input("Введите имя второго игрока: ")
        mark2 = "O" if mark1 == "X" else "X"

        print(f"{name2} получает символ {mark2}.")
        self.players.append(Player(name1, mark1))
        self.players.append(Player(name2, mark2))

    def play_one_turn(self):
        player = self.players[0]
        self.board.display()

        while True:
            move = player.get_move()
            if self.board.make_move(move, player.mark):
                break
            else:
                print('Эта клетка уже занята!')

        winner = self.board.check_winner()
        if winner:
            self.board.display()
            print('Победитель {}'.format(player.name))
            return True

        if self.board.is_full():
            self.board.display()
            print('Ничья')
            return True

        self.players.reverse()
        return False

    def play(self):
        self.add_players()
        while not self.play_one_turn():
            pass

    def start(self):
        # Начало игры с запросом у пользователя
        play = input("Хотите начать игру? (да/нет): ").lower()
        if play == "да":
            self.play()
        else:
            print("Игра завершена.")


game = Game()
game.start()

# |0|1|2|
# |3|4|5|
# |6|7|8|
