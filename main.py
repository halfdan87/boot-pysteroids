import pygame
from constants import *

def main():
    (succs, fails) = pygame.init()

    print(f"{succs}, {fails}")

    window = pygame.display.set_mode(
            size=(SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        window.fill(pygame.Color("black"))
        pygame.display.flip()

    pygame.quit()



if __name__ == "__main__":
    main()
