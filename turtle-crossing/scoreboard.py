from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard:
    def __init__(self):
        self.level = 1
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(-260, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.turtle.clear()
        self.turtle.write(f"Level: {self.level}", align="left", font=FONT)

    def update_score(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.turtle.goto(0, 0)
        self.turtle.write("GAME OVER", align="center", font=FONT)
