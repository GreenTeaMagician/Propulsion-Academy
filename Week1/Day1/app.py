
#COPY PASTED DUE TO LACK OF TIME
#Used to create classes for futher exercises during the course. 

from Dish import Dish
from Restaurant import Restaurant
from Ingredients import Ingredients


pesto = Ingredients('pesto', 10)
print(pesto)
pluto = {
    'name': 'Pluto',
    id: 1
}

goofy = {
    'name': 'Goofy',
    id: 2
}

donald = {
    'name': 'Donald',
    id: 3
}

cheese = Ingredients('Cheese', 5)
pepperoni = Ingredients('Pepperoni', 10)
dough = Ingredients('Dough', 2)
lettuce = Ingredients('Lettuce', 3)
tomato = Ingredients('Tomato', 4)
pizza = Dish("Pizza", 35, [cheese, pepperoni, dough])
salad = Dish("Salad", 30, [lettuce, cheese, tomato])

print(pizza)
print(salad)
print("This pizza costs you: {}".format(pizza.cost()))
print("The profit on this {} was {}.-".format(pizza.profit()[1], pizza.profit()[0]))
print("\n")
restaurant = Restaurant()

# ordering dishes:
restaurant.order_dish(pizza, goofy)
restaurant.order_dish(salad, pluto)
restaurant.order_dish(salad, goofy)
restaurant.order_dish(pizza, goofy)
restaurant.print_check(goofy)
restaurant.print_check(pluto)
restaurant.print_check(donald)
restaurant.print_orders()
# bonus points
restaurant.total_profit()
# restaurant.profit_from_customer(pluto)
# restaurant.profit_from_customer(goofy)
