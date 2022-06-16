# Inicial game for study propurse
# by: Marcos Antonio and Giordano Bruno
# twitter @marcosadsjunior @giordanobruno

# The propuse is create a game that Caixa Economica employess can play and study about
# differents subjects that is intrested for the company

# imports needed
import sys

import pygame
import time
import random
import mainCharacter

# iniciating pygame
check_erros = pygame.init()
if check_erros[1] > 0:
    print("Ops! Something went wrong while iniciating the game")
    sys.exit(-1)
else:
    print("Pygame iniciated successfully")

# defining window game size

window_game_width = 640
window_game_height = 480
window_game_size = (window_game_width, window_game_height)
main_window = pygame.display.set_mode(window_game_size)

# setting clock to limite in 30 fps

clock = pygame.time.Clock()
pygame.display.set_caption("Jogo Agencia!!")
background_sprite = pygame.image.load("sprites/background/livingRoom.png").convert()
# main_window.blit(background_sprite, (0, 0))


# main character variables


main_character_position_y = 40
main_character_position_x = 260
velocity_movement = 5
main_character_right = False
main_character_left = False
main_character_down = False
main_character_up = False
walk_count = 0
first_position_count = 0

main_char_sprites_walk_up = [
    pygame.image.load('sprites/mainCharacter/Char_back_1.png').convert_alpha(),
    pygame.image.load('sprites/mainCharacter/Char_back_2.png').convert_alpha(),
    pygame.image.load('sprites/mainCharacter/Char_back_3.png').convert_alpha(),
    pygame.image.load('sprites/mainCharacter/Char_back_4.png').convert_alpha(),
    pygame.image.load('sprites/mainCharacter/Char_back_5.png').convert_alpha(),
    pygame.image.load('sprites/mainCharacter/Char_back_6.png').convert_alpha()
]

main_char_sprites_walk_down = [
    pygame.image.load('sprites/mainCharacter/Char_frente_1.png').convert_alpha(),
    pygame.image.load('sprites/mainCharacter/Char_frente_2.png').convert_alpha(),
    pygame.image.load('sprites/mainCharacter/Char_frente_3.png').convert_alpha(),
    pygame.image.load('sprites/mainCharacter/Char_frente_4.png').convert_alpha(),
    pygame.image.load('sprites/mainCharacter/Char_frente_5.png').convert_alpha(),
    pygame.image.load('sprites/mainCharacter/Char_frente_6.png').convert_alpha()
]

main_char_sprites_walk_left = [
    pygame.image.load('sprites/mainCharacter/Char_esquerda_1.png').convert_alpha(),
    pygame.image.load('sprites/mainCharacter/Char_esquerda_2.png').convert_alpha(),
    pygame.image.load('sprites/mainCharacter/Char_esquerda_3.png').convert_alpha(),
    pygame.image.load('sprites/mainCharacter/Char_esquerda_4.png').convert_alpha(),
    pygame.image.load('sprites/mainCharacter/Char_esquerda_5.png').convert_alpha(),
    pygame.image.load('sprites/mainCharacter/Char_esquerda_6.png').convert_alpha()
]

main_char_sprites_walk_right = [
    pygame.image.load('sprites/mainCharacter/Char_direita_1.png').convert_alpha(),
    pygame.image.load('sprites/mainCharacter/Char_direita_2.png').convert_alpha(),
    pygame.image.load('sprites/mainCharacter/Char_direita_3.png').convert_alpha(),
    pygame.image.load('sprites/mainCharacter/Char_direita_4.png').convert_alpha(),
    pygame.image.load('sprites/mainCharacter/Char_direita_5.png').convert_alpha(),
    pygame.image.load('sprites/mainCharacter/Char_direita_6.png').convert_alpha()
]


def move_char(character, position_x, position_y):
    global walk_count
    main_window.blit(character, (position_x, position_y))
    walk_count += 1


def main_char_first_position():
#    global first_position_count
#    if first_position_count == 0:
    main_window.blit(main_char_sprites_walk_down[walk_count], (main_character_position_x, main_character_position_y))
#        first_position_count += 1
#    else:
#        return


def redraw_game_window():
    # mainChart = mainCharacter.main_character()
    global walk_count
    global main_character_down
    global main_character_up
    global main_character_right
    global main_character_left
    main_char_first_pos = 0

    background_color = pygame.Color(0, 0, 255, 255)
    main_window.blit(background_sprite, (0, 0))

    if walk_count >= 6:
        walk_count = 0

#    main_window.blit(main_char_sprites_walk_down[walk_count], (main_character_position_x, main_character_position_y))

    if main_character_down:
        move_char(main_char_sprites_walk_down[walk_count], main_character_position_x, main_character_position_y)
        # main_character_down = False
        main_char_first_pos += 1

    elif main_character_up:
        move_char(main_char_sprites_walk_up[walk_count], main_character_position_x, main_character_position_y)
        # main_character_up = False
        main_char_first_pos += 1

    elif main_character_left:
        move_char(main_char_sprites_walk_left[walk_count], main_character_position_x, main_character_position_y)
        # main_character_left = False
        main_char_first_pos += 1

    elif main_character_right:
        move_char(main_char_sprites_walk_right[walk_count], main_character_position_x, main_character_position_y)
        # main_character_right = False
        main_char_first_pos += 1

    else:
        print("waiting movement")

#    pygame.draw.circle(main_window, (0, 255, 0), (main_character_position_x, main_character_position_y), 50)
    if main_char_first_pos == 0:
        main_char_first_position()
    pygame.display.update()


while True:
    clock.tick(12)
    for event in pygame.event.get():
        # event process
        if event.type == pygame.QUIT:
            # quit game when click in 'x'
            quit()

    movement_arrows = pygame.key.get_pressed()
    main_character_up = (movement_arrows == [pygame.K_UP])
    main_character_right = (movement_arrows == [pygame.K_RIGHT])
    main_character_left = (movement_arrows == [pygame.K_LEFT])
    main_character_down = (movement_arrows == [pygame.K_DOWN])

    if movement_arrows[pygame.K_DOWN]:
        main_character_position_y += velocity_movement
        main_character_down = True

    if movement_arrows[pygame.K_UP]:
        main_character_position_y -= velocity_movement
        main_character_up = True

    if movement_arrows[pygame.K_RIGHT]:
        main_character_position_x += velocity_movement
        main_character_right = True

    if movement_arrows[pygame.K_LEFT]:
        main_character_position_x -= velocity_movement
        main_character_left = True

    redraw_game_window()


