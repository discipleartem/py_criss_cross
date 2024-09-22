from random import choice

# Constants
VERTICAL_COORDS = ('a', 'b', 'c')
HORIZONTAL_COORDS = '123'
ALLOWED_CHARS = ('x', 'o')
EMPTY_CELL = '_'


def is_valid_character(char):
    return char in ALLOWED_CHARS


def prompt_user_input(message):
    return input(message).strip().lower()


def get_character_from_user():
    while True:
        user_char = prompt_user_input('Select char (x, o): ')
        if is_valid_character(user_char):
            return user_char
        print('Character not available. Please choose either "x" or "o".')


def display_game_board(board):
    print('  1 2 3')
    for row_index, row_label in enumerate(VERTICAL_COORDS):
        print(f"{row_label} {' '.join(board[row_index])}")


def is_draw(board):
    return all(EMPTY_CELL not in row for row in board)


def get_coordinates():
    while True:
        coordinates = prompt_user_input('Input coordinates (e.g., a1): ')
        if len(coordinates) == 2 and coordinates[0] in VERTICAL_COORDS and coordinates[1] in HORIZONTAL_COORDS:
            return coordinates[0], int(coordinates[1]) - 1
        print('Invalid coordinates. Ensure input format "a1". Example positions: "a1", "b2".')


def get_player_move(board):
    while True:
        y, x = get_coordinates()
        real_y = VERTICAL_COORDS.index(y)
        if board[real_y][x] == EMPTY_CELL:
            return x, real_y
        print('Position not empty. Please choose an empty cell.')


def get_computer_character(user_char):
    return 'o' if user_char == 'x' else 'x'


def has_winner(char, board):
    lines = board + list(zip(*board))  # Check rows and columns
    lines.append([board[i][i] for i in range(3)])  # Check main diagonal
    lines.append([board[i][2 - i] for i in range(3)])  # Check secondary diagonal
    return any(line == [char] * 3 for line in lines)


def get_random_move_for_computer(board):
    empty_cells = [(x, y) for x in range(3) for y in range(3) if board[y][x] == EMPTY_CELL]
    return choice(empty_cells) if empty_cells else None


# Game class encapsulating game state and behavior
class TicTacToeGame:
    def __init__(self):
        self.board = [[EMPTY_CELL for _ in range(3)] for _ in range(3)]
        self.user_char = get_character_from_user()
        self.computer_char = get_computer_character(self.user_char)

    def play(self):
        while True:
            self.show_board()
            if self.is_draw():
                print('The game is a draw.')
                break
            self.user_turn()
            if self.check_winner(self.user_char):
                print('You win!')
                break
            if self.is_draw():
                print('The game is a draw.')
                break
            self.computer_turn()
            if self.check_winner(self.computer_char):
                self.show_board()
                print('You lose.')
                break

    def show_board(self):
        display_game_board(self.board)

    def is_draw(self):
        return is_draw(self.board)

    def user_turn(self):
        x, y = get_player_move(self.board)
        self.board[y][x] = self.user_char
        self.show_board()

    def computer_turn(self):
        move = get_random_move_for_computer(self.board)
        if move:
            x, y = move
            self.board[y][x] = self.computer_char

    def check_winner(self, char):
        return has_winner(char, self.board)


# Start the game
if __name__ == "__main__":
    game = TicTacToeGame()
    game.play()