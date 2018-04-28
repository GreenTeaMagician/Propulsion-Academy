class Paddle:
    def __init__(self, canvas):
        self.width = 100
        self.height = 15
        self.position_x = canvas[0] / 2 - 50
        self.position_y = canvas[1] - 20
        self.color = (0, 0, 0)
