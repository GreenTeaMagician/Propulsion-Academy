class House:

    def __init__(self):
        self._walls = []
        self._holes = []

    def register_wall(self, shape):
        self._walls.append(shape)

    def register_hole(self, shape):
        self._holes.append(shape)

    def get_wall_area(self):
        return sum(map(lambda w : w.get_area(), self._walls)) - sum(map(lambda w : w.get_area(), self._holes))

    def draw(self)   
     
    def create_house():		
        base_wall = Rectangle(5, 8, 5, 8)
        roof_wall = Triangle(2, 4, 2, 4)
        door = Rectangle(1.2, 2, 1.2, 2)
        window = Rectangle(0.8, 0.8, 0.8, 0.8)
        window2 = Circle(0.5, 0.5, 0.5, 0.5)
        myHouse = House()
        myHouse.register_wall(base_wall)
        myHouse.register_wall(roof_wall)
        myHouse.register_hole(door)
        myHouse.register_hole(window)
        myHouse.register_hole(window2)

