from turtle import Turtle,Screen

soreta = Turtle()
screen = Screen()

def fw():
    soreta.forward(10)

def bw():
    soreta.backward(10)

def left():
    soreta.left(10)

def right():
    soreta.right(10)

def clear_screen():
    screen.reset()
    # soreta.goto(0,0)

# soreta.listen()
screen.listen()
screen.onkey(fw,'w')
screen.onkey(bw,'s')
screen.onkey(left,'a')
screen.onkey(right,'d')
screen.onkey(clear_screen,'c')


screen.exitonclick()