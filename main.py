from game_engine import Game
from settings import INITIAL_CREATURES, INITIAL_FOOD
from entities.creature import Creature
from entities.plant_food import Plant_food

def main():
    game = Game()
    
    creatures = [Creature() for _ in range(INITIAL_CREATURES)]
    foods = [Plant_food() for _ in range(INITIAL_FOOD)]

    game.run(creatures, foods)

if __name__ == "__main__":
    main()