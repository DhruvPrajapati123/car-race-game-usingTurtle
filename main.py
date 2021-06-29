import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
screen.listen()
score = Scoreboard()

screen.onkey(key="Up", fun=player.up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    # detect the collision with car

    for i in car.all_cars:
        if i.distance(player) < 20:
            game_is_on = False
            score.game_over()

    # detect when turtle finished crossing road

    if player.ycor() > player.FINISH_LINE_Y:
        player.goto(player.STARTING_POSITION)
        # car increase his speed
        car.level_up()
        score.update_score()

screen.exitonclick()
