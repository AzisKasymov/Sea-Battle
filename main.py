import random

# Инициализация поля
pole = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

# First ship
ship1 = [[0, 0], [0, 1], [0, 2], [0, 3]]
palubi1 = 4

# Second ship
ship2 = [[0, 0], [1, 0], [2, 0], [3, 0]]
palubi2 = 4

# Third ship 
ship3 = [[1,2],[2,1]]
palubi3 = 2

def random_ship(ship, palubi):
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    d = random.randint(0, 1)
    if d == 0:
        ship = [[x, y], [x, y + 1], [x, y + 2], [x, y + 3]]
    else:
        ship = [[x, y], [x + 1, y], [x + 2, y], [x + 3, y]]
    palubi = 4
    return ship, palubi

def show_pole():
    for row in pole:
        print('|'.join(row))
        print('-' * 15)

def kuda_strelat(ship, palubi):
    print('Укажите столбец:')
    stolbec = int(input())
    print('Укажите ряд:')
    ryad = int(input())

    if [ryad, stolbec] in ship:
        if pole[ryad][stolbec] != '#':
            print('Попал!')
            pole[ryad][stolbec] = '#'
            palubi -= 1
            if palubi == 0:
                print('Вы потопили корабль!')
    else:
        print('Мимо...')
        pole[ryad][stolbec] = '~'

# Placement of the first ship
ship1, palubi1 = random_ship(ship1, palubi1)

# Placement of the second ship
ship2, palubi2 = random_ship(ship2, palubi2)

# Placement of the third ship
ship3, palubi3 = random_ship(ship3, palubi3)

for i in range(20):  # Увеличил количество попыток для примера
    show_pole()
    kuda_strelat(ship1, palubi1)
    kuda_strelat(ship2, palubi2)
