from tracemalloc import start
from turtle import Turtle,Screen
import colorgram
import random

def extract_color_for_turtle(color:colorgram) -> tuple:
    return (color.rgb.r,color.rgb.g,color.rgb.b)


colors = colorgram.extract('./static/hirst-1.jpg',30)
rgb_colors = []
for color in colors:
    if color.proportion < 0.12:
        rgb_colors.append(extract_color_for_turtle(color))
    # print(color.proportion)

# print(rgb_colors)
main_color = rgb_colors[0]
rgb_colors.remove(main_color)
screen = Screen()
screen.colormode(255)
screen.bgcolor(main_color)
soreta = Turtle('arrow',visible=True)
soreta.speed(9)
soreta.pensize(9)

def draw_dot(turtle: Turtle,size):
    turtle.dot(size,random.choice(rgb_colors))

def paint_hirst_square(turtle:Turtle,side_size:int,factor:int):
    size = side_size * factor
    start_location = size/2 * -1
    turtle.penup()
    turtle.goto(start_location,start_location)
    for row in range(side_size):
        for column in range(side_size):
            turtle.forward(factor)
            draw_dot(turtle,20)
        turtle.goto(start_location,start_location+(row+1)*factor)
    turtle.hideturtle()
        
        
        
    # turtle.goto(0,side_size)
    # draw_dot(turtle)
    # turtle.goto(side_size,0)
    # draw_dot(turtle)
    # turtle.goto(side_size,side_size)
    # draw_dot(turtle)



paint_hirst_square(soreta,10,50)
screen.exitonclick()