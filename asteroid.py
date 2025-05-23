import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        clockwise_angle = self.velocity.rotate(random_angle)
        counter_clockwise_angle = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        second_new_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        first_new_asteroid.velocity = clockwise_angle * 1.2
        second_new_asteroid.velocity = counter_clockwise_angle * 1.2

