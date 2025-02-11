"""
Задача: написать игру крестики-нолики для двух игроков.
- Добавить возможность выбора символа (x или o) и ходов.
- Режим игры два игрока
- проверка на занятость клетки
- проверка на победу
- проверка на ничью
"""
# Игровое поле можно представить в виде словаря с ключами a, b, c и значениями в виде списка [].
FIELD = [None, None, None,
         None,None,None,
         None,None,None]


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

        # Ход второго игрока
        make_move("player2", sym2)

        #TODO: проверка на занятость клетки
        #TODO: проверка на победу
        #TODO: проверка на ничью

def make_move(player, symbol):
    player_cor = input(f'Введите координаты для {player}: ')
    FIELD[int(player_cor)] = symbol
    print(FIELD)


if __name__ == '__main__':
    game()