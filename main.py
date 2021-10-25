import time
from turtle import Screen
from player import Player
from car_manager import CarManager

from scoreboard import Scoreboard

screen = Screen()
score=Scoreboard()
screen.setup(width=600, height=600)

screen.tracer(0)
screen.listen()
player = Player()
print(player.xcor())
print(player.ycor())
count=0
car_manager = CarManager()
a=0.1
game_is_on = True
while game_is_on:
    time.sleep(a)
    screen.update()
    car_manager.create()
    print(player.ycor())
    for car in car_manager.cars:

        if player.distance(car) <= 20:
            score.game_over()
            print("game over")
            game_is_on = False

    car_manager.move()
    if player.ycor() > 270 :
        score.clear()
        score.increase_level()
        if a>0.05:
            a-=0.04
        player.reset()

    screen.onkeypress(key="Down", fun=player.move_down)
    screen.onkeypress(key="Up", fun=player.move_up)
    screen.onkeypress(key="Left", fun=player.move_left)
    screen.onkeypress(key="Right", fun=player.move_right)


screen.exitonclick()


