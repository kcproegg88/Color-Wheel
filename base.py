import pygame
import math
pygame.init()

WIDTH, HEIGHT = 1000, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WINDOW.fill((0, 0, 0))
FPS = 60


def main():
    counter = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.flip() # Needed to update the screen
        counter += 1
    pygame.quit()

if __name__ == "__main__":
    main()