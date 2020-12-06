import pygame
import random
from os import path
from utils.constants import (
    BLUE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    BLACK,
    IMG_DIR
)
allowed_speed = list(range(3,7))
class Block(pygame.sprite.Sprite):
    def __init__(self,size):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(IMG_DIR, "unnamed.png")).convert()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.speedy = random.choice(allowed_speed)
        self.speedx = random.choice(allowed_speed)
        self.size = size

    def update(self):
        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy
        if self.rect.right > SCREEN_WIDTH:
            self.rect_right = SCREEN_WIDTH
            self.speedx = random.choice(allowed_speed) * -1
        if self.rect.left < 0:
            self.rect.left = 0
            self.speedx = random.choice(allowed_speed)
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.speedy = random.choice(allowed_speed) *-1
        if self.rect.top < 0:
            self.rect.top = 0
            self.speedy = random.choice(allowed_speed)*+1