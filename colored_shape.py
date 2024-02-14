import math


class colored_shape:
    def __init__(self, origin, distance=100, angle=0.0, color=(0, 0, 0), base=0, peak=255, period=2*math.pi):
        self.origin = origin
        self.d = distance
        self.angle = angle
        self.color = color
        self.base = base
        self.peak = peak
        self.range = peak - base
        self.period = period

    def location(self):
        x = int(math.cos(self.angle) * self.d + self.origin[0])
        y = int(math.sin(self.angle) * self.d + self.origin[1])
        return x, y

    def color_change(self, phase_shift):
        r, g, b = self.color
        f = (math.pi*2)/self.period
        r = max(min(int(math.cos(self.angle * f + phase_shift)*self.range + self.base + self.range/2), self.peak), self.base)
        g = max(min(int(math.cos(self.angle*f-math.pi*2/3 + phase_shift)*self.range + self.base+self.range/2), self.peak), self.base)
        b = max(min(int(math.cos(self.angle*f+math.pi*2/3 + phase_shift)*self.range + self.base+self.range/2), self.peak), self.base)

        self.color = (r,g,b)


class Circle(colored_shape):
    def __init__(self, radius, origin, distance=100, angle=0.0, color=(0, 0, 0), base=0, peak=255, period=2*math.pi):
        super().__init__(origin, distance, angle, color, base, peak, period)
        self.radius = radius


class Ring(colored_shape):
    def __init__(self, circle_num, radius, origin, dark=False, angle_rate=1, distance=100, width=100, angle=0, color=(0, 0, 0), base=0, peak=255, period=2*math.pi):
        super().__init__(origin, distance, angle, color, base, peak, period)
        self.circle_num = circle_num
        self.radius = radius
        self.angle_rate = angle_rate/180*math.pi
        self.width = width
        self.dark = dark

    def generate_loop(self):
        # Handles grey scaling for a line
        separation = self.width / self.circle_num
        color_grad = (self.peak - self.base) / self.circle_num
        circle = []
        for j in range(int(2 * math.pi / self.angle_rate)):
            line = [Circle(self.radius, self.origin, self.d - separation * i, self.angle_rate*j, self.color, (color_grad * i + self.base) * (not self.dark), 255 - color_grad * i * self.dark, self.period) for i in range(self.circle_num)]
            circle.extend(line)
        return circle


class Line(colored_shape):
    def __init__(self, circle_num, radius, origin, dark=False, angle_rate=1, distance=100, width=100, angle=0, color=(0, 0, 0), base=0, peak=255, period=2*math.pi):
        super().__init__(origin, distance, angle, color, base, peak, period)
        self.circle_num = circle_num
        self.radius = radius
        self.angle_rate = angle_rate/180*math.pi
        self.width = width
        self.dark = dark

    def generate_line(self):
        separation = int(self.width / self.circle_num)
        color_grad = int((self.peak - self.base) / self.circle_num)
        line = [Circle(self.radius, self.origin, self.d - separation * i, self.angle, self.color, (color_grad * i + self.base) * (not self.dark), 255 - color_grad * i * self.dark, self.period) for i in range(self.circle_num)]
        return line
