import os.path

import pygame

# Function Load Image


def load_image(image_name):
    """Carrega uma imagem na memoria"""
    fullname = os.path.join("images", image_name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print("Cannot load image: ", fullname)
        raise SystemExit
    return image, image.get_rect()