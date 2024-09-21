from random import randint

VERTICAL_COORDINATES = ('a', 'b', 'c')


def select_char():
    return input('Select char (x, 0): '.strip(' ').lower())


def get_user_char():
    char = select_char()

    while char not in ('x', '0'):
        print('Not available char')
        char = select_char()
    return char


def show_field(field):
    print(' ', '1', '2', '3')
    for y, v in enumerate(VERTICAL_COORDINATES):
        print(v, ' '.join(field[y]))


def is_draw(field):
    count = 0
    for y in range(3):
        count += 1 if '_' in field[y] else 0
    return count == 0


def input_coordinates():
    return input('Input coordinates: ').lower().strip(' ')


def get_user_position(field):
    real_x, real_y = None, None

    while True:
        y, x = tuple(input_coordinates())

        if int(x) not in range(1, 4) or y not in VERTICAL_COORDINATES:
            print('Not available coordinates')
            continue

        real_x, real_y = int(x) - 1, VERTICAL_COORDINATES.index(y)
        if field[real_y][real_x] == '_':
            break
        else:
            print('Position not empty')
    return real_x, real_y


def get_opponent_char(char):
    return '0' if char == 'x' else 'x'

def is_win(char, field):
    opponent_char = get_opponent_char(char)

    #check lines
    for y in range(3):
        if opponent_char not in field[y] and '_' not in field[y]:
            return True

   #check column
    for x in range(3):
        col = [field[0][x], field[1][x], field[2][x]]
        if opponent_char not in col and '_' not in col:
            return True

    #check diagonal
    first_cross_line = [field[0][0], field[1][1], field[2][2]]
    if opponent_char not in first_cross_line and '_' not in first_cross_line:
        return True

    second_cross_line = [field[0][2], field[1][1], field[2][0]]
    if opponent_char not in second_cross_line and '_' not in second_cross_line:
        return True

    return False

static_field = [
    ['_' for x in range(3)] for y in range(3)
]

user_char = get_user_char()
computer_char = get_opponent_char(user_char)


def get_computer_position(field):
    x, y = randint(0, 2), randint(0, 2)
    while field[y][x] != '_':
        x, y = randint(0, 2), randint(0, 2)
    return x, y


while True:
    show_field(static_field)
    if is_draw(static_field):
        print('is Draw')
        break


    x, y = get_user_position(static_field)
    static_field[y][x] = user_char

    if is_win(user_char, static_field):
        show_field(static_field)
        print('You win')
        break


    x, y = get_computer_position(static_field)
    static_field[y][x] = computer_char

    if is_win(computer_char, static_field):
        show_field(static_field)
        print('You lose')
        break