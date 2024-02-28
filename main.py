import pygame
import math
import colored_shape
import draw_colored_shape

pygame.init()

WIDTH, HEIGHT = 750, 750
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WINDOW.fill((0, 0, 0))
FPS = 60


def init():
    initColors()
    initCircle()
    initLine()
    initRing()


def initColors():
    global RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA, BLACK, WHITE
    RED, YELLOW, GREEN, CYAN, BLUE, MAGENTA, BLACK, WHITE = (255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (255, 0, 255), (0, 0, 0), (255, 255 ,255)


def initCircle():
    global circle_list
    circle_list = []


def initLine():
    global line_list
    line_list = [colored_shape.Line(10, 5, (WIDTH/2, HEIGHT/2), True, 1, 150, 150)]


def initRing():
    global ring_list
    circle_num, radius, origin, dark, angle_rate, distance, width, angle = 1, 5, (WIDTH/2, HEIGHT/2), True, 1, 150, 150, 0
    ring_list = [colored_shape.Ring(circle_num, radius, origin, not dark, angle_rate, distance, width, angle, period=math.pi*2)]
    ring_list.append(colored_shape.Ring(circle_num, radius, origin, dark, angle_rate, distance, -width, angle, period=math.pi*2))


def update():
    global circle_list, line_list, ring_list
    ring_list[0].circle_num += 1
    ring_list[1].circle_num += 0
    line_list[0].angle += math.pi/180 * 1


def main():
    running = True

    init()
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update()

        WINDOW.fill(BLACK)
        draw_colored_shape.draw(ring_list, [], [], WINDOW)
        pygame.draw.circle(WINDOW, WHITE, ring_list[0].origin, ring_list[0].radius)

        pygame.display.flip()  # Needed to update the screen
        clock.tick(FPS)
    pygame.quit()


if __name__ == "__main__":
    main()
