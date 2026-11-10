import pygame
import math
from settings import *

# Initialize game
pygame.init()

# Create game window
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(Title)

# background sprites
farm_background = pygame.image.load("assets/backgrounds/farm.png").convert_alpha()
# character sprites
farmer_up = pygame.image.load("assets/characters/farmer_up.png").convert_alpha()
farmer_down = pygame.image.load("assets/characters/farmer_down.png").convert_alpha()
farmer_right = pygame.image.load("assets/characters/farmer_right.png").convert_alpha()
farmer_left = pygame.image.load("assets/characters/farmer_left.png"). convert_alpha()
farmer_up_right = pygame.image.load("assets/characters/farmer_up_right.png").convert_alpha()
farmer_up_left = pygame.image.load("assets/characters/farmer_up_left.png").convert_alpha()
farmer_down_right = pygame.image.load("assets/characters/farmer_down_right.png").convert_alpha()
farmer_down_left = pygame.image.load("assets/characters/farmer_down_left.png").convert_alpha()
farmer = farmer_down

# farmer variables
farmer_x = 100
farmer_y = 100
farmer_speed = 2
farmer = farmer_down

game_surface = pygame.Surface((game_width, game_height))

clock = pygame.time.Clock()

running = True

while running:
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #keyboard input
    keys = pygame.key.get_pressed()
    move_x = 0
    move_y = 0
    if keys[pygame.K_w]:
        move_y -= 1
    if keys[pygame.K_s]:
        move_y += 1
    if keys[pygame.K_a]:
        move_x -= 1
    if keys[pygame.K_d]:
        move_x += 1

    if move_x == 0 and move_y == -1:
        farmer = farmer_up
    elif move_x == 0 and move_y == 1:
        farmer = farmer_down
    elif move_x == -1 and move_y == 0:
        farmer = farmer_left
    elif move_x == 1 and move_y == 0:
        farmer = farmer_right
    elif move_x == -1 and move_y == -1:
        farmer = farmer_up_left
    elif move_x == 1 and move_y == -1:
        farmer = farmer_up_right
    elif move_x == 1 and move_y == 1:
        farmer = farmer_down_right
    elif move_x == -1 and move_y == 1:
        farmer = farmer_down_left

    length = math.hypot(move_x, move_y)
    if length > 0:
        move_x /= length
        move_y /= length
    farmer_x += move_x * farmer_speed
    farmer_y += move_y * farmer_speed
    


    #draw background
    game_surface.blit(farm_background, (0,0))
    #draw farmer
    game_surface.blit(farmer, (farmer_x, farmer_y))

    #scale game to window
    scaled_surface = pygame.transform.scale(game_surface, (window_width, window_height))

    #display game
    screen.blit(scaled_surface, (0,0))
    pygame.display.flip()

    #limit fps
    clock.tick(fps)

pygame.quit()

