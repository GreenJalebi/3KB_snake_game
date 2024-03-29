from turtle import Turtle
HOME = (0, 270)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.score = 0
        self.setposition(HOME)
        self.write(f"Score: {self.score}", True, "center", ("Calibri", 16, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 16, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.setposition(HOME)
        self.write(f"Score: {self.score}", True, "center", ("Calibri", 16, "bold"))

