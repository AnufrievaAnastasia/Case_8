import turtle
import math

def get_color_choice():

    color = input('Допустимые цвета заливки:\n'
      'red\n'
      'blue\n'
      'green\n'
      'yellow\n'
      'orange\n'
      'magenta\n'
      'pink\n'
      'Пожалуйста, введите цвет: ').lower()

    list_color = ['red', 'blue', 'green', 'yellow', 'orange', 'magenta','pink']
    while color not in list_color:
        print("'", color, "' ", 'не является верным значением. Пожалуйста, повторите попытку: ', sep='')
        color = input().lower()
    return color

def get_num_hexagons():
    try:
        number = int(input('Пожалуйста, введите количество шестиугольников, располагаемых в ряд: '))
        while number > 20 or number < 4:
            print('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ')
            number = int(input())
        return number
    except ValueError:
        print('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ')
        number = get_num_hexagons()

color1 = get_color_choice()
color2 = get_color_choice()
number = get_num_hexagons()

def draw_hexagon(x, y, side_len):
    '''

    :param x: upper left corner coordinate x
    :param y: upper left corner coordinate y
    :param side_len: side length of a hexagon
    :param color:
    :return: None
    '''

    turtle.up()
    turtle.setposition(x, y)
    for i in range(number):
        for j in range(number):
            turtle.down()
            if j % 2 == 0:
                turtle.color(color1)
            else:
                turtle.color(color2)
            turtle.left(90)
            turtle.forward(side_len)
            turtle.right(60)
            turtle.forward(side_len)
            turtle.right(60)
            turtle.forward(side_len)
            turtle.right(60)
            turtle.forward(side_len)
            turtle.right(60)
            turtle.forward(side_len)
            turtle.right(60)
            turtle.forward(side_len)
            turtle.right(150)
            turtle.up()
            turtle.forward(side_len*math.sqrt(3))
        turtle.right(120)
        turtle.forward(side_len)
        turtle.left(30)
        turtle.forward(side_len)
        turtle.right(90)
        turtle.forward((side_len*math.sqrt(3))*number)
        turtle.right(180)


x = int(input('Введите координату х: '))
y = int(input('Введите координату у: '))
d_2 = 250
d_2_n = d_2 // number
side_len = int((3**0.5) / 2 * d_2_n)
draw_hexagon(x,y,side_len)
