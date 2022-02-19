from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


# Create a scoreboard
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.best_score = self.read_best_score()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.goto(-300, 270)
        self.pendown()
        self.forward(600)
        self.penup()
        self.goto(0, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} \tBest Score: {self.read_best_score()}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.read_best_score():
            self.write_new_best_score()
        self.score = 0
        self.update_scoreboard()

    def read_best_score(self):
        with open("data.txt") as data:
            self.best_score = int(data.read())
            return self.best_score

    def write_new_best_score(self):
        with open("data.txt", mode="w") as data:
            data.write(f"{self.score}")

    # def game_over(self):
    #     self.setposition(0.0, 0.0)
    #     self.pencolor("black")
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
