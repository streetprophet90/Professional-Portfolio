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

#Game Loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddle 
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and paddle_pos[0] > 0:
        paddle_pos[0] -= 5
    if keys[K_RIGHT] and paddle_pos[0] < WIDTH - PADDLE_WIDTH:
        paddle_pos[0] += 5

    #Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    #Bounce off the walls
    if ball_pos[0] <= 0 or ball_pos[0] >= WIDTH - BALL_RADIUS * 2:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] <= 0:
        ball_speed[1] = -ball_speed[1]

    #Bounce off the paddle
    if {
        paddle_pos[1] <= ball_pos[1] <= paddle_pos[1] + PADDLE_HEIGHT
        and paddle_pos[0] <= ball_pos[0] <= paddle_pos[0] + PADDLE_WIDTH
    }:
        ball_speed[1] = -ball_speed[1]

# Draw everything
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (int(ball_pos[0]), int(ball_pos[1])), BALL_RADIUS)
    pygame.draw.rect(screen, BLUE, (paddle_pos[0], paddle_pos[1], PADDLE_WIDTH, PADDLE_HEIGHT))

    pygame.display.flip()
    clock.tick(60)