class Ball:
    def __init__(self, canvas):
        self.diameter = 14
        self.radius = self.diameter / 2
        self.velocity = [1, -1]
        self.position_x = canvas[0] / 2 - self.radius
        self.position_y = canvas[1]
        self.color = (0, 0, 255)
        self.velocity = [4, -4]
