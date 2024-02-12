import pygame
import math
import colored_shape
pygame.init()

WIDTH, HEIGHT = 1000, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WINDOW.fill((0, 0, 0))
FPS = 60

def change_all(c_list):
    for c in c_list:
        pygame.draw.circle(WINDOW, c.color, c.location(), c.radius)
        c.angle += math.pi / 180 * 1
        c.color_change()


def main():
    counter = 0
    run = True
    c_list = []
    resolution = 100
    radius = 2
    for i in range(resolution):
        c = colored_shape.circle(radius, (WIDTH / 2, HEIGHT / 2), base=255/resolution*i, distance=resolution-(i+1))
        c.color_change()  # so that its set to proper base and peak
        c_list.append(c)
        c = colored_shape.circle(radius, (WIDTH / 2, HEIGHT / 2), peak=255 / resolution * i -1, distance=resolution*2 - i)
        c.color_change()  # so that its set to proper base and peak
        c_list.append(c)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if counter%60 == 0:
            change_all(c_list)

        pygame.display.flip() # Needed to update the screen
        counter += 1
    pygame.quit()

if __name__ == "__main__":
    main()