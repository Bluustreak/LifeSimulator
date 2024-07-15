import pygame
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Life Simulator")
        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, creatures, foods):
        for creature in creatures:
            creature.update()
        for food in foods:
            food.update()


    def draw(self, creatures, foods):
        self.screen.fill(BG_COLOR)
        for creature in creatures:
            creature.draw(self.screen)
        for food in foods:
            food.draw(self.screen)
        pygame.display.flip()

    def run(self, creatures, foods):
        while self.running:
            self.handle_events()
            self.update(creatures, foods)
            self.draw(creatures, foods)
            self.clock.tick(FPS)
        pygame.quit()
