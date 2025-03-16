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
'a1', 'a2', 'a3'
'b1', 'b2', 'b3'
'c1', 'c2', 'c3' # вертикальные комбинации

'a1', 'b1', 'c1' # горизонтальные комбинации
'a2', 'b2', 'c2'
'a3', 'b3', 'c3'

'a1', 'b2', 'c3' # диагональные комбинации
'a3', 'b2', 'c1'
"""

LETTERS = ['a', 'b', 'c']
NUMBERS = ['1', '2', '3']
ALLOWED_SYMBOLS = ('x', 'o')

player_1 = {'name': 'Игрок 1', 'symbol': None}
player_2 = {'name': 'Игрок 2', 'symbol': None}



def game():
    print('Игра крестики-нолики')
    game_mode()
    field = set_field()
    display_field(field=field)

    global player_1, player_2 # чтобы изменить значения переменных внутри функции
    player_1, player_2 = choose_symbol(player_1, player_2)
    make_move(field)

def game_mode() -> str:
    mode = ['два игрока', 'игрок vs компьютер']

    while True:
        print('Выберите режим игры: ')
        for index, option in enumerate(mode):
            print(f"{index} - {option}")

        choice = input()
        try:
            choice = int(choice)
            if 0 <= choice < len(mode):
                print(f'Выбран режим игры: {mode[choice]}')
                return mode[choice]
        except ValueError:
            print('Неверный ввод. Пожалуйста, введите число.')


def make_move(field: dict) -> None:
    """Организует процесс хода игроков."""
    while True: # бесконечный цикл для ходов
        for player in (player_1, player_2): # перебираем игроков
            move = get_valid_move(player, field)
            field[move] = player['symbol']
            display_field(field=field) # отображение поля после хода

            if is_win(field):
                return  # выход из функции и завершение игры
            elif is_draw(field):
                print("Ничья!")
                return  # выход из функции и завершение игры


def is_win(field: dict) -> bool:
    win_combinations = [
        ['a1', 'a2', 'a3'],
        ['b1', 'b2', 'b3'],
        ['c1', 'c2', 'c3'], # вертикальные комбинации

        ['a1', 'b1', 'c1'], # горизонтальные комбинации
        ['a2', 'b2', 'c2'],
        ['a3', 'b3', 'c3'],

        ['a1', 'b2', 'c3'], # диагональные комбинации
        ['a3', 'b2', 'c1'],
    ]

    for combination in win_combinations:
        if None not in combination:
            if all(field[cell] == 'x' for cell in combination):
                print(f'Победил {player_1["name"]}')
                return True
            elif all(field[cell] == 'o' for cell in combination):
                print(f'Победил {player_2["name"]}')
                return True
    return False
def is_draw(field: dict) -> bool:
    """Проверяет, есть ли ничья."""
    return all(value is not None for value in field.values())

def get_valid_move(player: dict, field: dict) -> str:
    """Запрашивает у игрока ход и проверяет его на корректность."""
    while True:
        move = input(f'{player["name"]}, сделайте ход (например, a1): ').lower().strip()
        if is_validate_move(field, move): # True | False
            return move
def is_validate_move(field: dict, move: str) -> bool:
    """Проверяет корректность и доступность хода."""
    if move not in field:
        print(f'Поля с координатами "{move}" не существует. Используйте формат буква+цифра (например, a1, b2, c3).')
        return False

    if field[move] is not None:
        print(f'Поле "{move}" уже занято. Выберите другое поле.')
        return False

    return True

def choose_symbol(first_player: dict, second_player: dict) -> tuple[dict, dict]:
    first_player['symbol'] = get_player_symbol(first_player['name'])
    second_player['symbol'] = 'o' if first_player['symbol'] == 'x' else 'x'
    print(f'{second_player["name"]} будет играть символом "{second_player["symbol"]}"')

    return first_player, second_player
def get_player_symbol(player_name: str) -> str:
    while True:
        symbol = input(f'Выберите символ для {player_name} (x или o): ').lower().strip()
        if symbol in ALLOWED_SYMBOLS:
            return symbol
        print('Неверный символ. Пожалуйста, выберите x или o.')

def display_field(field: dict) -> None:
    modified_field = {key: "_" if value is None else value for key, value in field.items()}

    print('  ', end=' ') # отступ в начале строки для a, b, c

    for letter in LETTERS:
        print(letter, end=' | ') # разделитель между буквами

    print('', end='\n') # перенос строки

    for number in NUMBERS:
        print(number, end='  ')# отступ между цифрами

        for letter in LETTERS:
            print(modified_field[letter + number], end=" | ") # разделитель между клетками

        print('', end='\n') # перенос после каждой строки
def set_field() -> dict:
    keys = [letter + number for letter in LETTERS for number in NUMBERS]
    default_value = None

    field = dict.fromkeys(keys, default_value)
    return field


if __name__ == '__main__':
    game()