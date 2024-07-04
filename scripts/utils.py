import os

import pygame

# loading images/files

BASE_IMG_PATH = 'data/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert() # converts internal representation for rendering in pygame
    img.set_colorkey((0, 0, 0)) # black color is transparent apparently removes the black color
    return img

def load_images(path):
    images = []
    for img_name in os.listdir(BASE_IMG_PATH + path):
        images.append(load_image(path + '/' + img_name))
    return images # loading images ontto a list