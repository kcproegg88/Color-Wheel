import pygame
import math
import colored_shape
pygame.init()

WIDTH, HEIGHT = 1000, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WINDOW.fill((5, 5, 5))
FPS = 60


def init():
    initColors()
    initRing()


def initColors():
    global RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA, BLACK, WHITE
    RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA, BLACK, WHITE = (255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (255, 0, 255), (0, 0, 0), (255, 255 ,255)


def initRing():
    global da_list
    da_list = [colored_shape.Ring(5, 50, (WIDTH/2, HEIGHT/2), False, 1, )]

def main():
    counter = 0
    run = True

    init()
    c = colored_shape.Circle(50, (WIDTH/2, HEIGHT/2), 100, 60/180*math.pi, WHITE)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.draw.circle(WINDOW, c.color, c.location(), c.radius)

        pygame.display.flip() # Needed to update the screen
        counter += 1
    pygame.quit()

if __name__ == "__main__":
    main()

