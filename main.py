# Snake game
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

GAME_SPEED = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Detect collision with the tail of the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(GAME_SPEED)

    snake.move()

    # Detect collision with food and increase scoreboard
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

    # Detect collision with a wall
    x_pos = snake.head.xcor()
    y_pos = snake.head.ycor()
    if x_pos < -295 or x_pos > 296 or y_pos < -295 or y_pos > 266:
        screen.bgcolor("red")
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()
