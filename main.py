import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidsfield import *
from circleshape import CircleShape
from shot import Shot


def main():
    print("Starting asteroids!")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updateable, drawable)

    AsteroidField.containers = updateable
    Asteroid.containers = (asteroids, updateable, drawable)
    asteroidfield = AsteroidField()

    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    player_lives = PLAYER_LIFE

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for object in updateable:
            object.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if shot.is_colliding(asteroid):
                    shot.kill()
                    asteroid.split()

        for asteroid in asteroids:
            if asteroid.is_colliding(player) and not player.invulnerable:
                player_lives -= 1
                player.invulnerable = True
                player.reset_invul_timer
                print(f"player hit! Lives remaining {player_lives}")


        if player_lives == 0:
            print("Game Over!!")
            sys.exit()

        screen.fill("black")

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()

