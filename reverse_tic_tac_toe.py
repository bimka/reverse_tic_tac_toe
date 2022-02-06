import random
import numpy as np

# Размеры поля
size = 10
# Пройгрышная комбинация
combo = 5

# Матрица с которой будем работать
field = [[' ' for i in range(size)] for j in range(size)]
#field = np.ones((size, size))
""""""
def arr_to_list(arr):
    """
    Функция arr_to_list возвращает список с игровым полем
    """
    field = arr.tolist() 
    i = 0
    while i < size: 
        j = 0
        while j < size:
            field[i][j] = ' '
            j += 1
        i += 1

def field_rendering(field):
    """
    Функция field_rendering отрисовывает игровое поле
    """
    def next_letter(row):
        """
        Функция next_letter возвращает следующую букву алфавита
        """
        return chr(ord(row) + 1) 
    

    col = 1
    row = 'a'
    hor_sep = ' ' * 3 + '-' * (size * 4 + 1)
    
    row_coord = ' ' * 5
    # Начинаем отрисовку игрового поля
    for i in field:
        row_coord += f'{row}   '
        row = next_letter(row)
    print(row_coord)
    print(hor_sep)
    i = 0
    while i < len(field):
        j = 0
        print(f'{col}  ', end = '')
        while j < len(field):
            cell = f'| {field[i][j]} '
            print(f'{cell}', end = '')           
            j += 1
        print('|')
        print(hor_sep)
        col += 1
        i += 1

def opponents_move(field):
    """
    Функция opponents_move возвращает координтахода компьютера
    """
    row, col = random.choice(range(4)), random.choice(range(4))
    if field[row][col] != ' ':
        opponents_move(field)
    print(row, col)
    return (row, col)

user_input = 'b3'

def trans_coord(user_input):
    """
    Функция trans_coord возвращает координату списка, куда пользователь 
    делает ход
    """
    if len(user_input) != 2:
        game(messages[1])
    else:
        if user_input[0].isalpha() and user_input[1].isdigit():
            coord1 = int(ord(user_input[0].lower())) - 97
            coord2 = int(user_input[1]) - 1
            if field[coord2][coord1] != ' ':
                game(messages[2])
            return (coord2, coord1)
        else:
            game(messages[1])

messages = [
    "Добро пожаловать в игру обратные крестики нолики. Проигрывает тот игрок, "
    "у которого в один ряд по горизонтили, вертикали или диагонали выстраиваются ходы.", 
    "Не корректный ввод. Повторите попытку.",
    "Ваш ход."
    "Эта клетка занята. Выберете другую."
]


def game(messages):
    '''
    Функция game возвращает игровое поле с ходами противников
    '''
    while True:
        user_input = input("Введите координату, куда будете ходить. Например, 'b3':  ")
        user_coord = trans_coord(user_input)
        field[user_coord[0]][user_coord[1]] = 'x'   
        opponents_coord = opponents_move(field)
        field[opponents_coord[0]][opponents_coord[1]] = 'o'
        field_rendering(field)
        check_comb(combo, field, mark = 'x')        
        check_comb(combo, field, mark = 'o')

def check_comb(combo, field, mark):
    """
    Функция check_comb проверяет сошлась ли пройгрушная комбинация
    """

    def check_hor(field):
        """
        Функция check_hor проверяет сошлась ли комбинация по горизонтали
        """
        for i in field:
            col = 0
            check = 0
            for j in i:
                if j == mark:
                    check += 1
                else:
                    check = 0
                if check == combo:
                        print(f'{mark} проиграл. Игра окончена')
                        exit()
                col += 1

    def diags_field(field, combo):
        """
        Функция diags_field возвращает список с диагоналями которые больше combo
        """
        diags = [field.diagonal(i) for i in range(-3,4)]
        diags.extend(field.diagonal(i) for i in range(3,-4,-1))
        diags_satis = []
        for i in diags:
            if len(i) >= combo:
                diags_satis.append(i)
        #print(diags_satis)
        return diags_satis

    # Поверим матрицу по горизонтали
    check_hor(field)
    # Транспонируем матрицу и также проверяем ее по горизонтали
    field = np.transpose(field)
    check_hor(field)
    field = np.transpose(field)
    # Проверяем диагонали матрицы
    check_hor(diags_field(field, combo))   
print(messages[0])
game(messages[0])

