
# These are a set of exercises that we have been asked to complete. Each
# exercise is given a number, and examples of what must be true of the 
# output in order to complete the exercise. 

#Exercise 1

def is_string(possibleString):
	try:
		possibleString + "a"
		return True
	except:
		return False
		
#Answer:

def is_string(text):
    return type(text) is str
    
#print(is_string('hello'))  # True
#print(is_string(['hello']))  # False
#print(is_string('this is a long sentence'))  # True
#print(is_string({'a': 2}))  # False

#Exercise 2

possibleString = 'Me & Amanda'
def is_only_string(possibleString):
	specialCharArray = [' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	stringValue = is_string(possibleString)
	if stringValue == False:
		return False
	for char in possibleString:
		#print(char)
		if char in specialCharArray:
			return False
	return True
	
#Answer:
def is_only_string(text):
    return is_string(text) and ' ' in text and bool(len([n for n in text if n.isdigit()]))

#print(is_only_string('11'))  # False
#print(is_only_string(['hello']))  # ? Please handle this case!! Should return False
#print(is_only_string('this is a long sentence'))  # False
#print(is_only_string({'a': 2}))  # # ? Please handle this case!! Should return False
#print(is_only_string("ThisIsOnlyAStupidString***&^%$#"))

#Exercise 3

def is_alphanumeric(hopefullyAlphanumeric):
	#Tests if input is a string (from Exercise 1)
	try:
		hopefullyAlphanumeric + "a"
	except:
		return False
	#The rest checks for alphanumerls and makes sure string is not empty
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
			  'l', 'm', 'n', 'o', 'p', 'k', 'q', 'r', 's', 't', 'u', 
			  'v', 'w', 'x', 'y', 'z']
	numerals = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
	
	if hopefullyAlphanumeric == '':
		return False
	for char in hopefullyAlphanumeric:
		if char not in (letters + numerals) or char == ' ':
			return False
	return True

#Answer:
def is_alphanumeric(text):
    return is_string(text) and bool(len([n for n in text if n.isdigit()]) == len(text))


#print(is_alphanumeric('11'))  # True
#print(is_alphanumeric(['hello']))  # False
#print(is_alphanumeric('this is a long sentence'))  # False
#print(is_alphanumeric({'a': 2}))  # False
#print(is_alphanumeric("this is string....!!!"))  # False

#Exercise 4

def is_array_or_tuple(someObject):
	if str(type(someObject)) == "<class 'tuple'>" or str(type(someObject)) == "<class 'list'>":
		return True
	return False
	
#Answer:
def is_array_or_tuple(argument):
    return type(argument) in [list, tuple]	
	
#print(is_array_or_tuple('hello'))  # False
#print(is_array_or_tuple(['hello']))  # True
#print(is_array_or_tuple([2, {}, 10]))  # True
#print(is_array_or_tuple({'a': 2}))  # False
#print(is_array_or_tuple((1, 2)))  # True
#print(is_array_or_tuple(set())) #False

#Exercise 5
def are_same_type(someArray):
	arrType = type(someArray[0])
	for thing in someArray:
		if arrType != type(thing):
			return False
	return True

#Answer:
def are_same_type(my_list):
    iseq = iter(my_list)
    first_type = type(next(iseq))
    return True if all((type(x) is first_type) for x in iseq) else False
    
#print(are_same_type(['hello', 'world', 'long sentence']))  # True
#print(are_same_type([1, 2, 9, 10]))  # True
#print(are_same_type([['hello'], 'hello', ['bye']]))  # False
#print(are_same_type([['hello'], [1, 2, 3], [{'a': 2}]]))  # True
#print(are_same_type([['hello'], set('hello')]))  # False

#Exercise 6
a = 'xyaabbbccccdefww'
b = 'xxxxyyyyabklmopq'
x = 'abcdefghijklmnopqrstuvwxyz'

def longest_string(string1, string2):
	finalArray = []
	finalString = ''
	for char in string1:
		if char not in finalArray:
			finalArray.append(char)
	for char in string2:
		if char not in finalArray:
			finalArray.append(char)
	return "".join(sorted(finalArray))
	
#Answer:
def longest_string(a, b):
    c = a + b
    chars = []
    for char in c:
        if char not in chars:
            chars.append(char)
    return ''.join(list(sorted(chars)))

