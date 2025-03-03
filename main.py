"""
Задача: написать игру крестики-нолики для двух игроков.
- Добавить возможность выбора символа (x или o) и ходов.
- Режим игры два игрока
- проверка на занятость клетки
- проверка на победу
- проверка на ничью
"""

"""выигрышные последовательности
0 1 2   3 4 5    6 7 8
0 3 6   1 4 7    2 5 8
0 4 8   2 4 6
"""



# Игровое поле можно представить в виде списка [].
FIELD = [None, None, None,
         None, None, None,
         None, None, None]


def game():
    print('Игра крестики-нолики')

    player1_sym = input('Выберите символ для первого игрока (x или o): ')
    player2_sym = input('Выберите символ для второго игрока (x или o): ')

    order(player1_sym, player2_sym)

def order(sym1, sym2):
    print(f'Первый ходит игрок player1 с символом {sym1}')

    while True:
        # Ход первого игрока
        make_move("player1", sym1)
        if is_win():
            print(f'Победил игрок player1')
            break

        elif draw():
            print('Ничья')
            break

        # Ход второго игрока
        make_move("player2", sym2)
        if is_win():
            print(f'Победил игрок player2')
            break




def make_move(player, symbol):
    while True:
        player_cor = input(f'Введите координаты для {player}: ')
        if is_presence(player_cor):
            break

    FIELD[int(player_cor)] = symbol #int() - преобразование в число ибо индекс списка int, а input() - строка
    print(FIELD)


def is_presence(player_cor):
    if FIELD[int(player_cor)] is not None:
        print(f"Клетка занята {FIELD[int(player_cor)]}")
        return False
    else:
        return True

#TODO: проверка на победу
def is_win():
    # горизонтальные последовательности
    if FIELD[0] == FIELD[1] == FIELD[2] or \
       FIELD[3] == FIELD[4] == FIELD[5] or \
       FIELD[6] == FIELD[7] == FIELD[8]:
        return True

    # вертикальные последовательности
    elif FIELD[0] == FIELD[3] == FIELD[6] or \
       FIELD[1] == FIELD[4] == FIELD[7] or \
       FIELD[2] == FIELD[5] == FIELD[8]:
        return True

    # диагональные последовательности
    elif FIELD[0] == FIELD[4] == FIELD[8] or \
       FIELD[2] == FIELD[4] == FIELD[6]:
        return True


#TODO: проверка на ничью
def draw():
    pass

if __name__ == '__main__':
    game()