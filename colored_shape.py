import math


class colored_shape:
    def __init__(self, origin, distance=100, angle=0, color=(0, 0, 0), base=0, peak=255, period=2*math.pi):
        self.origin = origin
        self.d = distance
        self.angle = angle
        self.color = color
        self.min = base
        self.max = peak
        self.range = peak - base
        self.period = period

    def location(self):
        x = int(math.cos(self.angle) * self.d + self.origin[0])
        y = int(math.sin(self.angle) * self.d + self.origin[1])
        return x, y

    def color_change(self):
        r, g, b = self.color
        f = (math.pi*2)/self.period
        r = max(min(int(math.cos(self.angle * f)*self.range + self.min + self.range/2), self.max), self.min)
        g = max(min(int(math.cos(self.angle * f - math.pi * 2/3) * self.range + self.min + self.range/2), self.max), self.min)
        b = max(min(int(math.cos(self.angle * f + math.pi * 2/3) * self.range + self.min + self.range/2), self.max), self.min)

        self.color = (r,g,b)


class Circle(colored_shape):
    def __init__(self, radius, origin, distance=100, angle=0, color=(0, 0, 0), base=0, peak=255, period=2*math.pi):
        super().__init__(origin, distance, angle, color, base, peak, period)
        self.radius = radius
