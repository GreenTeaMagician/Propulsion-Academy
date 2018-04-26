
#COPY PASTED DUE TO LACK OF TIME
#Used to create classes for futher exercises during the course. 

class Restaurant:
    dishes = {}

    def __init__(self):
        pass

    def order_dish(self, dish, customer):
        if customer[id] not in self.dishes:
            self.dishes[customer[id]] = [dish]
            return

        self.dishes[customer[id]].append(dish)

    def print_check(self, customer):
        total = 0
        for key, value in self.dishes.items():
            if key == customer[id]:
                print("Customer: {}".format(customer['name']))
                for i, dish in enumerate(value):
                    total += dish.price
                    print("Order #{}: {} - {:0.2f}.-".format(i + 1, dish.dish, dish.price))
                print("Total: {:0.2f}.-".format(total))
                print("\n")

        if customer[id] not in self.dishes:
            print("{} has no orders!".format(customer['name']))

    def print_orders(self):
        total = 0
        all_dishes = []
        print("\nBill info")
        print("_" * 15)
        for key, value in self.dishes.items():
            for dish in value:
                all_dishes.append(dish)
                total += dish.price
        for dish in all_dishes:
            print("Order #{}: {:0.2f}.-".format(dish.dish, dish.price))
        print("Total: {:0.2f}".format(total))
        print("_" * 15)

    """
    Bonus points
    total_profit for the restaurant profit
    profit_from_customer 
    """

    def total_profit(self):
        total_p = 0
        for key, value in self.dishes.items():
            for dish in value:
                total_p += dish.profit()[0]
        print("Profit {:0.2f}.-:".format(total_p))

    def profit_from_customer(self, customer):
        total_p = 0
        for key, value in self.dishes.items():
            if key == customer[id]:
                for dish in value:
                    total_p += dish.profit()[0]
                print("Profit from {}'s orders was {}.-".format(customer['name'], total_p))

