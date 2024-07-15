import pygame
import random
from settings import *

class Creature:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.size = CREATURE_SIZE
        self.color = (0, 255, 0)  # Green
        

    def update(self):
        # Implement creature behavior, e.g., move randomly
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

        # Ensure the creature stays within the screen bounds
        self.x = max(0, min(SCREEN_WIDTH, self.x))
        self.y = max(0, min(SCREEN_HEIGHT, self.y))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
    
