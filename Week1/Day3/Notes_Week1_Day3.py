#**fun(**args) is an easy way to create a dictionary. It accepts 
#arguments in the form of name='Michal', or more generally, key=value

def fun(**args):
	for key, val in args.items():
		print(f"Key is {key} has value {val}")
		
fun(name='Michal', age=26, hometown='Rheinfelden')

#*args accepts as many arguments as you want, in the form of 'Michal, 
#or 26, or even arrays such as ['I', 'am', 'Mufasa']
def fun2(*args):
	print(args)

fun2("Michal", 26, "Rheinfelden")


from Car2 import Car2

testCar = Car2('BMW', 'X2')

print(testCar.model)

from Teachers import *

teacher1 = Teachers('MrBrocket')

#Magic methods are those methods that start with "__". These functions 
#are reseverd by python for certain functions that apply to all classes

class Words:
	def __init__(self):
		self.words = []
	
	def add(self, word):
		self.words.append(word)
	
	def __len__(self):
		return len(self.words)
		
	def __prop__(self):
		return "Rocket"

sentence = Words()

sentence.add("Hello")
sentence.add("Michal!")
print(len(sentence))
print(sentence.__prop__())


def normalize(a,b):
	try:
		sum = a+b
		return (a/sum, b/sum)
	except:
		return "Divided by zero (error). You have destroyed a universe. Be careful next time..."

print(normalize(0, 0))


import collections

Person = collections.namedtuple("Person", "name age gender")
laurent = Person(name='Laurent', age=26, gender='male')
print('Representation:', laurent)



#print(laurent.age)

from Teachers import *

cevey = Teachers('Cevey')
#print(cevey.name)

from collections import *

import collections

#print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
#print(collections.Counter({'a': 2, 'b': 3, 'c': 1}))
#print(collections.Counter(a=2, b=3, c=1))


from Book import *

from Book import *
books = [("The Ocean at the End of the Lane", "Neil Gaiman")]
book1 = Book("The Ocean at the End of the Lane", "Neil Gaiman")
bookcase1 = Bookcase(books)
#print(bookcase1[0])
print('--------------------------------------')
for i in bookcase1:
	print(i)
print('--------------------------------------')
from quark import *

upQ = quark('Up')
downQ = quark('Down')
#print('test')
#print((str(upQ)[0]))
#print(upQ.symbol())

qtypeList = ['Up', 'Up', 'Down']
chargeList = [0.666, 0.666, -0.333]
lquarkList = [upQ, upQ, upQ]


proton = nucleon(qtypeList, chargeList, lquarkList)
for i in proton:
	print(i)
#print(str(i) for i in proton.whatisit())
print([i for i in proton])
print(proton.whatisit())

hydrogenNucleons = [proton]
HeliumNucleons = [proton, proton, neutron, neutron]
