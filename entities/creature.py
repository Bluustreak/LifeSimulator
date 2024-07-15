import pygame
import random
from settings import *
from  utils.helpers import sign

class Creature:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = CREATURE_SIZE
        self.color = (0, 255, 0)  # Green
        self.eaten_foods = 0
        

    def update(self, foods:list, hungry=True,):
        offset = 10
        if hungry:
            # if food is in range, and if hungry, approach it
            for food in foods:
                dx = food.x-self.x
                dy = food.y-self.y
                if abs(dx)<=offset and abs(dy)<=offset:
                    self.x+=sign(dx)
                    self.y+=sign(dy)
                    if abs(dx)<5 and abs(dy)<5:
                        foods.remove(food)
                        self.eaten_foods+=1
                        #print("eatened food")


        # Implement creature behavior, e.g., move randomly
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

        # Ensure the creature stays within the screen bounds
        self.x = max(0, min(SCREEN_WIDTH, self.x))
        self.y = max(0, min(SCREEN_HEIGHT, self.y))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)
    


