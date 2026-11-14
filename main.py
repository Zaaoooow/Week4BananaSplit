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
cutting_board = pygame.image.load("assets/backgrounds/cutting_board.png").convert_alpha()
# character sprites
farmer_up = pygame.image.load("assets/characters/farmer_up.png").convert_alpha()
farmer_down = pygame.image.load("assets/characters/farmer_down.png").convert_alpha()
farmer_right = pygame.image.load("assets/characters/farmer_right.png").convert_alpha()
farmer_left = pygame.image.load("assets/characters/farmer_left.png").convert_alpha()
farmer_up_right = pygame.image.load("assets/characters/farmer_up_right.png").convert_alpha()
farmer_up_left = pygame.image.load("assets/characters/farmer_up_left.png").convert_alpha()
farmer_down_right = pygame.image.load("assets/characters/farmer_down_right.png").convert_alpha()
farmer_down_left = pygame.image.load("assets/characters/farmer_down_left.png").convert_alpha()
farmer = farmer_down
#farm sprites
tree = pygame.image.load("assets/farm/tree.png").convert_alpha()
banana = pygame.image.load("assets/items/banana.png").convert_alpha()
conveyor = pygame.image.load("assets/farm/conveyor.png").convert_alpha()
dropoff = pygame.image.load("assets/farm/dropoff.png").convert_alpha()
# cutting board sprites
receiving_box = pygame.image.load("assets/cutting_board/receiving_box.png").convert_alpha()
large_unpeeled_banana = pygame.image.load("assets/items/large_unpeeled_banana.png").convert_alpha()
large_peeled_banana = pygame.image.load("assets/items/large_peeled_banana.png").convert_alpha()
large_cut_banana = pygame.image.load("assets/items/large_cut_banana.png").convert_alpha()
tray = pygame.image.load("assets/items/tray.png").convert_alpha()
vanilla_button = pygame.image.load("assets/items/vanillabutton.png").convert_alpha()
chocolate_button = pygame.image.load("assets/items/chocolatebutton.png").convert_alpha()
strawberry_button = pygame.image.load("assets/items/strawberrybutton.png").convert_alpha()
vanilla_scoop = pygame.image.load("assets/items/vanilla_scoop.png").convert_alpha()
strawberry_scoop = pygame.image.load("assets/items/strawberry_scoop.png").convert_alpha()
chocolate_scoop = pygame.image.load("assets/items/chocolate_scoop.png").convert_alpha()


#dropoff hitbox
dropoff_rect = pygame.Rect(0, 215, 80, 30)
#receiving box hitbox
receiving_box_rect = pygame.Rect(240, 220, 80, 60)
#cutting board hitbox
cutting_board_rect = pygame.Rect(275, 26, 170, 190)
#large banana rect peeled
large_banana_rect = pygame.Rect(0, 0, 0, 0)

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
banana_positions = [[98, 68, 0], [53, 148, 0], [148, 118, 0]]
#carrying bananas
carrying_bananas = False
delivered_bananas = 0
conveyor_bananas = []
#mouse interaction
dragging_banana = False
dragged_banana_x = 0
dragged_banana_y = 0
batch_on_board = False
banana_peeled = False
banana_cut = False
left_half_x = 0
right_half_x = 0
#tray variables
tray_x = cutting_board_rect.centerx - tray.get_width() // 2
tray_y = - tray.get_height() # start above screen
tray_target_y = 47
tray_speed = 2
tray_visible = False
#ice button variables
button_y = -150
button_target_y = 50
button_speed = 2
buttons_arrived = False
buttons_visible = False
# ice cream variables
scoop_count = 0
selected_scoops = []
scoop_positions = [(0, 0), (0, 0), (0, 0)]
scoop_images = {
    "chocolate": chocolate_scoop,
    "strawberry": strawberry_scoop,
    "vanilla": vanilla_scoop
}

# game screen
game_surface = pygame.Surface((game_width, game_height))

#font
font = pygame.font.Font(None, 16)

clock = pygame.time.Clock()

running = True

