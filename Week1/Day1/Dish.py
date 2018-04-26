

#COPY PASTED DUE TO LACK OF TIME
#Used to create classes for futher exercises during the course. 

class Dish:
    def __init__(self, dish, price, ingredients):
        self.dish = dish
        self.ingredients = ingredients
        self.price = price

    def __str__(self):
        return self.dish

    def cost(self):
        total = 0
        fixed_price = 10
        for dish in self.ingredients:
            total += int(dish.price)
        return total + fixed_price

    def profit(self):
        the_profit = self.price - self.cost()
        return the_profit, self.dish
