from turtle import Screen, Turtle
from player import Player

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

player = Player()

screen.listen()


screen.exitonclick()
