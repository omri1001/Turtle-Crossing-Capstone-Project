import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
turtle=Player()
car_manager=CarManager()
screen.title("TURTLE CROSSING")
scoreboard = Scoreboard()
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(turtle.move_player, "Up")
    car_manager.create_cars()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            turtle.squish()
            game_is_on = False
            scoreboard.game_over()

    if turtle.is_at_finishline() == True:
        turtle.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



screen.exitonclick()