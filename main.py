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



#сравнить https://github.com/samalexpro375/TicTacToe.git



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
        player1_sym = input('Выберите символ для первого игрока (x или o): ').strip().lower()
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
        display_field()
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
        player_cor = input(f'Введите координаты для {player}: ').strip().lower()

        numpad_to_index = {
            '7': 0, '8': 1, '9': 2,
            '4': 3, '5': 4, '6': 5,
            '1': 6, '2': 7, '3': 8
        }

        if player_cor in numpad_to_index:
            cell = numpad_to_index[player_cor]
            if is_presence(FIELD[cell]):
                print('Клетка занята')
            else:
                FIELD[cell] = symbol
                break
        else:
            print('Неверные координаты, введите цифры от 1 до 9')



def display_field():
    print("""для координат вы можете использовать расположение цифровой клавиатуры:
------------
| 7 | 8 | 9 |
| 4 | 5 | 6 |
| 1 | 2 | 3 |
------------""")
    field = list(map(lambda x: '_' if x is None else x, FIELD)) #заменяем None на '_'

    #отрисовываем игровое поле
    print('------------')
    for i in range(0, 9, 3):
        print(f"| {field[i]} | {field[i + 1]} | {field[i + 2]} |")
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