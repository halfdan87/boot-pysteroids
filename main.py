import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from shots import *


def main():
    (succs, fails) = pygame.init()

    print(f"{succs}, {fails}")

    window = pygame.display.set_mode(
            size=(SCREEN_WIDTH, SCREEN_HEIGHT)
    )

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 

    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    asteroidField = AsteroidField()

    updatable.add(asteroidField)

    updatable.add(player)
    drawable.add(player)

    Player.containers = (updatable, drawable)

    clock = pygame.time.Clock()
    dt = 0

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        window.fill(pygame.Color("black"))

        updatable.update(dt)

        for a in asteroids:
            if player.collides(a):
                print("Game over")
                return

        for d in drawable:
            d.draw(window)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


    pygame.quit()



if __name__ == "__main__":
    main()
