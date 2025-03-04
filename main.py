"""
Задача: написать игру крестики-нолики для двух игроков.
- Добавить возможность выбора символа (x или o) и ходов.
- Режим игры два игрока
- проверка на занятость клетки
- проверка на победу
- проверка на ничью

Дополнительные задачи:
- добавить возможность выбора режима игры (два игрока, компьютер против игрока и т.д.)
"""

"""выигрышные последовательности
0 1 2   3 4 5    6 7 8
0 3 6   1 4 7    2 5 8
0 4 8   2 4 6
"""

"""
расположение цифровой клавиатуры
------------
| 7 | 8 | 9 |
| 4 | 5 | 6 |
| 1 | 2 | 3 |
------------
"""

#сравнить https://github.com/samalexpro375/TicTacToe.git


# TODO: рефакторизация

# Игровое поле можно представить в виде списка [].
FIELD = [None, None, None,
         None, None, None,
         None, None, None]


def game():
    print('Игра крестики-нолики')
    player1_sym , player2_sym = choose_sym()
    order(player1_sym, player2_sym)


def choose_sym():
    ALLOWED_SYMBOLS = ('x', 'o')
    while True:
        player1_sym = input('Выберите символ для первого игрока (x или o): ').lower()
        if player1_sym in ALLOWED_SYMBOLS:
            player2_sym = 'o' if player1_sym == 'x' else 'x'
            print(f'игроку_1 присвоено "{player1_sym}", игроку_2 присвоено "{player2_sym}"')
            return player1_sym, player2_sym
        else:
            print('Неверный символ, только "x" или "o" (en)')


def order(sym1, sym2):
    print(f'Первый ходит игрок_1 с символом "{sym1}"')

    while True:
        # Ход первого игрока
        make_move("игрок_1", sym1)
        display_field()
        if is_win():
            print(f'Победил игрок_1')
            break

        elif is_draw():
            print('Ничья')
            break

        # Ход второго игрока
        make_move("игрок_2", sym2)
        display_field()
        if is_win():
            print(f'Победил игрок_2')
            break


def make_move(player, symbol):
    while True:
        player_cor = input(f'Введите координаты для {player}: ')

        #TODO: переписать
        """#numpad_to_index = {
            '7': 0, '8': 1, '9': 2,
            '4': 3, '5': 4, '6': 5,
            '1': 6, '2': 7, '3': 8
        }"""
        match player_cor:
            case '7':
                if not is_presence(FIELD[0]):
                    FIELD[0] = symbol
                    break
                else:
                    print("Эта клетка уже занята!")
            case '8':
                if not is_presence(FIELD[1]):
                    FIELD[1] = symbol
                    break
                else:
                    print("Эта клетка уже занята!")
            case '9':
                if not is_presence(FIELD[2]):
                    FIELD[2] = symbol
                    break
                else:
                    print("Эта клетка уже занята!")
            case '4':
                if not is_presence(FIELD[3]):
                    FIELD[3] = symbol
                    break
                else:
                    print("Эта клетка уже занята!")
            case '5':
                if not is_presence(FIELD[4]):
                    FIELD[4] = symbol
                    break
                else:
                    print("Эта клетка уже занята!")
            case '6':
                if not is_presence(FIELD[5]):
                    FIELD[5] = symbol
                    break
                else:
                    print("Эта клетка уже занята!")
            case '1':
                if not is_presence(FIELD[6]):
                    FIELD[6] = symbol
                    break
                else:
                    print("Эта клетка уже занята!")
            case '2':
                if not is_presence(FIELD[7]):
                    FIELD[7] = symbol
                    break
                else:
                    print("Эта клетка уже занята!")
            case '3':
                if not is_presence(FIELD[8]):
                    FIELD[8] = symbol
                    break
                else:
                    print("Эта клетка уже занята!")
            case _:
                print('Неверный символ, только цифры от 1 до 9')
                continue



def display_field():
    field = list(map(lambda x: '_' if x is None else x, FIELD))
    print('------------')
    print(f"| {field[0]} | {field[1]} | {field[2]} |")
    print(f"| {field[3]} | {field[4]} | {field[5]} |")
    print(f"| {field[6]} | {field[7]} | {field[8]} |")
    print('------------')

def is_presence(cell):
    return cell is not None

def is_win():
    # Создаем кортежи для проверки выигрышных комбинаций
    rows = ((0, 1, 2), (3, 4, 5), (6, 7, 8))  # горизонтали
    cols = ((0, 3, 6), (1, 4, 7), (2, 5, 8))  # вертикали
    diags = ((0, 4, 8), (2, 4, 6))  # диагонали

    for combination in rows + cols + diags:
        if FIELD[combination[0]] == FIELD[combination[1]] == FIELD[combination[2]] is not None:
            return True
    return False

# проверка на ничью
def is_draw():
    return None not in FIELD #None - это пустая клетка, если все клетки заполнены, то None не будет

if __name__ == '__main__':
    game()