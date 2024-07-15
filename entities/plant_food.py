import pygame
import random
from settings import *

class Plant_food:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.size = FOOD_SIZE
        self.color = (255, 0, 0)  # Red

    def update(self):
        # Food might not need to update, but could implement regrowth or decay
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)