import random
pole = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
      

ship = [[0, 0], [0, 1], [0, 2], [0, 3]]
palubi = 4    #----

def random_ship():
  global ship
  x = random.randint(0, 4)
  y = random.randint(0, 4)
  d = random.randint(0, 1)
  if d == 0:
    ship = [[x, y], [x, y+1], [x, y+2], [x, y+3]]
  else:
    ship = [[x, y], [x+1, y], [x+2, y], [x+3, y]]


def show_pole():
  for row in pole:
    print('*'.join(row))
    print('_'*15)

def kuda_strelat():
  global palubi      #---
  print('choose column:')
  stolbec = int(input())
  print('indicate the row:')
  ryad = int(input())

  if [ryad, stolbec] in ship:
    if pole[ryad][stolbec] != '#':   #----
      print('hit!')
      pole[ryad][stolbec] = '#'
      palubi = palubi - 1
      if palubi == 0:
        print('you win!!')
  else:
    print('missed...')
    pole[ryad][stolbec] = '~'


show_pole()
random_ship()
for i in range(10):
  kuda_strelat()
  show_pole()
