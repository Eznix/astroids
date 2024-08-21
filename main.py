import sys
import pygame
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from score import Score


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    score = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots,updatable,drawable)
    Score.containers = (score,drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()
    score = Score()

    dt = 0

    font = pygame.font.Font(None, 36)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                player.player_died()
                player.kill()
                if player.get_lives() > 0:
                    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, player.player_lives)
                else:    
                    print("Game over!")
                    print("Score:", score.get_score())
                    sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    score.add_score(asteroid)
                    asteroid.split()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        # Draw the score to the screen
        score_text = font.render(f'Score: {score.get_score()}  Lives: {player.player_lives}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))


        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
