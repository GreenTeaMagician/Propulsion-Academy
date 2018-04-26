
from Inheritance.House import *
from Inheritance.Shapes import *

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

print(f"My House is has a wallsize of {myHouse.get_wall_area()}")
