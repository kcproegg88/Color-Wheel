import pygame
import math
pygame.init()

WIDTH, HEIGHT = 1000, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WINDOW.fill((0, 0, 0))
FPS = 60


class colored_shape:
    def __init__(self, origin=(WIDTH/2, HEIGHT/2), distance=100, angle=0, color=(255, 0, 0), min=0, max=256):
        self.origin = origin
        self.d = distance
        self.angle = angle
        self.color = color
        self.min = min
        self.max = max

    def location(self):
        x = int(math.cos(self.angle) * self.d + self.origin[0])
        y = int(math.sin(self.angle) * self.d + self.origin[1])
        return x, y

    def color_change(self, s=1):
        r, g, b = self.color

        if math.cos(self.angle)>= math.cos(math.pi/3):
            r = self.max
        elif math.cos(self.angle)<= -math.cos(math.pi/3):
            r = self.min
        else:
            r = math.cos(self.angle)


        pass
class circle(colored_shape):
    def __init__(self, radius=100):
        super().__init__()
        self.r = radius

def color_change(color, min, max, speed=1):
    r, g, b = color
    if self.angle
    if color == (255, 255, 0):
        r -= speed
    elif color == (0, 255, 0):
        b += speed
    elif color == (0, 255 ,255):
        g -= speed
    elif color == (0, 0, 255):
        r += speed
    elif color == (255, 0, 255):
        b -= speed
    elif r == max and b == min:
        g += speed
    elif g == max and b == min:
        r -= speed
    elif r == min and g == max:
        b += speed
    elif r == min and b == max:
        g -= speed
    elif g == min and b == max:
        r += speed
    elif r == max and g == min:
        b -= speed

    return (r, g, b)


def main():
    c = circle(radius=10)
    angle = 0
    color_speed = 1
    angle_speed = 2*math.pi/(255*6-3)*color_speed
    counter = 0
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if counter%1 == 0:
            c.color = color_change(c.color, c.min, c.max, color_speed)
            c.angle += angle_speed
        try:
            pygame.draw.circle(WINDOW, c.color, c.location(), c.r)
        except ValueError:
            print(c.color)
            break


        pygame.display.flip() # Needed to update the screen
        counter += 1
    pygame.quit()

if __name__ == "__main__":
    main()

