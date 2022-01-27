# Snake game
from turtle import Screen
from food import Food
from snake import Snake
import time

GAME_SPEED = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Create a scoreboard

# Detect collision with a wall

# Detect collision with the tail of the snake


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(GAME_SPEED)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()
