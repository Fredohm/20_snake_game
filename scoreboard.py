from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


# Create a scoreboard
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.penup()
        self.goto(-300, 270)
        self.pendown()
        self.forward(600)
        self.penup()
        self.goto(0, 275)
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

