import pygame
from player import *

# Base class for game objects
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
        # must override
        pass

    def update(self, dt):
        # Must override
        pass

    def is_colliding(self, object):
        if (
            pygame.math.Vector2.distance_to(self.position, object.position)
            <= self.radius + object.radius
        ):
            return True