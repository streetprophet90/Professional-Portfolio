from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()


screen.exitonclick()
