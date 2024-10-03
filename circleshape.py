import pygame
#from shot import Shot

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass
    
    def collision(self, CircleShape):
        if (self.position.distance_to(CircleShape.position) < self.radius + CircleShape.radius):
            return True
        else:
            return False
    
    def wrap_around(self):
        if self.position.y > 740:
            self.position.y -= 760
            return True
        if self.position.y < (-20):
            self.position.y += 760
            return True
        if self.position.x > 1300:
            self.position.x -= 1320
            return True
        if self.position.x < (-20):
            self.position.x += 1320
            return True
        
