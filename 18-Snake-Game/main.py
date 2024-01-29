from turtle import Screen
from snake import Snake
from food import Food

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Street Game")
screen.tracer(0)

snake = Snake()
food = Food()


