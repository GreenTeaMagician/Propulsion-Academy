#-----------------------------------------------------------------------
#Exercise 1
#-----------------------------------------------------------------------
#Part 1.1

numArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def filter_even(arr):
	return list(filter(lambda x: x%2==0, arr))

#print(filter_even(numArray))
#-----------------------------------------------------------------------
#Part 1.2

def is_squares(arr):
	return list(map(lambda x: x*x, arr))

#print(is_squares(numArray))
#-----------------------------------------------------------------------
#Part 1.3

def squares_even(numArray):
	return list(map(lambda x: x*x, list(filter(lambda x: x%2==0, numArray))))

print(squares_even(numArray))
#-----------------------------------------------------------------------
#Part 1.4
#For loop version
def find_numbers(min, max):
	finalArray = []
	for n in range(min, max):
		if n%7==0 and n%5!=0:
			finalArray.append(n)
	return finalArray

print(find_numbers(1,100))
#--------------------------------
#Lambda function/Filter version
def find_numbers(min, max):
	return list(filter(lambda x: x%7==0 and x%5!=0, list(range(min, max))))

print(find_numbers(1,100))
#-----------------------------------------------------------------------
# Exercise 2
#-----------------------------------------------------------------------

orders = [
  {
    'id': 'order_001',
    'item': 'Introduction to Python', 
    'quantity': 1, 
    'price_per_item': 32
  }, 
  {
    'id': 'order_002',
    'item': 'Advanced Python', 
    'quantity': 3, 
    'price_per_item': 40
  
  },
  {
    'id': 'order_003', 
    'item': 'Python web frameworks', 
    'quantity': 2, 
    'price_per_item': 51
  }
]

#----------------------------------------
#Explicit for loop
def compute_totals(orders):
	finalArray = []
	for order in orders:
		if order['price_per_item'] * order['quantity'] < 100:
			order['price_per_item'] += 10
		finalArray.append((order['id'], order['price_per_item'] * order['quantity']))
	return finalArray
		
#print(compute_totals(orders))	


#----------------------------------------
#Optimization using map and lambda functions
def tempFunc(order):
	if order['price_per_item'] * order['quantity'] < 100:
		return (order['id'], order['price_per_item'] * order['quantity'] + 10)
	return (order['id'], order['price_per_item'] * order['quantity'])
	
def compute_totals(orders):
	return list(map(tempFunc, orders))
	
print(compute_totals(orders))

#-----------------------------------------------------------------------
#Exercise 3
#-----------------------------------------------------------------------

n = 10
def make_dict(n):
	sampleDict = {}
	for i in range(1,int(n)):
		sampleDict[i] = i*i
	return sampleDict
#n = input("Write a number: ")
print(make_dict(n))

###SOLVED BY INSTRUCTOR (I'm clearly not good at dictionaries yet)


#-----------------------------------------------------------------------
#Exercise 4
#-----------------------------------------------------------------------

#Solution 1: Long answer
def weird():
	workArray = [x*x for x in range(1,21)]
	return workArray[15:]
	
print(weird())

#Solution: Compact answer
def weird2():
	return list(map(lambda x: x*x, list(range(1,21))))[15:]
	
print(weird2())

#-----------------------------------------------------------------------
#Exercise 5
#-----------------------------------------------------------------------

numArray = list(range(1,11))

#Long answer
def even_odd(numArray):
	finalString = ''
	for n in numArray:
		if n % 2 == 0:
			finalString += str(n)
		else:
			finalString += '_'
	return finalString

print(even_odd(numArray))	

#Short answer
def charDefine(numArray):
	if numArray % 2 == 0:
		return str(numArray)
	return '_'

def evenString(n):
	return "".join(list(map(charDefine, list(range(1,n+1)))))
	
print(evenString(10))

#-----------------------------------------------------------------------
#Exercise 6
#-----------------------------------------------------------------------

def BMI_calc():
	print("Let's calculate your BMI (kg/m^2)")
	weightKg = input("First of all, what is your weight in kilograms? ")
	weightKg = float(weightKg)
	heightCm = input(f"Wonderful, so you are {str(weightKg)}. Now, how tall are you, in centimeters? ")
	BMI = weightKg / (int(heightCm)/100)**2
	print(f"Your BMI is {BMI}. This classifies you as " + classBMI(BMI))
def classBMI(BMI):
	if BMI < 18.5:
		return 'underweight'
	elif 18.5 <= BMI <= 25:
		return 'having a normal BMI index'
	elif 25 <= BMI <= 30:
		return 'overweight'
	else:
		return 'obese'

#BMI_calc()

#-----------------------------------------------------------------------
#Exercise 7
#-----------------------------------------------------------------------

shoppingList = {}
global i
i = 1
def help_menu(shoppingList):
	print("Hi! what do you want to do?\n")
	print("Type in 's' to show the items in your cart\nType in 'a' to add an item into you cart\nPress 'r' to remove an item from your cart\nPress 'q' to quit")
	while True:
		I = input("What do you want to do? ")
		if I in ['s', 'S', 'show', 'show items', 'showitems', 'showItems'] :
			show_items(shoppingList)
		elif I in['a', 'A', 'add', 'additem', 'addItem', 'add items']:
			add_item(shoppingList)
		elif I in ['r', 'R', 'remove', 'remove item', 'removeitem', 'removeItem']:
			remove_item(shoppingList)
		elif I in ['q', 'Q', 'quit']:
			print("Awesome! Here is your shopping list:")
			print(shoppingList)
			print("\nHave a nice day! <3")
			return
		else:
			print("I did not understand your input. Try again:")
			
def show_items(shoppingList):
	if shoppingList == {}:
		print("There is nothing in your list!")
	else:
		print(shoppingList)
	return
	
def add_item(shoppingList):
	i = len(shoppingList) + 1
	add = input("What do you want to add? ")
	shoppingList[i] = add
	i += 1
	return "Done!\n"
	
def remove_item(shoppingList):
	if shoppingList == {}:
		return "There are no items on the list!"
	removeItem = input("What do you want to remove? type in the number of your item: ")
	del shoppingList[int(removeItem)]
	print("Done!")
	

#help_menu(shoppingList)
#-----------------------------------------------------------------------
#Exercise 8
#-----------------------------------------------------------------------
import random

def start():
	randInt = random.randint(1,10)
	i = 5
	I = input('I am thinking of a number from 1-10. Can you find it? You have 5 tries. ')
	while True:
		int(I)
		i -= 1
		if int(I) == int(randInt):
			print("Yay! You did it!")
			break
		elif i == 1:
			print(checkStatus(I, randInt))
			I = input(f"Nope! Guess again! You have {i} try left! ")
			try:
				int(I)
			except:
				print("Your entry was not an integer! Cheater! You lose one turn! ")
				print(f"You have {i} try left!")
			continue
		elif i != 1 and i != 0:
			print(checkStatus(I, randInt))
			try:
				int(I)
			except:
				print("Your entry was not an integer! Cheater! You lose one turn! ")
				print(f"You have {i} try left!")
			I = input(f"Nope! Guess again! You have {i} tries left! ")
		else:
			print("You've run out of tries! I win! Ha-ha!")
			break
	a = input("Play again? Type 'y' for yes, anything else for no:\n")
	if a in ['y', 'yes']:
		play_again()
	
def play_again():
	start()
	
def checkStatus(I, randInt):
	if int(I) < int(randInt):
		return "My number is HIGHER"
	elif int(I) > int(randInt):
		return "My number is LOWER"
	else:
		return

#start()
#-----------------------------------------------------------------------
