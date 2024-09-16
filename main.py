import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updateable)
    Asteroid.containers = (updateable, drawable, asteroids)
    Player.containers = (updateable, drawable)
    Shot.containers = (updateable, drawable, shots)
    asteroid_field_main = AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        dt = clock.tick(60) / 1000

        for i in updateable:
            i.update(dt)

        for i in drawable:
            i.draw(screen)
        
        for i in asteroids:
            if player.collision(i) == True:
                print("Game over!")
                exit()
            for j in shots:
                if j.collision(i) == True:
                    i.split()

        
        pygame.display.flip()


if __name__ == "__main__":
    main()
        
