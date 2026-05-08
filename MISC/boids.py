import pygame
import random
import math

# Constants
WIDTH, HEIGHT = 800, 600
BOID_COUNT = 10
MAX_SPEED = 4
SEPARATION_RADIUS = 50
ALIGNMENT_RADIUS = 50
COHESION_RADIUS = 50

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Helper functions
def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Boid Class
class Boid:
    def __init__(self):
        self.position = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]
        angle = random.uniform(0, 2 * math.pi)
        self.velocity = [math.cos(angle) * MAX_SPEED, math.sin(angle) * MAX_SPEED]
        self.acceleration = [0, 0]

    def limit_speed(self):
        speed = math.sqrt(self.velocity[0] ** 2 + self.velocity[1] ** 2)
        if speed > MAX_SPEED:
            self.velocity[0] = (self.velocity[0] / speed) * MAX_SPEED
            self.velocity[1] = (self.velocity[1] / speed) * MAX_SPEED

    def separation(self, boids):
        steer = [0, 0]
        total = 0
        for other in boids:
            if other == self:
                continue
            d = distance(self.position, other.position)
            if d < SEPARATION_RADIUS:
                steer[0] += self.position[0] - other.position[0]
                steer[1] += self.position[1] - other.position[1]
                total += 1
        if total > 0:
            steer[0] /= total
            steer[1] /= total
            self.velocity[0] += steer[0]
            self.velocity[1] += steer[1]

    def update(self):
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.limit_speed()
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

        # Wrap around edges
        self.position[0] %= WIDTH
        self.position[1] %= HEIGHT

    def draw(self):
        pygame.draw.circle(screen, (0, 0, 255), (int(self.position[0]), int(self.position[1])), 5)

# Create boids
boids = [Boid() for _ in range(BOID_COUNT)]

# Game loop
running = True
while running:
    screen.fill((240, 240, 240))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for boid in boids:
        boid.separation(boids)
        boid.update()
        boid.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

