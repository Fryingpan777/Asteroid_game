import pygame
from constants import *
from circleshape import CircleShape

    

class Speed(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, POWER_UP_RADIUS)
        self.timer = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, "green", self.position, self.radius, 2)
    
    def counter(self, dt, player):
        if self.timer > 0:
            self.timer -= dt
            if self.timer <= 0:
                player.speed_buff = 1
    
    def collect(self, player):
        self.timer += 7
        self.position.y += 2000
        player.speed_buff *= 2



class Machine_gun(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, POWER_UP_RADIUS)
        self.timer = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)
    
    def counter(self, dt, player):
        if self.timer > 0:
            self.timer -= dt
            if self.timer <= 0:
                player.shoot_buff = 1
    
    def collect(self, player):
        self.timer += 7
        self.position.y += 2000
        player.shoot_buff = 0.33


class Super_bullet(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, POWER_UP_RADIUS)
        self.timer = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 2)
    
    def counter(self, dt, player):
        if self.timer > 0:
            self.timer -= dt
            if self.timer <= 0:
                player.shoot_buff = 1
                player.bullet_buff = 1
    
    def collect(self, player):
        self.timer += 7
        self.position.y += 2000
        player.shoot_buff = 2
        player.bullet_buff = 3