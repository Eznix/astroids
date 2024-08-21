import pygame
from constants import *
from asteroid import Asteroid

class Score():
    def __init__(self):
        self.score = 0

    def add_score(self,asteroid):
        if asteroid.radius == ASTEROID_MAX_RADIUS:
            self.score += 50
        elif asteroid.radius == ASTEROID_MIN_RADIUS:
            self.score += 150
        else:
            self.score += 100

    def get_score(self):
        return self.score