import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    gameClock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    myPlayer = Player( x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        myPlayer.draw(screen)
        pygame.display.flip()

        dt = gameClock.tick(60) / 1000

    



if __name__ == "__main__":
    main()