#print(longest_string(a, b))  # abcdefklmopqwxy
#print(longest_string(a, x))  # abcdefghijklmnopqrstuvwxyz

#Exercise 7
import random

def convert(num):
	if str(type(num)) != "<class 'int'>":
		return False
	finalArray = []
	numsArray = list(str(num))
	for char in numsArray:
		finalArray.insert(random.randint(0, len(numsArray)), char)
	return finalArray

#Answer:
def convert(number):
    numbers_list = [int(n) for n in str(number)]
    return sorted(numbers_list, reverse=True)

#print(convert(429563))  # [9, 6, 5, 4, 3, 2]
#print(convert(324))  # [4, 3, 2]

#Exercise 8

def count_repetition(array):
	dictPpl = {}
	for ppl in array:
		if ppl in dictPpl:
			dictPpl[ppl] += 1
			continue
		dictPpl[ppl] = 1
	return dictPpl
	
#print(count_repetition(['kerouac', 'fante', 'fante', 'buk', 'hemingway', 'hornby', 'kerouac', 'buk', 'fante']))
# {'kerouac': 2, 'fante': 3, 'buk': 2, 'hemingway': 1, 'hornby': 1}

#Answer:

def count_repetition(argument):
    output = {}
    for element in argument:
        if element in output:
            output[element] += 1
        else:
            output[element] = 1
    return output

#print(count_repetition(['kerouac', 'fante', 'fante', 'buk', 'hemingway', 'hornby', 'kerouac', 'buk', 'fante']))

#Exercise 9

def is_caught(someString):
	if not is_string(someString):
		return False
	i = 0
	dot = 0
	sampleString = ''
	for char in someString:
		if char == 'C':
			sampleString = someString[i+1:len(someString)]
		else:
			i += 1
	for char in sampleString:
		if char == '.':
			dot += 1
		elif char == 'm':
			break
		else:
			continue
	if dot < 3:
		return True
	else:
		return False

#Answer:
def is_caught(argument):
    cat_and_mouse = list(argument)
    c = cat_and_mouse.index('C')
    m = cat_and_mouse.index('m')
    return True if m - c <= 3 else False #This can also be shortened

#print(is_caught(['C.....m']))  # False
#print(is_caught('C..m'))  # True
#print(is_caught('..C..m'))  # True
#print(is_caught('...C...m'))  # False
#print(is_caught('C.m'))  # True

#Exercise 10

group = {
    'Amy': 20,
    'Bill': 15,
    'Chris': 10
}

def split_the_bill(group):
	groupWork = group
	i = 0
	for num in list(groupWork.values()):
		i += int(num)
	average = i / len(list(groupWork.values()))
	for key, value in groupWork.items():
		groupWork[key] =  average - groupWork[key]
	return groupWork
	
#Answer:

def split_the_bill(obj):
    output = {}
    average = sum(obj.values()) / len(obj)
    for key, value in obj.items():
        output[key] = round(average - value)
    return output
    
#print(split_the_bill(group))  # { 'Amy': -5, 'Bill': 0, 'Chris': 5 }

#Exercise 11

def exp_recursive(num1, num2):
	i = 1
	if(num2 != 0):
		i *= (exp_recursive(num1, num2-1))
	else:
		return 1
	i = i * num1
	return i	
		
#Answer number 1:

def exp(num, exponent):
    if exponent == 0:
        return 1
    result = 1
    for i in range(exponent):
        result *= num
    return result
    
#Answer number 2:
def exp_recursive(num, exponent):
    if exponent == 0:
        return 1
    else:
        return num * exp_recursive(num, exponent - 1)
    
#print(exp_recursive(5, 3))  # 125
#print(exp_recursive(2, 4))  # 16
#print(exp_recursive(5, 1))  # 5
#print(exp_recursive(6, 0))  # 1

#Exercise 12

def zero_sum(array):
	arrayWork = array
	finalArray = []
	for num1 in array:
		for num2 in array:
			if num1 + num2 == 0:
				finalArray.append([array.index(num1), array.index(num2)])
				arrayWork.remove(num2)
	return finalArray
	
print(zero_sum([1, 5, 0, -5, 3, -1]))  # [[0, 5], [1, 3], [2, 2]]
print(zero_sum([1, -1]))  # [[0, 1]]
print(zero_sum([0, 4, 3, 5]))  # [[0, 0]]
print(zero_sum([0, 4, 3, 5, -4, -5, -3, 2 ,-2, 0, 0, -1])) #custom

