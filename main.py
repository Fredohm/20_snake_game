# Snake game
from turtle import Screen
from snake import Snake
import time

GAME_SPEED = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Detect collision with food

# Create a scoreboard

# Detect collision with a wall

# Detect collision with the tail of the snake


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(GAME_SPEED)

    snake.move()

screen.exitonclick()
