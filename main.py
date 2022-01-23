# Snake game
from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Create a snake body
snake = []

x_pos = 0.0
for _ in range(3):
    turtle = Turtle(shape="square")
    turtle.color("white")
    turtle.penup()
    turtle.setx(x_pos)
    x_pos += -20.0
    snake.append(turtle)

# Move the snake

# Control the snake

# Detect collision with food

# Create a scoreboard

# Detect collision with a wall

# Detect collision with the tail of the snake

screen.exitonclick()
