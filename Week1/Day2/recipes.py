def print_ingredients(name, **kwargs):
	print(f"Recipe for {name} is: ")
	for ingredient, amount in kwargs.items():
		print(f" - {ingredient}: {amount}")

print_ingredients('Cake', flour='100g', eggs='1')
