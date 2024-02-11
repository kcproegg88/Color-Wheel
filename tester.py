import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Example")

# Define player variables
player_size = 50
player_x = (WIDTH - player_size) // 2
player_y = (HEIGHT - player_size) // 2

# Set up clock
clock = pygame.time.Clock()

# Main game loop
running = True
screen.fill((0, 0, 0))  # Fill screen with black
mode = 1
r = 255
g = 0
b = 0


def change_rgb(r, g, b):
    pass

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5

    # Draw graphics

    if mode == 0:
        r += 1
        b -= 1
        if r >= 255:
            mode = 1
    elif mode == 1:
        g += 1
        r -= 1
        if g >= 255:
            mode = -1
    elif mode == -1:
        b += 1
        g -= 1
        if b >= 255:
            mode = 0
    pygame.draw.rect(screen, (r, g, b), (player_x, player_y, player_size, player_size))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
# Quit Pygame
pygame.quit()
sys.exit()
