from game_engine import Game
from settings import INITIAL_CREATURES, INITIAL_FOOD, SCREEN_HEIGHT, SCREEN_WIDTH
from entities.creature import Creature
from entities.plant_food import Plant_food
import random

def main():
    game = Game()
    
    creatures = [Creature(random.randint(0, SCREEN_HEIGHT), random.randint(0, SCREEN_WIDTH)) for _ in range(INITIAL_CREATURES)]
    foods = [Plant_food() for _ in range(INITIAL_FOOD)]

    game.run(creatures, foods)

if __name__ == "__main__":
    main()