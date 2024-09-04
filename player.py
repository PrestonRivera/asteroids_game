import pygame
from circleshape import CircleShape
from constants import *
from shot import *
from asteroid import *


class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.radius = PLAYER_RADIUS
        self.rotation = 0
        self.shot_timer = 0
        self.invulnerable = False
        self.invul_timer = PLAYER_LIFE_TIMER
        self.blink_timer = 0
        self.visible = True
        
    

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    def draw(self, screen):
        if self.visible or not self.invulnerable:
            pygame.draw.polygon(screen, "white", self.triangle(), 2)
    

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt 


    def update(self, dt):
        self.shot_timer -= dt
        self.check_invul_status(dt)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

        if self.invulnerable:
            self.blink_timer += dt
            if self.blink_timer >= 0.1:
                self.visible = not self.visible
                self.blink_timer = 0


    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt


    def shoot(self):
        if self.shot_timer > 0:
            return
        self.shot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED


    def check_invul_status(self, dt):
        if self.invulnerable:
            self.invul_timer -= dt
            if self.invul_timer < 0:
                self.invulnerable = False
                self.reset_invul_timer()

    def reset_invul_timer(self):
        self.invul_timer = PLAYER_LIFE_TIMER
        
