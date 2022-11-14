from turtle import Screen
from food import Food
from scoreboard import ScoreBoard
from snake import Snake
import time


TURTLE_SIZE = 20
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
DEAD_X_COOR = SCREEN_WIDTH / 2 - TURTLE_SIZE
DEAD_Y_COOR = SCREEN_HEIGHT / 2 - TURTLE_SIZE


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.title("Snake")

# makes snake move all together
screen.tracer(0)
snake = Snake(TURTLE_SIZE, 10)
food = Food()
scoreboard = ScoreBoard()
# Keybindings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()  # start_moving(snake_body)

    # Detect collision with food
    if snake.head.distance(food) < 15:
        # TODO: snake add body_part
        food.refresh()
        scoreboard.add_point()
        # print()
        snake.create_body_part(previous_square=snake.head)

    # Detect collision with wall
    if (
        snake.head.ycor() > DEAD_Y_COOR
        or snake.head.ycor() < -DEAD_Y_COOR
        or snake.head.xcor() > DEAD_X_COOR
        or snake.head.xcor() < -DEAD_X_COOR
    ):
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake._snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
