import pygame
import sys
from pygame.locals import *


#initialize Pygame
pygame.init()

#constants
WIDTH, HEIGHT = 600, 400
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10

#Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

#Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout")

#Initialise the ball
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = [5, 5]

#Initialise the paddle 
paddle_pos = [WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30]

