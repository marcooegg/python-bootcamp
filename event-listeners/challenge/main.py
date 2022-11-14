from turtle import Turtle,Screen, width
import random

screen = Screen()
screen.setup(width=500,height=400)

user_bet = screen.textinput(title='Make your bet',prompt='Which turtle you think is going to get to the finish line first?')

colors = ['red','orange','yellow','green','blue','purple']

turtles = []

for color in colors:
    new_turtle = Turtle('turtle')
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.getscreen = screen
    new_turtle.speed(0)
    turtles.append(new_turtle)

x = -220
y = -120
for turtle in turtles:
    turtle.goto(x,y)
    y += 50

while not any(turtle.xcor() >= 250 for turtle in turtles):
    for turtle in turtles:
        turtle.forward(random.randint(1,15))

for turtle in turtles:
    print(f"{turtle.color()},{turtle.xcor()}")


winner = [turtle for turtle in turtles if turtle.xcor() > 250] #turtles.mapped(lambda x: x.xcor() > 250)
winner = winner[0]
winner = winner.color()[0]
if user_bet == winner:
    print("CONGRATULATIONS")
print(f"the turtle that won was the {winner} turtle")

screen.exitonclick()
# soreta = Turtle('turtle',color='red')
# sorete = Turtle('turtle',color='blue')
# soreti = Turtle('turtle',)
# soreto = Turtle('turtle')
# soretu = Turtle('turtle')