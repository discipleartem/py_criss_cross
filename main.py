# сравнить https://github.com/samalexpro375/TicTacToe.git
"""
Задача: написать игру крестики-нолики для двух игроков.
- Добавить возможность выбора символа (x или o) и ходов.
- Режим игры два игрока
- проверка на занятость клетки
- проверка на победу
- проверка на ничью

Дополнительные задачи:
- добавить возможность выбора режима игры (два игрока, компьютер против игрока и т.д.)
- добавить возможность выбора размера игрового поля (3x3, 4x4, 5x5 и т.д.)
"""

""" вообразим виртуальное игровое поле 3x3
   | a | b | c |
------------------
1  |   |   |   |
   -------------
2  |   |   |   |
   -------------
3  |   |   |   |
   -------------   
"""


"""выигрышные последовательности
0 1 2   3 4 5    6 7 8
0 3 6   1 4 7    2 5 8
0 4 8   2 4 6
"""

letters = ['a', 'b', 'c']
numbers = ['1', '2', '3']
keys = [letter + number for letter in letters for number in numbers]
default_value = None
FIELD = dict.fromkeys(keys, default_value)
ALLOWED_SYMBOLS = ('x', 'o')
player_1 = {'name': 'Игрок 1', 'symbol': None}
player_2 = {'name': 'Игрок 2', 'symbol': None}


def game():
    print('Игра крестики-нолики')
    display_field()

    global player_1, player_2
    player_1, player_2 = choose_symbol(player_1, player_2)



def choose_symbol(first_player: dict, second_player: dict) -> tuple[dict, dict]:
    first_player['symbol'] = get_player_symbol(first_player['name'])
    second_player['symbol'] = 'o' if first_player['symbol'] == 'x' else 'x'

    print(f'Символ {first_player["symbol"]} уже выбран. '
          f'{second_player["name"]} будет играть символом {second_player["symbol"]}.')

    return first_player, second_player


def get_player_symbol(player_name: str) -> str:
    while True:
        symbol = input(f'Выберите символ для {player_name} (x или o): ').lower().strip()
        if symbol in ALLOWED_SYMBOLS:
            return symbol
        print('Неверный символ. Пожалуйста, выберите x или o.')

def display_field():
    field = {key: "_" if value is None else value for key, value in FIELD.items()}

    print('  ', end=' ') # отступ в начале строки для a, b, c

    for letter in letters:
        print(letter, end=' | ') # разделитель между буквами

    print('', end='\n') # перенос строки

    for number in numbers:
        print(number, end='  ')# отступ между цифрами

        for letter in letters:
            print(field[letter + number], end=" | ") # разделитель между клетками

        print('', end='\n') # перенос после каждой строки


if __name__ == '__main__':
    game()