import pygame
import math
import colored_shape
pygame.init()

WIDTH, HEIGHT = 1000, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WINDOW.fill((5, 5, 5))
FPS = 10


def init():
    initColors()
    initRing()


def initColors():
    global RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA, BLACK, WHITE
    RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA, BLACK, WHITE = (255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (255, 0, 255), (0, 0, 0), (255, 255 ,255)


def initRing():
    global ring_list
    circle_num, radius, origin, dark, angle_rate, distance, width, angle = 50, 5, (WIDTH/2, HEIGHT/2), True, 10, 150, 150, 0
    ring_list = [colored_shape.Ring(circle_num, radius, origin, dark, angle_rate, distance, width, angle, period=math.pi*2)]


def drawRings(ring_list):
    for ring in ring_list:

        for c in ring.generate_loop():
            c.color_change(ring.angle)
            pygame.draw.circle(WINDOW, c.color, c.location(), c.radius)


def main():
    counter = 0
    run = True

    init()
    c = colored_shape.Circle(50, (WIDTH/2, HEIGHT/2), 100, 60/180*math.pi, WHITE)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if counter%1 == 0:
            ring_list[0].angle += math.pi/180 * 1
        WINDOW.fill((0,0,0))
        pygame.draw.circle(WINDOW, WHITE, ring_list[0].origin, ring_list[0].radius)
        drawRings(ring_list)

        pygame.display.flip()  # Needed to update the screen
        counter += 1
        print(counter)
    pygame.quit()

if __name__ == "__main__":
    main()

