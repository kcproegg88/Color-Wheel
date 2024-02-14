import pygame
import colored_shape

def draw(ringList, lineList, circleList, WINDOW):
    drawRings(ringList, WINDOW)
    drawLines(lineList, WINDOW)
    drawCircles(circleList, WINDOW)

def drawRings(ringList, WINDOW):
    for ring in ringList:
        for c in ring.generate_loop():
            c.color_change(ring.angle)
            pygame.draw.circle(WINDOW, c.color, c.location(), c.radius)


def drawLines(lineList, WINDOW):
    for line in lineList:
        for c in line.generate_line():
            c.color_change(line.angle)
            pygame.draw.circle(WINDOW, c.color, c.location(), c.radius)


def drawCircles(circleList, WINDOW):
    for c in circleList:
        c.color_change(c.angle)
        pygame.draw.circle(WINDOW, c.color, c.location(), c.radius)