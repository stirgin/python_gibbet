import random
import turtle
import sys

# Комментарий

'''
Многострочный
комментарий
x = random.randrange(1, 100)
'''

def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def draw_line(from_x, from_y, to_x, to_y):
    gotoxy(from_x, from_y)
    turtle.goto(to_x, to_y)

def draw_circle(x, y ,r):
    gotoxy(x, y)
    turtle.circle(r)

def draw_gibbet_element(step):
    if step == 1:
        draw_line(-160, -100, -160, 80)
    elif step == 2:
        draw_line(-160, 80, -80, 80)
    elif step == 3:
        draw_line(-160, 40, -120, 80)
    elif step == 4:
        draw_line(-100, 80, -100, 40)
    elif step == 5:
        draw_circle(-100, 0, 20)
    elif step == 6:
        draw_line(-100, 0, -100, -50)
    elif step == 7:
        draw_line(-100, -10, -120, -20)
    elif step == 8:
        draw_line(-100, -10, -80, -20)
    elif step == 9:
        draw_line(-100, -50, -120, -60)
    elif step == 10:
        draw_line(-100, -50, -80, -60)


x = random.randint(1, 100)
#print(type(x))
print('Случайное число: ', x)


gotoxy(-200, 200)
turtle.write("Загадано число от 1 до 100. \n попробуй угадать!", \
             font=("Arial", 18, "normal"))

ans = turtle.textinput("Хотите играть?", "y/n")

if ans == 'n':
    sys.exit(13)

ans = turtle.textinput("Давать подсказки?", "y/n")
hints = ans == 'y'
#if ans == 'y':
#    hints = True

try_count = 1

while True:
    number = turtle.numinput("Поробуй угадать", "Число", 0, 0, 100)

    if hints:
        turtle.color("black")
        gotoxy(170, 200 - try_count * 15)
        if x > number:
            turtle.write(str(number) + ' Загаданное число больше')
        elif x < number:
            turtle.write(str(number) + ' Загаданное число меньше')

    if number == x:
        gotoxy(-150, -200)
        turtle.color('green')       #color((150, 45, 78))
        turtle.write("Вы угадали", font=("Arial", 24, "normal"))
        break
    else:
        gotoxy(-150, -200)
        turtle.color("red")
        turtle.write("Неверно", font=("Arial", 20, "normal"))
        draw_gibbet_element(try_count)
        try_count += 1
        if try_count == 10:
            gotoxy(-150, -150)
            turtle.color('brown')
            turtle.write("Вы проиграли", font=("Arial", 20, "normal"))
            break

'''
turtle.circle(30)
gotoxy(140, 200)
turtle.circle(30)
gotoxy(-70, 200)
turtle.circle(30)
'''

input('Нажмите Enter')
#input('Нажмите Enter')

# apt-get install python3-tk

#SublimeREPL