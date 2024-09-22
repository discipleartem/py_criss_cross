from random import choice

# Constants
VERTICAL_COORDS = ('a', 'b', 'c')
HORIZONTAL_COORDS = '123'
ALLOWED_CHARS = ('x', 'o')
EMPTY_CELL = '_'


def is_valid_character(character):
    return character in ALLOWED_CHARS


def prompt_user_input(message):
    return input(message).strip().lower()


def get_user_character():
    while True:
        user_char = prompt_user_input('Select char (x, o): ')
        if is_valid_character(user_char):
            return user_char
        print('Character not available. Please choose either "x" or "o".')


def show_game_board(game_board):
    print('  1 2 3')
    for row_index, row_label in enumerate(VERTICAL_COORDS):
        print(f"{row_label} {' '.join(game_board[row_index])}")


def is_game_draw(game_board):
    return all(EMPTY_CELL not in row for row in game_board)


def get_valid_coordinates():
    while True:
        coordinates = prompt_user_input('Input coordinates (e.g., a1): ')
        if len(coordinates) == 2 and coordinates[0] in VERTICAL_COORDS and coordinates[1] in HORIZONTAL_COORDS:
            return coordinates[0], int(coordinates[1]) - 1
        print('Invalid coordinates. Ensure input format "a1". Example positions: "a1", "b2".')


def get_player_move(game_board):
    while True:
        y, x = get_valid_coordinates()
        real_y = VERTICAL_COORDS.index(y)
        if game_board[real_y][x] == EMPTY_CELL:
            return x, real_y
        print('Position not empty. Please choose an empty cell.')


def get_opponent_character(character):
    return 'o' if character == 'x' else 'x'


def check_winner(character, game_board):
    lines = game_board + list(zip(*game_board))  # Check rows and columns
    lines.append([game_board[i][i] for i in range(3)])  # Check main diagonal
    lines.append([game_board[i][2 - i] for i in range(3)])  # Check secondary diagonal
    return any(line == [character] * 3 for line in lines)


def get_random_computer_move(game_board):
    empty_cells = [(x, y) for x in range(3) for y in range(3) if game_board[y][x] == EMPTY_CELL]
    return choice(empty_cells) if empty_cells else None


# Game class encapsulating game state and behavior
class TicTacToeGame:
    def __init__(self):
        self.game_board = [[EMPTY_CELL for _ in range(3)] for _ in range(3)]
        self.user_char = get_user_character()
        self.computer_char = get_opponent_character(self.user_char)

    def play(self):
        while True:
            show_game_board(self.game_board)
            if is_game_draw(self.game_board):
                print('The game is a draw.')
                break
            x, y = get_player_move(self.game_board)
            self.game_board[y][x] = self.user_char
            show_game_board(self.game_board)
            if check_winner(self.user_char, self.game_board):
                print('You win!')
                break
            if is_game_draw(self.game_board):
                print('The game is a draw.')
                break
            x, y = get_random_computer_move(self.game_board)
            self.game_board[y][x] = self.computer_char
            if check_winner(self.computer_char, self.game_board):
                show_game_board(self.game_board)
                print('You lose.')
                break


# Start the game
if __name__ == "__main__":
    game = TicTacToeGame()
    game.play()