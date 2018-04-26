cities = ['Zurich', 'Bern', 'Lausanne', 'Luzern']
for city in cities:
	print(city)

for i in range(len(cities)):
	print(f"Index {i} contains {cities[i]}")

doubles = []
for i in range(4):
	doubles.append(i*2)
	
print(doubles)

print([i*2 for i in range(4)])

cars = ['BMW', 'Audi', 'Porsche', 'Opel']
[car for car in cars if car != "Opel"]
#is the same thing as 

result = []
for car in cars:
	if car != 'Opel':
		result.append(car)
		
[c for c in 'Propulsion Academy' if c.isupper()]

[x*2 for x in range(10) if x > 5]

[x for x in range(20) if x%3==0]

[x*y for x in [1, 2, 3] for y in [10, 100]]
#is the same as 

result = []
for x in [1,2,3]:
	for y in [10, 100]:
		result.append(x*y)


#print(set([1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4]))

my_list = [1, 2, 3, 4, 5]
iseq = iter(my_list)

#print(next(iseq))
#print(next(iseq))
#print(next(iseq))
#print(next(iseq))
#print(next(iseq))


def is_positive(x):
	if x > 0:
		return True
	else:
		return False
		
#MUCH MORE CONCISE:

def is_positive():
	return x > 0

def zero_sum():
	for i in range(len(arguments)):
		print(f"i = {i} arguments[i]={arguments[i]}")
					
		for j in range(len(arguments)):
			print(f"j = {j} arguments[j]={arguments[j]}")
#List comprehensiopn: when a list is given in a single line with a for loop in it
arguments = [1, 5, 0, -5, 3, -1]
#print([(i,j) for i in range(len(arguments)) for j in range(len(arguments)) if arguments[i] - arguments[j] == 0])


#-----------------------------------------------------------------------
#Coffee break
#-----------------------------------------------------------------------

##FUNCTIONS

def say_name(string):
	print(f"hello, my name is {name}")

def describe_movie(title, genre):
	print(f"Movie {title} has genre {genre}")
	
sw_title = "star wars"
sw_genre = "fantasy"

print(describe_movie("Green Room", "Horror"))
print(describe_movie(genre = "Drama", title = "Star Wars"))

def describe_show(title, genre, producer = 'Netflix', country = 'USA'):
	print(f"Movie {title} has genre {genre}, produced by {producer} in {country}")

describe_show("Jessica Jones", "Horror")
	

def example_vars(*args):
	print(args)

#Enumerate: 
arr = ['a', 'c', 'b']
for el in arr:
	print(el)
##THIS...
for i in range(len(arr)):
	print(f"index {i} element {arr[i]}")
	
def example_vars(*args):
	#...AND THIS...
	for i, el in enumerate(args):
		print(f"index {i} element {el}")
#...ARE THE SAME
example_vars('a', 'c', 'b')

#The multipkly sign inside in function parameter means some number of parameters.
#This will only work on positional arguments, not keyword arguments

def fun(*args):
	res = 0
	for a in args:
		res += a
	return res

#fun(1)
#fun()

def fun(**args):
	for key, val in args.items():
		print(f"Key is {key} has value {val}")

#** create a dictionary of keywords and values

def fun(**args):
	print(args)
#fun(twenty=20, thirty=30)

def mixed(*args, **kwargs):
	print(f"args is {args}")
	print(f"kwargs is {kwargs}")


def make_dict(**kwargs):
	return kwargs

make_dict(Key1=1, Key2=2)

def create_user(name, password, **kwargs):
	user = {}
	user['name'] = name
	user['password'] = password
	for key, value in kwargs.items():
		user[key] = value
	return user

#print(create_user("Donald", 'asdf'))

#print(create_user('Donald', 'asdf', full_name='Donald Duck', age='150'))

#This imports functions from different python files
from recipes import *
#print_ingredients('Cake', flour='100g', eggs='1')

#----------------------------------------------------------------------
#FUNCTIONAL PROGRAMMING
#----------------------------------------------------------------------

def say_hello(name):
	print(f"hello my name is {name}")

say = say_hello

say("Michal")

print(say == say_hello)

def greeting(intro_fn, name):
	print("Hi there!")
	intro_fn(name)
	print("Nice to meet you!")

greeting(say_hello, 'Michal')

def fancy_greeting(name):
	print(f"Hello there I am Sir {name}")

greeting(fancy_greeting, "Michal")

def sqr(x):
	return x*x
#lambda functions
sqr_l = lambda x: x*x

sqr_l(2)

mul = lambda x,y: x*y
print(mul(10, 20))

def mult(arr):
	new_list = []
	for element in arr:
		new_list.append(element*2)
	
	return new_list

print(mult([1, 10, 100]))

def multiply_2(val):
	return val*2

print(list(map(multiply_2, [1, 10, 100])))

print(list(map(lambda x: x*2, [1, 10, 121])))

countries = ['Switzerland', 'USA', 'Russia', 'Panama']

#print(list(map(len, countries)))

[len(c) for c in countries]

def times2(x): return x*2
def times3(x): return x*3
#-----------------------------
fun = [times2, times3]
#print(list(map(lambda a: a(10), fun)))
print(list(map(lambda n: list(map(lambda a: a(n), fun)), [1, 2, 3])))
#SAME THING AS 
print([[f(i) for f in fun] for i in [1,2,3]])

# i = stuff youre appending
# f = object	 in array
# [1,2,3] = array
# fun
#SAME THING AS 
result = []
for i in [1,2,3]:
	arr = []
	for f in fun:
		arr.append(f(i))
	result.append(arr)
#print(result)


numbers = [10,20,30,40,50,60,70,80,90]
print(list(filter(lambda x: x%3==0, numbers)))

numbers1 = [-1, 0, 1, 2, 3, 4, 5]
list(filter(lambda a: a<2, numbers))

numbers2 = [ 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(lambda a: a in numbers1, numbers2)))
n = 8
def make_dict(**kwargs):
	return kwargs

kwargs = n
