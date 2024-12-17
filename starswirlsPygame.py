#MAKE SURE TO USE WASD TO MOVE
#VERY EARLY PROJECT TO SEE SOME CHANGES MOVING WHEN TRIGGERED BY MOVEMENT
#IT WILL OPEN IN FULL SCREEN
#trabajo en proceso

import pygame
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.SCALED | pygame.FULLSCREEN) #DELETE !.SCALED | pygame.FULLSCREEN! IF DONT WANT FULL SCREEN
clock = pygame.time.Clock()
pygame.display.set_caption("Swirling Star with VSync")
running = True

# Center and star properties
center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
radius = 100  # Initial swirl radius
angle = 0  # Initial swirl angle in radians
swirl_speed = 2  # Speed of swirling motion
radius_change = 50  # Speed of radius change
num_points = 5  # Star points
star_size = 50  # Star size (radius)

def draw_star(surface, position, size, points, color, angle=0):
    """Draws a star with a given position, size, number of points, and rotation."""
    x, y = position
    vertices = []
    for i in range(points * 2):  # Twice the points (inner and outer)
        r = size if i % 2 == 0 else size / 2  # Alternate radius (outer/inner points)
        theta = angle + i * math.pi / points  # Angle of each point
        px = x + r * math.cos(theta)
        py = y + r * math.sin(theta)
        vertices.append((px, py))
    pygame.draw.polygon(surface, color, vertices)

while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen
    screen.fill("black")

    # Handle keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:  # Move outward
        radius += radius_change * 1 / 60  # 1/60 assumes a ~60Hz screen
    if keys[pygame.K_s]:  # Move inward
        radius -= radius_change * 1 / 60
    if keys[pygame.K_a]:  # Rotate counterclockwise
        angle -= swirl_speed * 1 / 60
    if keys[pygame.K_d]:  # Rotate clockwise
        angle += swirl_speed * 1 / 60

    # Prevent radius from becoming negative
    radius = max(10, radius)

    # Convert polar to Cartesian coordinates for swirling motion
    star_pos = pygame.Vector2(
        center.x + radius * math.cos(angle),
        center.y + radius * math.sin(angle)
    )

    # Dynamically change the star's size or points
    star_size = 50 + 20 * math.sin(pygame.time.get_ticks() / 500)  # Pulsating effect
    num_points = 5 + int(2 * math.sin(pygame.time.get_ticks() / 1000))  # Change points dynamically

    # Draw the swirling star
    draw_star(screen, star_pos, star_size, num_points, "yellow", angle)

    # Update the display (with VSync)
    pygame.display.flip()

    # No frame limiting; let VSync control FPS
    # clock.tick() is removed

pygame.quit()
