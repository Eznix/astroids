# Particle class
import math
import random
import pygame
from constants import *


class Particle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(0.5, 1.5)

    def update(self):
        self.angle += 0.02
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

        if self.x < 0:
            self.x = SCREEN_WIDTH
        elif self.x > SCREEN_WIDTH:
            self.x = 0

        if self.y < 0:
            self.y = SCREEN_HEIGHT
        elif self.y > SCREEN_HEIGHT:
            self.y = 0

    def draw(self, window):
        color = (255,255,255)
        pos = (int(self.x), int(self.y))
        radius = int(self.radius)
        pygame.draw.circle(window, color, pos, radius)

# Particle system class
class ParticleSystem:
    def __init__(self):
        self.particles = []

    def add_particle(self, x, y, radius):
        print(len(self.particles))
        if len(self.particles) < 500:
            self.particles.append(Particle(x, y, radius))
        

    def update(self):
        for particle in self.particles:
            particle.update()

    def draw(self, window):
        for particle in self.particles:
            particle.draw(window)