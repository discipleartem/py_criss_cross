from random import randint

VERTICAL_COORDINATES = ('a', 'b', 'c')
ALLOWED_CHARS = ('x', '0')


def is_valid_char(char):
    return char in ALLOWED_CHARS


def get_char_input(prompt):
    return input(prompt).strip().lower()


def get_user_choice():
    user_char = get_char_input('Select char (x, 0): ')
    while not is_valid_char(user_char):
        print('Character not available')
        user_char = get_char_input('Select char (x, 0): ')
    return user_char


def display_field(field):
    print(' ', '1', '2', '3')
    for y, v in enumerate(VERTICAL_COORDINATES):
        print(v, ' '.join(field[y]))


def is_draw(field):
    return all('_' not in row for row in field)


def get_user_coordinates():
    while True:
        coordinates = get_char_input('Input coordinates (e.g., a1): ')
        if len(coordinates) == 2 and coordinates[0] in VERTICAL_COORDINATES and coordinates[1] in '123':
            return coordinates[0], int(coordinates[1]) - 1
        print('Invalid coordinates. Please try again.')


def get_user_move(field):
    while True:
        y, x = get_user_coordinates()
        real_y = VERTICAL_COORDINATES.index(y)
        if field[real_y][x] == '_':
            return x, real_y
        else:
            print('Position not empty')


def get_opponent_char(char):
    return '0' if char == 'x' else 'x'


def has_winner(char, field):
    lines = field + list(zip(*field))  # Check rows and columns
    lines.append([field[i][i] for i in range(3)])  # Check main diagonal
    lines.append([field[i][2 - i] for i in range(3)])  # Check secondary diagonal
    return any(line == [char] * 3 for line in lines)


def get_computer_move(field):
    x, y = randint(0, 2), randint(0, 2)
    while field[y][x] != '_':
        x, y = randint(0, 2), randint(0, 2)
    return x, y


# Game loop
game_field = [['_' for x in range(3)] for y in range(3)]
user_char = get_user_choice()
computer_char = get_opponent_char(user_char)
while True:
    display_field(game_field)
    if is_draw(game_field):
        print('The game is a draw.')
        break
    x, y = get_user_move(game_field)
    game_field[y][x] = user_char
    if has_winner(user_char, game_field):
        display_field(game_field)
        print('You win!')
        break
    if is_draw(game_field):
        print('The game is a draw.')
        break
    x, y = get_computer_move(game_field)
    game_field[y][x] = computer_char
    if has_winner(computer_char, game_field):
        display_field(game_field)
        print('You lose.')
        break
