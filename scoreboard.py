from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.goto(-270,260)

        self.level=1
        self.write(f"Level: {self.level} ",False,align="left",font=FONT)

    def increase_level(self):
        self.level+=1

        self.write(f"Level: {self.level} ", False, align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over \nYour score = {self.level-1}",False, align="center", font=FONT)



