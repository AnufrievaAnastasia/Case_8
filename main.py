import turtle


def get_color_choice():

    color = input('Допустимые цвета заливки:\n'
      'красный\n'
      'синий\n'
      'зеленый\n'
      'желтый\n'
      'оранжевый\n'
      'пурпурный\n'
      'розовый\n'
      'Пожалуйста, введите цвет: ').lower()

    list_color = ['красный', 'синий', 'зеленый', 'желтый', 'оранжевый', 'пурпурный','розовый']
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

def draw_hexagon(x, y, side_len, color):

    d_2 = 250
    d_2_n = d_2 // number # это d в зависимости от количества фигур
    s = int((3**0.5) / 2 * d_2_n) # это длина стороны шестиугольника
