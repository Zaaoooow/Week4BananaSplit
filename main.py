import pygame
import math
import random
from settings import *

# Initialize game
pygame.init()
pygame.mixer.init()

# Create game window
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption(Title)

game_state = "menu"

#sound effects
clicksound = pygame.mixer.Sound("assets/sounds/click.wav")
cutsound = pygame.mixer.Sound("assets/sounds/cut.mp3")
pickupsound = pygame.mixer.Sound("assets/sounds/pickup.mp3")
peelsound = pygame.mixer.Sound("assets/sounds/peel.mp3")
scoopsound = pygame.mixer.Sound("assets/sounds/scoop.mp3")
serve_sound = pygame.mixer.Sound("assets/sounds/order.mp3")
dropoffsound = pygame.mixer.Sound("assets/sounds/dropoff.mp3")
currentmusic = None
def play_music(filename):
    global currentmusic
    if currentmusic != filename:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        currentmusic = filename

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
serve_button = pygame.image.load("assets/items/serve_button.png").convert_alpha()
serve_button_rect = serve_button.get_rect(center = (350, 246))
complete_orders = 0
#game over and win/lose
win_screen = pygame.image.load("assets/backgrounds/win_screen.png").convert_alpha()
lose_screen = pygame.image.load("assets/backgrounds/lose_screen.png").convert_alpha()
final_win_screen = pygame.image.load("assets/backgrounds/final_win_screen.png").convert_alpha()
final_lose_screen = pygame.image.load("assets/backgrounds/final_lose_screen.png").convert_alpha()
#main menu
main_menu = pygame.image.load("assets/backgrounds/mainmenu.png").convert_alpha()
play_button = pygame.image.load("assets/ui/playbutton.png").convert_alpha()
guide_button = pygame.image.load("assets/ui/guidebutton.png").convert_alpha()
guide_screen = pygame.image.load("assets/backgrounds/guide_screen.png").convert_alpha()
stats_button = pygame.image.load("assets/ui/statsbutton.png").convert_alpha()
stats_screen = pygame.image.load("assets/backgrounds/stats_screen.png").convert_alpha()

