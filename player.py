from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
screen = Screen()


class Player(Turtle):

        def __init__(self):
            super().__init__()
            self.shape("turtle")
            #self.color()
            self.penup()
            self.goto(STARTING_POSITION)
            self.setheading(90)

        def move_up(self):
            curr_y = self.ycor()
            if curr_y < 280:
                self.goto(x=self.xcor(), y=curr_y + 20)

        def move_down(self):
            curr_y = self.ycor()
            if curr_y >-280:
                self.goto(x=self.xcor(), y=curr_y - 20)

        def move_left(self):
            curr_x = self.xcor()
            if curr_x >-260:
                self.goto(x=curr_x-20, y=self.ycor())

        def move_right(self):
            curr_x = self.xcor()
            if curr_x <260:
                self.goto(x=curr_x+20, y=self.ycor())

        def reset(self):
            self.goto(STARTING_POSITION)