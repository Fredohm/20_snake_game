# Snake game
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


# Create a snake body
def create_snake():
    segments = []

    x_pos = 0.0
    for _ in range(3):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setx(x_pos)
        x_pos += -20.0
        segments.append(new_segment)
    return segments


# Move the snake

# Control the snake

# Detect collision with food

# Create a scoreboard

# Detect collision with a wall

# Detect collision with the tail of the snake

# game on
game_is_on = True
snake = create_snake()
while game_is_on:
    screen.update()
    time.sleep(0.2)
    for segment in snake:
        segment.forward(10)


screen.exitonclick()
