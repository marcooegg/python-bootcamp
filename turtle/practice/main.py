from turtle import Turtle, Screen
import random
def draw_square(turtle, size):
    for x in range(4):
        turtle.forward(size)
        turtle.left(90)
def draw_dashed_line(turtle, distance, section):
    count = 0
    while count < distance:
        count += section
        turtle.forward(section)
        alter_pen(turtle)

def alter_pen(turtle):
    if turtle.isdown():
        turtle.penup()
    else:
        turtle.pendown()

def draw_shape(turtle,side_count):
    angle = 360/side_count
    for side in range(side_count):
        turtle.forward(100)
        turtle.right(angle)

def change_random_color(turtle):
    screen = turtle.getscreen()
    r = random.randint(0,screen.colormode())
    g = random.randint(0,screen.colormode())
    b = random.randint(0,screen.colormode())
    turtle.pencolor((r,g,b))

def rotate_random(turtle,max_turn=180):
    options = ['left','right','none']
    choice = random.choice(options)
    if choice == 'left':
        turtle.left(random.randint(1,max_turn))
    elif choice == 'right':
        turtle.right(random.randint(1,max_turn))



screen = Screen()
screen.colormode(255)
soreta = Turtle()
soreta.shape('turtle')
soreta.color("green")
#1
# draw_square(soreta,100)
#2 
# draw_dashed_line(soreta,500,10)
#3
# shapes = [3,4,5,6,7,8,9,10]
# for sides in range(3,11):
#     change_random_color(screen,soreta)
#     draw_shape(soreta,sides)
#4

# for walk in range(150):
#     change_random_color(screen,soreta)
#     soreta.forward(20)
#     rotate_random(soreta)
#     soreta.pensize(random.randint(1,10))
#     soreta.speed(random.randint(1,10))

#5 uses similar random color as previous exercises
#6
# soreta.speed(0)
# for x in range(72):
#     soreta.circle(100)
#     change_random_color(soreta)
#     soreta.left(5)


screen.exitonclick()

