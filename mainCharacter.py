import pygame

# setting main character position


def main_character():
    main_character_position_y = 40
    main_character_position_x = 260
    velocity_movement = 5
    main_character_right = False
    main_character_left = False
    main_character_down = False
    main_character_up = False
    walk_count = 0
    main_character_sprites_walk_down = [pygame.image.load('sprites/mainCharacter/mainCharacterMoveDown1.png'),
                                        pygame.image.load('sprites/mainCharacter/mainCharacterMoveDown2.png'),
                                        pygame.image.load('sprites/mainCharacter/mainCharacterMoveDown3.png'),
                                        pygame.image.load('sprites/mainCharacter/mainCharacterMoveDown4.png'),
                                        pygame.image.load('sprites/mainCharacter/mainCharacterMoveDown5.png'),
                                        pygame.image.load('sprites/mainCharacter/mainCharacterMoveDown6.png')
                                        ]


if __name__ == "__main__":
    main_character()