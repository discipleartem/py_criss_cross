from random import randint


VERTICAL_COORDINATS = ('a', 'b', 'c')

def get_user_char():
    user_char = input('Select char (x, 0): ').strip(' ').lower()
    while user_char not in ('x', '0'):
        print('Not available char')
        user_char = input('Select char (x, 0): ').strip(' ').lower()
    return user_char

def show_field(field):
    print(' ', '1', '2', '3')
    for y, v in enumerate(VERTICAL_COORDINATS):
        print(v, ' '.join(field[y]))


def is_draw(field):
    count = 0
    for y in range(3):
        count += 1 if '_' in field[y] else 0
    return count == 0


def get_user_position(field):
    real_x, real_y = None, None
    while True:
        coordinats = input('Input coordinats: ').lower().strip(' ')
        y, x = tuple(coordinats)

        if int(x) not in range(1, 4) or y not in VERTICAL_COORDINATS:
            print('Not available coordinats')
            continue

        real_x, real_y = int(x) - 1, VERTICAL_COORDINATS.index(y)
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
    diag1 = [field[0][0], field[1][1], field[2][2]]
    if opponent_char not in diag1 and '_' not in diag1:
        return True

    diag2 = [field[0][2], field[1][1], field[2][0]]
    if opponent_char not in diag2 and '_' not in diag2:
        return True

    return False

field = [
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
    show_field(field)
    if is_draw(field):
        print('is Draw')
        break


    x, y = get_user_position(field)
    field[y][x] = user_char

    if is_win(user_char, field):
        print('You win')
        break


    x, y = get_computer_position(field)
    field[y][x] = computer_char

    if is_win(computer_char, field):
        print('You lose')
        break