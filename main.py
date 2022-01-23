# Snake game
from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


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



screen.exitonclick()
