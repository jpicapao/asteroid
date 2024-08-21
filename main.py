import sys

import pygame

from asteroid import Asteroid
from bullet import Shot
from constants import *
from player import Player
from asteroidfield import *

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))





    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2




    updatable = pygame.sprite.Group()

    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(x, y)

    asteroids_contain = pygame.sprite.Group()

    bullets = pygame.sprite.Group()
    Shot.containers = (bullets, updatable, drawable)

    Asteroid.containers = (asteroids_contain, updatable, drawable)

    AsteroidField.containers = (updatable)

    asteroid = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updatables in updatable:
            updatables.update(dt)

        for asteroids in asteroids_contain:
            if asteroids.collides_with(player):
                print("Game over!")
                sys.exit()
            for shot in bullets:
                if asteroids.collides_with(shot):
                    shot.kill()
                    asteroids.split()



        screen.fill((0, 0, 0))

        for drawables in drawable:
            drawables.draw(screen)






        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000






if __name__ == "__main__":

    main()