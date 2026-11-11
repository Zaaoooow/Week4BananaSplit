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
#farm sprites
tree = pygame.image.load("assets/farm/tree.png").convert_alpha()
banana = pygame.image.load("assets/items/banana.png").convert_alpha()


# farmer variables
farmer_x = 25
farmer_y = 25
farmer_speed = 2
farmer = farmer_down
# tree variables
tree_positions = [(80, 40), (35, 120), (130, 90)]
# tree trunk collision
tree_hitboxes = []
for tree_x, tree_y in tree_positions:
    tree_hitboxes.append(pygame.Rect(tree_x + 27, tree_y + 74, 19, 5))
#banana variables
banana_positions = [(98, 68), (53, 148), (148, 118)]
#carrying bananas
carrying_bananas = False

# game screen
game_surface = pygame.Surface((game_width, game_height))

clock = pygame.time.Clock()

running = True

while running:
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #carry bananas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e and not carrying_bananas:
                farmer_center_x = farmer_x + farmer.get_width() / 2
                farmer_center_y = farmer_y + farmer.get_height() - 4
                for banana_x, banana_y in banana_positions.copy():
                    banana_center_x = banana_x + banana.get_width() / 2
                    banana_center_y = banana_y + banana.get_height() / 2
                    distance = math.hypot(farmer_center_x - banana_center_x, farmer_center_y - banana_center_y)
                    if distance < 40:
                        banana_positions.remove((banana_x, banana_y))
                        carrying_bananas = True
                        break
                

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
    old_x = farmer_x
    old_y = farmer_y
    farmer_x += move_x * farmer_speed
    farmer_y += move_y * farmer_speed

    #keeping farmer inside game screen
    farmer_x = max(0, min(farmer_x, (game_width // 2) - farmer.get_width()))
    farmer_y = max(0, min(farmer_y, game_height - farmer.get_height()))
    #check tree collision
    for hitbox in tree_hitboxes:
        farmer_rect = pygame.Rect(farmer_x + 8, farmer_y + farmer.get_height() - 8, farmer.get_width() - 16, 8)
        if farmer_rect.colliderect(hitbox):
            farmer_x = old_x
            farmer_y = old_y

    #draw background
    game_surface.blit(farm_background, (0,0))
    #draw tree and farmer
    objects = []

    #add trees to objects
    for tree_x, tree_y in tree_positions:
        objects.append((tree_y + 79, tree, tree_x, tree_y))

    #add farmer to objects
    objects.append((farmer_y + farmer.get_height(), farmer, farmer_x, farmer_y))

    #sort objects from back to front
    objects.sort(key = lambda obj: obj[0])

    #draw farmer and tree
    for depth, image, x, y, in objects:
        game_surface.blit(image, (x, y))

    #draw bananas
    for banana_x, banana_y in banana_positions:
        game_surface.blit(banana, (banana_x, banana_y))

    #draw carried bananas
    if carrying_bananas:
        banana_x = farmer_x + 10
        banana_y = farmer_y + 15
        carried_banana = banana
        if farmer == farmer_up:
            banana_x = farmer_x + 0
            banana_y = farmer_y - 26
            carried_banana = banana
        elif farmer == farmer_down:
            banana_x = farmer_x - 6
            banana_y = farmer_y + 18
            carried_banana = pygame.transform.flip(banana, True, True)
        elif farmer == farmer_right:
            banana_x = farmer_x + 18
            banana_y = farmer_y - 0
            carried_banana = pygame.transform.rotate(banana, -90)
        elif farmer == farmer_left:
            banana_x = farmer_x - 26
            banana_y = farmer_y - 6
            carried_banana = pygame.transform.rotate(banana, 90)
        elif farmer == farmer_up_right:
            banana_x = farmer_x + 0 
            banana_y = farmer_y - 30
            carried_banana = pygame.transform.rotate(banana, -45)
        elif farmer == farmer_up_left:
            banana_x = farmer_x - 25
            banana_y = farmer_y - 26
            carried_banana = pygame.transform.rotate(banana, 45)
        elif farmer == farmer_down_right:
            banana_x = farmer_x + 6
            banana_y = farmer_y + 4
            carried_banana = pygame.transform.rotate(banana, -135)
        elif farmer == farmer_down_left:
            banana_x = farmer_x - 24
            banana_y = farmer_y + 3
            carried_banana = pygame.transform.rotate(banana, 135)

        game_surface.blit(carried_banana, (banana_x, banana_y))

    #scale game to window
    scaled_surface = pygame.transform.scale(game_surface, (window_width, window_height))

    #display game
    screen.blit(scaled_surface, (0,0))
    pygame.display.flip()

    #limit fps
    clock.tick(fps)

pygame.quit()

