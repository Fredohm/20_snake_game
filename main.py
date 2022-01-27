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


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(GAME_SPEED)

    snake.move()

    # Detect collision with food and increase scoreboard
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with a wall
    x_pos = snake.head.xcor()
    y_pos = snake.head.ycor()
    if x_pos < -301 or x_pos > 300 or y_pos < -300 or y_pos > 266:
        screen.bgcolor("red")
        print(x_pos)
        print(y_pos)
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with the tail of the snake
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            screen.bgcolor("red")
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
