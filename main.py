"""
Задача: написать игру крестики-нолики для двух игроков.
- Добавить возможность выбора символа (x или o) и ходов.
- Режим игры два игрока.

Дополнительные задачи:
    - Добавить матч с компьютером.
    - Добавить возможность выбора размера поля (по умолчанию 3x3).
"""

""" вообразим виртуальное игровое поле 3x3
     | a | b | c |
     
  1  |   |   |   |
     -------------
  2  |   |   |   |
     -------------
  3  |   |   |   |
     -------------   
"""
# Игровое поле можно представить в виде словаря с ключами a, b, c и значениями в виде списка [].
FIELD = {'a': [], 'b': [], 'c': []}
ALLOWED_SYMBOLS = ['x', 'o']

def game():
    print('Игра крестики-нолики')

    player1 = choose_symbol('player1')
    player2 = choose_symbol('player2')
    print(player1, player2)


def choose_symbol(player):
    if len(ALLOWED_SYMBOLS) == 1:
        print(f'{player} вам достался символ: {ALLOWED_SYMBOLS[0]}')
        return ALLOWED_SYMBOLS[0]
    else:
        print(f'Выберите символ для {player}: x или o')
        symbol = validate_symbol()
        return symbol


def validate_symbol():
    symbol = input().lower().strip()  # lower() - приводит к нижнему регистру, strip() - удаляет пробелы

    if symbol not in ALLOWED_SYMBOLS:
        print(f"Некорректный символ! Выберите один из: {ALLOWED_SYMBOLS} [en]")
        return validate_symbol()

    if len(ALLOWED_SYMBOLS) > 1:
        ALLOWED_SYMBOLS.remove(symbol)  # удаляем выбранный символ из списка доступных символов
    return symbol


if __name__ == '__main__':
    game()