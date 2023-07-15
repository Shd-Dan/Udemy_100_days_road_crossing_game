import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.make_newcar()
    car.move_car()

    # Detect collision with a car
    for item in car.all_cars:
        if item.distance(turtle) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Turtle reaches a finish
    if turtle.is_finish():
        turtle.back_to_start()
        car.level_up()
        scoreboard.increase_level()

screen.exitonclick()