import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from power_ups import *

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
    wrappable = pygame.sprite.Group()
    power_up_group = pygame.sprite.Group()

    AsteroidField.containers = (updateable)
    Asteroid.containers = (updateable, drawable, asteroids)
    Player.containers = (updateable, drawable, wrappable)
    Shot.containers = (updateable, drawable, shots, wrappable)
    Speed.containers = (drawable, power_up_group)
    Machine_gun.containers = (drawable, power_up_group)

    asteroid_field_main = AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, PLAYER_RADIUS)

    player_score = 0
    player_lives = 3
    timer2 = 2
    
    font = pygame.font.Font(None, 36)
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        health_text = font.render(f'Health: {player_lives}', True, (255, 255, 255))
        score_text = font.render(f"Score: {player_score}", True, (255, 255, 255))
        screen.fill("black")

        screen.blit(health_text, (10, 10))
        screen.blit(score_text, (10, 50))
        
    
        dt = clock.tick(60) / 1000
        
        timer2 -= dt
        
        for i in updateable:
            i.update(dt)

        for i in drawable:
            i.draw(screen)
        
        for i in wrappable:
            i.wrap_around()
        
        for i in asteroids:
            if (player.collision(i) == True) and timer2 <= 0:
                timer2 += ((timer2*-1)+PLAYER_DAMAGE_COOLDOWN)
                player_lives -= 1
                if player_lives == 0:
                    print(f"Player score: {player_score}")
                    print("Game over!")
                    exit()
                
            for j in shots:
                if j.collision(i) == True:
                    player_score += 1
                    j.kill()
                    i.split()
        
        for i in power_up_group:
            if player.collision(i) == True:
                i.collect(player)
            i.counter(dt, player)

        
        pygame.display.flip()


if __name__ == "__main__":
    main()
        