#animation 
secret_background = pygame.image.load("assets/backgrounds/secret_background.png").convert_alpha()
secret_rocket = pygame.image.load("assets/backgrounds/secret_rocket.png").convert_alpha()
secret_sky = pygame.image.load("assets/backgrounds/secret_sky.png").convert_alpha()
rocket_bounds = secret_rocket.get_bounding_rect()
secret_rocket = secret_rocket.subsurface(rocket_bounds).copy()
guide_font = pygame.font.Font(None, 20)
secret_font = pygame.font.Font(None, 12)
secret_city = pygame.image.load("assets/backgrounds/secret_city.png").convert_alpha()
secret_city = pygame.transform.scale(secret_city, (game_width, game_height))
secret_city_slime = pygame.image.load("assets/backgrounds/secret_city_slime.png").convert_alpha()
secret_city_slime = pygame.transform.scale(secret_city_slime, (game_width, game_height))
second_object = pygame.image.load("assets/backgrounds/second_object.png").convert_alpha()
second_object = pygame.transform.scale(second_object, (max(1, second_object.get_width()//4), max(1, second_object.get_height() // 4)))
second_object = pygame.transform.rotate(second_object, 180)
secret_city_destroyed = pygame.image.load("assets/backgrounds/destroyed_city.png").convert_alpha()
secret_city_destroyed = pygame.transform.scale(secret_city_destroyed, (game_width, game_height))


#menu
stats_button_rect = pygame.Rect(170, 180, 140, 25)
play_button_rect = pygame.Rect(170, 97, 140, 25)
guide_button_rect = pygame.Rect(170, 137, 140, 25)
#dropoff hitbox
dropoff_rect = pygame.Rect(0, 215, 80, 30)
#receiving box hitbox
receiving_box_rect = pygame.Rect(240, 220, 80, 60)
#cutting board hitbox
cutting_board_rect = pygame.Rect(275, 26, 170, 190)
#large banana rect peeled
large_banana_rect = pygame.Rect(0, 0, 0, 0)
#win lose rects
win_screen_rect = win_screen.get_rect(center = (game_width // 2, game_height // 2))
lose_screen_rect = lose_screen.get_rect(center = (game_width // 2, game_height // 2))
final_lose_screen_rect = final_lose_screen.get_rect(center = (game_width // 2, game_height // 2))
final_win_screen_rect = final_win_screen.get_rect(center = (game_width // 2, game_height // 2))

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
# banan split
banana_split_complete = False

# game timer and score
game_time = 60
target_orders = 6
start_time = pygame.time.get_ticks()
game_over = False
game_won = False

#stats
games_played = 0
games_won = 0
games_lost = 0
total_orders = 0
highest_orders = 0

#animation variables
secret_stage = 0
secret_timer = 0
rocket_x = 228
rocket_y  = 170
rocket_speed = 1
smoke_particles = []
stars = []
for i in range(60):
    star_x = random.randint(0, game_width - 1)
    star_y = random.randint(0, game_height - 1)
    stars.append([star_x, star_y]) 
city_rocket = pygame.transform.scale(
    secret_rocket,
    (max(1, secret_rocket.get_width() // 4),
     max(1, secret_rocket.get_height() // 4))
)
city_rocket = pygame.transform.rotate(city_rocket, 180)
city_rocket_y = -30
city_rocket_speed = 0.4
slime_radius = 0
slime_exploding = False
slime_shrinking = False
slime_hold_timer = 0
slime_reveal_timer = 0
second_rocket_y = -30
second_rocket_speed = 1
second_rocket_hit = False
final_explosion_radius = 0
final_explosion_timer = 0
city_destroyed = False
destroyed_timer = 0
ending_fade = 0

try:
    with open("stats.txt", "r") as file:
        stats = file.readlines()
        games_played = int(stats[0])
        games_won = int(stats[1])
        games_lost = int(stats[2])
        total_orders = int(stats[3])
        highest_orders = int(stats[4])
except FileNotFoundError:
    pass

#levels
level = 1

# game screen
game_surface = pygame.Surface((game_width, game_height))

#font
font = pygame.font.Font(None, 16)

clock = pygame.time.Clock()

running = True

while running:
    #events
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    time_left = max(0, game_time - elapsed_time)
    # check win lose
    if game_state == "playing" and not game_over:
        if complete_orders >= target_orders:
            game_won = True
            game_over = True
        elif time_left <= 0:
            game_over = True
    # record stats
        if game_over:
            games_played += 1
            if game_won:
                games_won += 1
            else:
                games_lost += 1
            if complete_orders > highest_orders:
                highest_orders = complete_orders
            with open("stats.txt", "w") as file:
                file.write(f"{games_played}\n")
                file.write(f"{games_won}\n")
                file.write(f"{games_lost}\n")
                file.write(f"{total_orders}\n")
                file.write(f"{highest_orders}\n")
    if game_state == "secret_ending":
        pygame.mixer.music.stop() 
    elif game_state == "menu" or game_state == "guide" or game_state == "stats":
        play_music("assets/sounds/menumusic.mp3")
    elif game_over:
        if game_won:
            play_music("assets/sounds/win.mp3")
        else:
            play_music("assets/sounds/loss.mp3")
    else:
        play_music("assets/sounds/gamemusic.mp3")
    #respawn bananas after 6.7 seconds
    for item in banana_positions:
        if item[2] != 0:
            if pygame.time.get_ticks() - item[2] >= 15000:
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
                                pickupsound.play()
                                break
                # Deliver bananas
                elif near_dropoff:
                    carrying_bananas = False
                    delivered_bananas += 1
                    dropoffsound.play()
                    banana_x = 20
                    banana_y = 230
                    conveyor_bananas.append([banana_x, banana_y, pygame.time.get_ticks()])
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if game_state == "menu":
                mouse_x = event.pos[0] * game_width // window_width
                mouse_y = event.pos[1] * game_height // window_height
                if play_button_rect.collidepoint(mouse_x, mouse_y):
                    clicksound.play()
                    level = 1
                    game_time = 60
                    target_orders = 6
                    game_over = False
                    game_won = False
                    game_state = "playing"
                    start_time = pygame.time.get_ticks()
                    continue
                elif guide_button_rect.collidepoint(mouse_x, mouse_y):
                    clicksound.play()
                    game_state = "guide"
                    continue
                elif stats_button_rect.collidepoint(mouse_x, mouse_y):
                    clicksound.play()
                    game_state = "stats"
                    continue
            if game_state == "guide" or game_state == "stats":
                game_state = "menu"
                continue
            if game_over:
                if level == 1 and game_won:
                    level = 2
                    game_time = 90
                    target_orders = 13
                elif level == 2 and game_over:
                    game_state = "menu"
                    level = 1
                    game_time = 60
                    target_orders = 6
                else:
                    level = 1
                    game_time = 60
                    target_orders = 6
                complete_orders = 0
                game_over = False
                game_won = False
                start_time = pygame.time.get_ticks()
                delivered_bananas = 0
                farmer_x = 25
                farmer_y = 25
                farmer = farmer_down
                carrying_bananas = False
                banana_positions = [[98, 68, 0], [53, 148, 0], [148, 118, 0]]
                conveyor_bananas = []
                dragging_banana = False
                batch_on_board = False
                banana_peeled = False
                banana_cut = False
                scoop_count = 0
                selected_scoops = []
                banana_split_complete = False
                tray_visible = False
                tray_y = -tray.get_height()
                buttons_visible = False
                buttons_arrived = False
                button_y = -150
                left_half_x = 0
                right_half_x = 0
                dragged_banana_x = 0
                dragged_banana_y = 0
                large_banana_rect = pygame.Rect(0, 0, 0, 0)

                continue
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
                    scoopsound.play()
                elif strawberry_rect.collidepoint(mouse_x, mouse_y):
                    print("strawberry selected")
                    selected_scoops.append("strawberry")
                    scoop_count += 1
                    scoopsound.play()
                elif vanilla_rect.collidepoint(mouse_x, mouse_y):
                    print("vanilla selected")
                    selected_scoops.append("vanilla")
                    scoop_count += 1
                    scoopsound.play()
                if scoop_count == 3:
                    banana_split_complete = True
            if banana_split_complete and serve_button_rect.collidepoint(mouse_x, mouse_y):
                complete_orders += 1
                total_orders += 1
                with open("stats.txt", "w") as file:
                    file.write(f"{games_played}\n")
                    file.write(f"{games_won}\n")
                    file.write(f"{games_lost}\n")
                    file.write(f"{total_orders}\n")
                    file.write(f"{highest_orders}\n")
                serve_sound.play()
                if total_orders >= 1:
                    game_state = "secret_ending"
                    secret_timer = pygame.time.get_ticks()
                    rocket_y = 170
                    smoke_particles = []
                    city_rocket_y = -30
                    slime_radius = 0
                    slime_exploding = False
                    slime_shrinking = False
                    slime_hold_timer = 0
                    slime_reveal_timer = 0
                    second_rocket_y = -30
                    second_rocket_hit = False
                    final_explosion_radius = 0
                    final_explosion_timer = 0
                    city_destroyed = False
                    destroyed_timer = 0
                    ending_fade = 0
                    continue
                #reset banana
                batch_on_board = False
                banana_peeled = False
                banana_cut = False
                #reset icecream
                scoop_count = 0
                selected_scoops = []
                banana_split_complete = False
                #reset tray
                tray_visible = False
                tray_y = -tray.get_height()
                #reset flavor buttons
                buttons_visible = False
                buttons_arrived = False
                button_y = -150
                #rset banana animation
                left_half_x = 0
                right_half_x = 0
            #large banana collision
            if batch_on_board and large_banana_rect.collidepoint(mouse_x, mouse_y):
                if not banana_peeled:
                    banana_peeled = True
                    peelsound.play()
                elif not banana_cut:
                    banana_cut = True
                    left_half_x = 0
                    right_half_x = 0
                    tray_visible = True
                    cutsound.play()
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
    if not game_over and game_state == "playing":
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

    if game_state == "menu":
        game_surface.blit(main_menu, (0,0))
        game_surface.blit(play_button, (0,0))
        game_surface.blit(guide_button, (0,0))
        game_surface.blit(stats_button, (0,0))
    elif game_state == "guide":
        game_surface.blit(guide_screen, (0, 0))
        instructions = [
            "HOW TO PLAY",
            "",
            "WASD - Move the farmer",
            "E - Collect and deliver bananas",
            "Drag a banana onto the cutting board",
            "Click banana to peel it",
            "Click again to cut it",
            "Choose 3 ice cream scoops",
            "Click SERVE to complete the order"
        ]
        for i, line, in enumerate(instructions):
            text = guide_font.render(line, True, (255, 255, 255))
            text_rect = text.get_rect(center = (game_width // 2, 35 + i * 22))
            game_surface.blit(text, text_rect)
    elif game_state == "stats":
        game_surface.blit(stats_screen, (0,0))
        win_rate = 0
        if games_played > 0:
            win_rate = (games_won / games_played) * 100
        stats_text = [
            f"Games Played: {games_played}",
            f"Games Won: {games_won}",
            f"Games Lost: {games_lost}",
            f"Orders Completed: {total_orders}",
            f"Highest Orders: {highest_orders}",
            f"Win Rate: {win_rate:.1f} %"
        ]
        for i, line in enumerate(stats_text):
            text = guide_font.render(line, True, (255, 255, 255))
            text_rect = text.get_rect(center = (game_width // 2,75 + i * 25))
            game_surface.blit(text, text_rect)        
    elif game_state == "secret_ending":
        elapsed = pygame.time.get_ticks() - secret_timer
        if elapsed >= 42000:
            #city background
            if city_destroyed:
                game_surface.blit(secret_city_destroyed, (0,0))
            elif slime_exploding:
                game_surface.blit(secret_city_slime, (0,0))
            else:
                game_surface.blit(secret_city, (0,0))
            #rocket falls
            if not slime_exploding:
                if city_rocket_y < 235 - city_rocket.get_height():
                    city_rocket_y += city_rocket_speed
                else:
                    slime_exploding = True
                game_surface.blit(city_rocket, (game_width // 2 - city_rocket.get_width() //2, int(city_rocket_y)))
            #slime explosion
            if slime_exploding:
                #expand
                if not slime_shrinking and slime_hold_timer == 0:
                    slime_radius += 5
                    if slime_radius >= 350:
                        slime_radius = 350
                        slime_hold_timer = pygame.time.get_ticks()
                #pause for 1 second
                if slime_hold_timer != 0:
                    if pygame.time.get_ticks() - slime_hold_timer >= 1000:
                        slime_shrinking = True
                #shrink
                if slime_shrinking:
                    slime_radius = max(0, slime_radius - 8)
                    if slime_radius == 0 and slime_reveal_timer == 0:
                        slime_reveal_timer = pygame.time.get_ticks()

                #draw slime circle
                if slime_radius > 0:
                    pygame.draw.circle(game_surface, (80, 220, 60), (game_width // 2, 235), int(slime_radius))
            if slime_reveal_timer != 0:
                if pygame.time.get_ticks() - slime_reveal_timer >= 3000:
                    if not second_rocket_hit:
                        second_rocket_y += second_rocket_speed
                        if second_rocket_y >= 235 - second_object.get_height():
                            second_rocket_y = 235 - second_object.get_height()
                            second_rocket_hit = True
                            final_explosion_timer = pygame.time.get_ticks()
                    if not city_destroyed:
                        game_surface.blit(second_object, (game_width // 2 - second_object.get_width() // 2, int(second_rocket_y)))
            if second_rocket_hit and not city_destroyed:
                final_explosion_radius = min(350, final_explosion_radius + 8)
                pygame.draw.circle(game_surface, (255, 220, 80), (game_width // 2, 235), int(final_explosion_radius))
                if pygame.time.get_ticks() - final_explosion_timer >= 1800:
                    destroyed_timer = pygame.time.get_ticks()
                    city_destroyed = True
            if city_destroyed:
                time_since_destroyed = pygame.time.get_ticks() - destroyed_timer
                if time_since_destroyed >= 3000:
                    ending_fade = min(255, ending_fade + 3)
                    fade_surface = pygame.Surface((game_width, game_height))
                    fade_surface.fill((0, 0, 0))
                    fade_surface.set_alpha(ending_fade)
                    game_surface.blit(fade_surface, (0,0))
                    if ending_fade >= 255:
                        ending_lines = [
                            "BANANA POWER SYSTEM - FINAL REPORT",
                            "CRITICAL POTASSIUM OVERLOAD",
                            "Banana energy output exceeded 9000%.",
                            "The city has been successfully",
                            "converted into a smoothie.. nevermind.",
                            "Scientists recommend using fewer",
                            "bananas next time.",
                            "END OF REPORT"
                        ]
                        for i, line in enumerate(ending_lines):
                            if i == 1:
                                color = (255, 220, 60)
                            else:
                                color = (255, 255, 255)
                            text = secret_font.render(line, True, color)
                            text_rect = text.get_rect(center= (game_width // 2, 55 + i * 22))
                            game_surface.blit(text, text_rect)
        else:
            if elapsed < 15000:
                game_surface.blit(secret_background, (0,0))
            else:
                if elapsed < 33000:
                    sky_offset = ((elapsed - 15000) // 20) % game_height
                else:
                    sky_offset = (900 - (elapsed - 33000) // 10) % game_height
                game_surface.blit(secret_sky, (0, sky_offset))
                game_surface.blit(secret_sky, (0, sky_offset - game_height))

                #darken the sky between 20 and 25
                if elapsed >= 20000:
                    if elapsed < 33000:
                        #sky darkens
                        darkness = min(255, int((elapsed - 20000) / 5000 * 255))
                    else:
                        #sky is blue again whe it falls back down
                        darkness = max(0, 255 - int((elapsed - 33000) / 5000 * 255))
                    dark_overlay = pygame.Surface((game_width, game_height), pygame.SRCALPHA)
                    dark_overlay.fill((0, 0, 25, darkness))
                    game_surface.blit(dark_overlay, (0,0))
                    #stars appear after 25 seconds
                    if 25000 <= elapsed < 30000:
                        for star in stars:
                            if elapsed < 33000:
                                #stars move down while rocket geos up
                                star[1] += 1
                                if star[1] >= game_height:
                                    star[1] = 0
                            else:
                                star[1] -=2
                                if star[1] <0:
                                    star[1] = game_height - 1
                            pygame.draw.circle(
                                game_surface, (255, 255, 255),
                                (star[0], star[1]),
                                1
                            )

            if elapsed < 3000:
                if(elapsed // 500) % 2 == 0:
                    pygame.draw.rect(game_surface, (255, 0, 0), (225, 202, 8, 8))
            if 3000 <= elapsed < 15000:
                pygame.draw.circle(game_surface, (255, 255, 0), (225, 200), 3)
            if 4000 <= elapsed < 15000:
                pygame.draw.circle(game_surface, (255, 255, 0), (235, 200), 3)
            if 5000 <= elapsed < 15000:
                pygame.draw.circle(game_surface, (255, 255, 0), (245, 200), 3)
            if 3000 <= elapsed < 6000:
                power_text = secret_font.render("POWERING UP...", True, (0, 255, 0))
                game_surface.blit(power_text, (207, 185))
            if 6000 <= elapsed < 15000:
                ready_text = secret_font.render("READY", True, (0, 255, 0))
                game_surface.blit(ready_text, (222, 185))
            if elapsed >= 8000:
                if elapsed < 15000:
                    # nuke launches from machine
                    if rocket_y > -secret_rocket.get_height():
                        rocket_y -= rocket_speed
                elif elapsed < 20000:
                    #rockey flies upward through the sky
                    rocket_y = game_height - (elapsed - 15000) // 20
                elif elapsed < 33000:
                    #rocket stays in center while rotate
                    rocket_y = game_height // 2 - secret_rocket.get_height() // 2
                else:
                    #rocket falling
                    rocket_y = game_height // 2 - secret_rocket.get_height() // 2
                    rocket_y += (elapsed - 33000) // 40
                # create smoke whiel rockets moving
                if rocket_y > -secret_rocket.get_height():
                    if random.randint(1,3) == 1:
                        angle = max(0, min(180, (elapsed - 30000) / 3000 * 180))
                        radians = math.radians(angle)
                        center_x = rocket_x + secret_rocket.get_width() / 2
                        center_y = rocket_y + secret_rocket.get_height() / 2
                        smoke_x = center_x + math.sin(radians) * secret_rocket.get_height() / 2
                        smoke_y = center_y + math.cos(radians) * secret_rocket.get_height() / 2
                        smoke_speed = random.uniform(0.2, 0.6)
                        smoke_vx = math.sin(radians) * smoke_speed
                        smoke_vy = math.cos(radians) * smoke_speed
                        smoke_particles.append([
                            smoke_x + random.randint(-5, 5),
                            smoke_y,
                            smoke_vx + random.uniform(-0.2, 0.2),
                            smoke_vy,
                            random.randint(2, 4),
                            60
                        ])
                for particle in smoke_particles[:]:
                    particle[0] += particle[2]
                    particle[1] += particle[3]
                    particle[4] += 0.04
                    particle[5] -= 1

                    brightness = max(40, int(160 * particle[5] / 60))
                    pygame.draw.circle(
                        game_surface,
                        (brightness, brightness, brightness),
                        (int(particle[0]), int(particle[1])),
                        int(particle[4])
                    )
                    if particle[5] <= 0:
                        smoke_particles.remove(particle)

                if rocket_y > -secret_rocket.get_height():
                    if elapsed >= 30000:
                        angle = min(180, (elapsed - 30000) / 3000 * 180)
                        rotated_rocket = pygame.transform.rotate(secret_rocket, angle)
                        rocket_rect = rotated_rocket.get_rect(center = (rocket_x + secret_rocket.get_width() // 2, rocket_y + secret_rocket.get_height() // 2))
                        game_surface.blit(rotated_rocket, rocket_rect)
                    else:
                        game_surface.blit(secret_rocket, (rocket_x, rocket_y))
    else:
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
        #completed orders
        score_text = font.render(f"Orders: {complete_orders}/{target_orders}", True, (255, 255, 255))
        game_surface.blit(score_text, (10, 20))
        #timer
        timer_text = font.render(f"Time: {time_left}", True, (255, 255, 255))
        game_surface.blit(timer_text, (10, 30))
        if game_over:
            if level == 1:
                if game_won:
                    game_surface.blit(win_screen, win_screen_rect)
                else:
                    game_surface.blit(lose_screen, lose_screen_rect)
            elif level == 2:
                if game_won:
                    game_surface.blit(final_win_screen, final_lose_screen_rect)
                else:
                    game_surface.blit(final_lose_screen, final_lose_screen_rect)


        if banana_split_complete:
            complete_text = font.render(f"Banana Split Complete!", True, (255, 255, 255))
            game_surface.blit(complete_text, (200, 20))
            game_surface.blit(serve_button, serve_button_rect)

    #screen shake
    shake_x = 0
    shake_y = 0

    if game_state == "secret_ending":
        elapsed = pygame.time.get_ticks() - secret_timer
        if 8000 <= elapsed < 15000:
            shake_x = random.randint(-3, 3)
            shake_y = random.randint(-3, 3)
        if second_rocket_hit and pygame.time.get_ticks() - final_explosion_timer < 800:
            shake_x = random.randint(-5, 5)
            shake_y = random.randint(-5, 5)

    #scale game to window
    scaled_surface = pygame.transform.scale(game_surface, (window_width, window_height))

    #scale shake to window res
    shake_x = shake_x * window_width // game_width
    shake_y = shake_y * window_height // game_height

    #display game
    screen.fill((0,0,0))
    screen.blit(scaled_surface, (shake_x, shake_y))
    pygame.display.flip()

    #limit fps
    clock.tick(fps)

pygame.quit()

