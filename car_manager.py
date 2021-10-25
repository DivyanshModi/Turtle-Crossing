from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
            #super().__init__()
            self.cars=[]

            self.create()
    def create(self):
        a=random.randint(1,5)
        if a==1:
            self.new_car=Turtle()
            self.new_car.shape("circle")
            x=random.randint(0,5)
            self.new_car.color(COLORS[x])
            self.new_car.penup()
            self.new_car.shapesize(stretch_wid=1,stretch_len=2)
            rand_y = random.randint(-200, 200)

            self.new_car.goto(x=280, y=rand_y)
            #self.new_car.left(90)
            self.cars.append(self.new_car)
            self.move()
            #self.forward(100)

    def move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

#    def game_over(self):

            #self.forward(10)