#Answer:		
def zero_sum(arguments):
    output = []
    temp = []
    for i in arguments:
        for j in arguments:
            if i + j == 0:
                first_number = arguments.index(i)
                second_number = arguments.index(j)
                if first_number not in temp and second_number not in temp:
                    temp.append(first_number)
                    temp.append(second_number)
                    output.append([first_number, second_number])
    return output
	
print(zero_sum([1, 5, 0, -5, 3, -1]))  # [[0, 5], [1, 3], [2, 2]]
print(zero_sum([1, -1]))  # [[0, 1]]
print(zero_sum([0, 4, 3, 5]))  # [[0, 0]]
print(zero_sum([0, 4, 3, 5, -4, -5, -3, 2 ,-2, 0, 0, -1])) #custom

#Exercise 13
	
def caseCounter(someString):
	upper = list(('abcdefghijklmnopqrstuvwxyz').upper())
	lower = list(('abcdefghijklmnopqrstuvwxyz').lower())
	upperNum = 0
	lowerNum = 0
	for char in someString:
		if char in upper:
			upperNum += 1
		elif char in lower:
			lowerNum += 1
		else:
			continue
	return "UPPERCASE " + str(upperNum) + " LOWERCASE " + str(lowerNum)

#Answer:

def upper_lower(data):
    d = {"UPPER CASE": 0, "LOWER CASE": 0}
    for c in data:
        if c.isupper():
            d["UPPER CASE"] += 1
        elif c.islower():
            d["LOWER CASE"] += 1
    return d
    
#print(caseCounter("merkgbkEHABERIHBakehgluahrHUAERGAER"))	
	
#Exercise 14
def new_dict(array):
	arrayDic = {}
	arrayWork = array
	for char in array:
		key = char
		arrayWork = arrayWork[1:]
		arrayDic[key] = new_dict(arrayWork)
		break
	return arrayDic

#Answer:

def new_dict(arg):
    the_new_dict = current = {}
    for name in arg:
        current[name] = {}
        current = current[name]
    return the_new_dict
print(new_dict([1, 2, 3, 4, 5])) # {1: {2: {3: {4: {5: {}}}}}}

#Exercise 15


#Exercise 16
#Exercise 17
#Exercise 18

def write_number(num):
	dictNum = {
		1: 'one',
		2: 'two',
		3: 'three',
		4: 'four',
		5: 'five',
		6: 'six',
		7: 'seven',
		8: 'eight',
		9: 'nine',
		10: 'ten',
		11: 'eleven',
		12: 'twelve',
		13: 'thirteen',
		15: 'fifteen',
		20: 'twenty',
		30: 'thirty',
		40: 'forty',
		50: 'fifty'
	}
	if len(list(str(num))) == 1:
		return dictNum[num]
	elif len(list(str(num))) == 2:
		try:
			return dictNum[num]
		except:
			try:
				if dictNum[int(str(list(str(num))[0]) + '0')] == 'ten':
					if dictNum[int(str(list(str(num))[1]))] == 'eight':
						return 'eighteen'
					return dictNum[int(str(list(str(num))[1]))] + 'teen'
				else:	
					return dictNum[int(str(list(str(num))[0]) + '0')] + '-' + dictNum[int(list(str(num))[1])]
			except:
				return dictNum[int(str(list(str(num))[0]))] + 'ty-' + dictNum[int(list(str(num))[1])]
	elif len(list(str(num))) == 3:
		tenner = ''
		try:
			tenner = dictNum[num]
		except:
			try:
				if dictNum[int(str(list(str(num))[1]) + '0')] == 'ten':
					if dictNum[int(str(list(str(num))[2]))] == 'eight':
						tenner = 'eighteen'
					tenner = dictNum[int(str(list(str(num))[2]))] + 'teen'
				else:	
					tenner = dictNum[int(str(list(str(num))[1]) + '0')] + '-' + dictNum[int(list(str(num))[2])]
			except:
				tenner = dictNum[int(str(list(str(num))[1]))] + 'ty-' + dictNum[int(list(str(num))[2])]
		return dictNum[int(str(list(str(num))[0]))] + "-hundred and " + tenner
	else:
		return "fuck you"
		
print(write_number(11)) # "eleven"
print(write_number(2)) # "two"
print(write_number(32)) # "thirty-two"
print(write_number(764)) # "sixty-four"


