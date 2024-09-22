from random import randint

# Constants
VERTICAL_COORDS = ('a', 'b', 'c')
HORIZONTAL_COORDS = '123'
ALLOWED_CHARS = ('x', '0')
EMPTY_CELL = '_'


def is_valid_character(character):
    return character in ALLOWED_CHARS


def prompt_user_input(message):
    return input(message).strip().lower()


def get_user_character():
    user_char = prompt_user_input('Select char (x, 0): ')
    while not is_valid_character(user_char):
        print('Character not available')
        user_char = prompt_user_input('Select char (x, 0): ')
    return user_char


def show_game_board(game_board):
    print(' ', '1', '2', '3')
    for row_index, row_label in enumerate(VERTICAL_COORDS):
        print(row_label, ' '.join(game_board[row_index]))


def is_game_draw(game_board):
    return all(EMPTY_CELL not in row for row in game_board)


def get_valid_coordinates():
    while True:
        coordinates = prompt_user_input('Input coordinates (e.g., a1): ')
        if len(coordinates) == 2 and coordinates[0] in VERTICAL_COORDS and coordinates[1] in HORIZONTAL_COORDS:
            return coordinates[0], int(coordinates[1]) - 1
        print('Invalid coordinates. Please try again.')


def get_player_move(game_board):
    while True:
        y, x = get_valid_coordinates()
        real_y = VERTICAL_COORDS.index(y)
        if game_board[real_y][x] == EMPTY_CELL:
            return x, real_y
        else:
            print('Position not empty')


def get_opponent_character(character):
    return '0' if character == 'x' else 'x'


def check_winner(character, game_board):
    lines = game_board + list(zip(*game_board))  # Check rows and columns
    lines.append([game_board[i][i] for i in range(3)])  # Check main diagonal
    lines.append([game_board[i][2 - i] for i in range(3)])  # Check secondary diagonal
    return any(line == [character] * 3 for line in lines)


def get_random_computer_move(game_board):
    x, y = randint(0, 2), randint(0, 2)
    while game_board[y][x] != EMPTY_CELL:
        x, y = randint(0, 2), randint(0, 2)
    return x, y


# Game loop
game_board = [[EMPTY_CELL for _ in range(3)] for _ in range(3)]
user_char = get_user_character()
computer_char = get_opponent_character(user_char)
while True:
    show_game_board(game_board)
    if is_game_draw(game_board):
        print('The game is a draw.')
        break
    x, y = get_player_move(game_board)
    game_board[y][x] = user_char
    if check_winner(user_char, game_board):
        show_game_board(game_board)
        print('You win!')
        break
    if is_game_draw(game_board):
        print('The game is a draw.')
        break
    x, y = get_random_computer_move(game_board)
    game_board[y][x] = computer_char
    if check_winner(computer_char, game_board):
        show_game_board(game_board)
        print('You lose.')
        break