while running:
    #events
    #respawn bananas after 6.7 seconds
    for item in banana_positions:
        if item[2] != 0:
            if pygame.time.get_ticks() - item[2] >= 6700:
                item[2] = 0
    #tray animation
    if tray_visible and tray_y < tray_target_y:
        tray_y += tray_speed
        if tray_y > tray_target_y:
            tray_y = tray_target_y
    #ice button animation
    if tray_visible and tray_y >= tray_target_y:
        buttons_visible = True
    if buttons_visible and button_y < button_target_y:
        button_y += button_speed
        if button_y > button_target_y:
            button_y = button_target_y
            buttons_arrived = True
    #check if farmer is near dropoff
    farmer_rect = pygame.Rect(farmer_x + 5, farmer_y + farmer.get_height() - 8, farmer.get_width() - 16, 8)
    near_dropoff = farmer_rect.colliderect(dropoff_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                # Collect bananas
                if not carrying_bananas:
                    farmer_center_x = farmer_x + farmer.get_width() / 2
                    farmer_center_y = farmer_y + farmer.get_height() - 4
                    for item in banana_positions:
                        if item[2] == 0:
                            banana_x = item[0]
                            banana_y = item[1]
                            banana_center_x = banana_x + banana.get_width() / 2
                            banana_center_y = banana_y + banana.get_height() / 2
                            distance = math.hypot(farmer_center_x - banana_center_x, farmer_center_y - banana_center_y)
                            if distance < 40:
                                item[2] = pygame.time.get_ticks() 
                                carrying_bananas = True
                                break
                # Deliver bananas
                elif near_dropoff:
                    carrying_bananas = False
                    delivered_bananas += 1
                    banana_x = 20
                    banana_y = 230
                    conveyor_bananas.append([banana_x, banana_y, pygame.time.get_ticks()])
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("mouse click detected")
            mouse_x = event.pos[0] * game_width // window_width
            mouse_y = event.pos[1] * game_height // window_height
            # ice cream mouse collision
            if buttons_visible and banana_cut and scoop_count < 3:
                chocolate_rect = pygame.Rect(295, button_y - 30, chocolate_button.get_width(), chocolate_button.get_height())
                strawberry_rect = pygame.Rect(345, button_y - 30, strawberry_button.get_width(), strawberry_button.get_height())
                vanilla_rect = pygame.Rect(395, button_y - 30, vanilla_button.get_width(), vanilla_button.get_height())
                if chocolate_rect.collidepoint(mouse_x, mouse_y):
                    print("chocolate selected")
                    selected_scoops.append("chocolate")
                    scoop_count += 1
                elif strawberry_rect.collidepoint(mouse_x, mouse_y):
                    print("strawberry selected")
                    selected_scoops.append("strawberry")
                    scoop_count += 1
                elif vanilla_rect.collidepoint(mouse_x, mouse_y):
                    print("vanilla selected")
                    selected_scoops.append("vanilla")
                    scoop_count += 1
            #large banana collision
            if batch_on_board and large_banana_rect.collidepoint(mouse_x, mouse_y):
                if not banana_peeled:
                    banana_peeled = True
                elif not banana_cut:
                    banana_cut = True
                    left_half_x = 0
                    right_half_x = 0
                    tray_visible = True
            #cuttong board collision check
            if not dragging_banana and not batch_on_board:
            #pickup banan batch
                for item in conveyor_bananas:
                    banana_rect = pygame.Rect(item[0], item[1], banana.get_width(), banana.get_height())
                    if banana_rect.collidepoint(mouse_x, mouse_y) and item[0] >= 270:
                        dragging_banana = True
                        conveyor_bananas.remove(item)
                        break
        # drop banana batch
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if dragging_banana:
                mouse_x = event.pos[0] * game_width // window_width
                mouse_y = event.pos[1] * game_height //  window_height
                if cutting_board_rect.collidepoint(mouse_x, mouse_y):
                    batch_on_board = True
                    banana_peeled = False
                    banana_cut = False
                else:
                    conveyor_bananas.append([270, 230, pygame.time.get_ticks()])
                dragging_banana = False
    #track mouse while dragging banana
    if dragging_banana:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dragged_banana_x = mouse_x * game_width // window_width - 10
        dragged_banana_y = mouse_y * game_height // window_height - 10

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
    farmer_y = max(0, min(farmer_y, game_height - 48 - farmer.get_height()))

    #check if farmer is near dropoff
    farmer_rect = pygame.Rect(farmer_x + 5, farmer_y + farmer.get_height() - 8, farmer.get_width() - 16, 8)
    near_dropoff = farmer_rect.colliderect(dropoff_rect)
    #check tree collision
    for hitbox in tree_hitboxes:
        farmer_rect = pygame.Rect(farmer_x + 8, farmer_y + farmer.get_height() - 8, farmer.get_width() - 16, 8)
        if farmer_rect.colliderect(hitbox):
            farmer_x = old_x
            farmer_y = old_y

    #draw background
    game_surface.blit(farm_background, (0, 0))
    game_surface.blit(cutting_board, (0, 0))
    #draw receive box
    game_surface.blit(receiving_box, (0, 0))
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
    for item in banana_positions:
        if item[2] == 0:
            game_surface.blit(banana, (item[0], item[1]))

    #draw dropoff and conveyor belt
    game_surface.blit(conveyor, (0,0))
    game_surface.blit(dropoff, (0,0))

    #dropped off bananas
    for item in conveyor_bananas:
        if pygame.time.get_ticks() - item[2] >= 500:
            if item[0] < 270:
                item[0] += 1
        game_surface.blit(banana, (item[0], item[1]))

    #banana while dragging
    if dragging_banana:
        game_surface.blit(banana, (dragged_banana_x, dragged_banana_y))
    # draw tray
    if tray_visible:
        game_surface.blit(tray, (tray_x, tray_y))
    #draw ice cream buttons
    if buttons_visible:
        game_surface.blit(chocolate_button, (295, button_y - 30))
        game_surface.blit(strawberry_button, (345, button_y - 30))
        game_surface.blit(vanilla_button, (395, button_y - 30))
    #draw large banana
    if batch_on_board:
        large_x = cutting_board_rect.centerx - large_unpeeled_banana.get_width() // 2
        large_y = cutting_board_rect.centery- large_unpeeled_banana.get_height() // 2
        scoop_positions = [
            (large_x + 15, large_y + 27),
            (large_x + 20, large_y + 52),
            (large_x + 15, large_y + 77)
        ]
        if banana_cut:
            middle = large_cut_banana.get_width() // 2
            left_half = large_cut_banana.subsurface((0, 0, middle, large_cut_banana.get_height()))
            right_half = large_cut_banana.subsurface((middle, 0, large_cut_banana.get_width() - middle, large_peeled_banana.get_height()))
            if left_half_x > - 12:
                left_half_x -= 1
            if right_half_x < 12:
                right_half_x += 1
            game_surface.blit(left_half, (large_x + left_half_x - 36, large_y - 2))
            game_surface.blit(right_half, (large_x + middle + right_half_x - 36, large_y - 2))
        elif banana_peeled:
            game_surface.blit(large_peeled_banana, (large_x - 36, large_y - 2))
        else:
            game_surface.blit(large_unpeeled_banana, (large_x, large_y))
        
        for i, flavor in enumerate(selected_scoops):
            scoop_image = scoop_images[flavor]
            scoop_rect = scoop_image.get_rect(center = (scoop_positions[i]))
            game_surface.blit(scoop_image, scoop_rect)
        large_banana_rect = pygame.Rect(large_x, large_y, large_unpeeled_banana.get_width(), large_unpeeled_banana.get_height())

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

    #delivered banana count
    delivered_text = font.render(f"Delivered: {delivered_bananas}", True, (255, 255, 255))
    game_surface.blit(delivered_text, (10, 10))

    #scale game to window
    scaled_surface = pygame.transform.scale(game_surface, (window_width, window_height))

    #display game
    screen.blit(scaled_surface, (0,0))
    pygame.display.flip()

    #limit fps
    clock.tick(fps)

pygame.quit()

