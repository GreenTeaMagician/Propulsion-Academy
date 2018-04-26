# Exercise 0

def multiply(a,b):
    minus = False
    if bool(a<0) != bool(b<0):
        minus = True
    aNew, bNew, more= abs(a), abs(b), 0
    if b == 0: 
        return 0
    more += multiply(aNew, bNew-1) + aNew
    if minus: 
        return -more
    else: 
        return more

print(multiply(-6,16))



# Exercise 1
L = [12, 14, 65, 43, 78, 37, 95, 24, 5]
q = 14

def binarySearch(array, query):
    half = int(len(array)/2)
    if query not in array:
        return -1
    if query == array[half]:
        return half
    elif query > array[half]:
        return binarySearch(array[half:], query) + half
    else:
        return binarySearch(array[:half], query)
print(sorted(L))
print(binarySearch(sorted(L), q))

# Exercise 2
# See other files, regrading the maze problem

# Exercise 3
L = [12, 14, 65, 43, 78, 37, 95, 24, 5]

def selectionSort(L):
    L_unsorted = L
    L_sorted = []

    for n in L_unsorted:
        low = n[0]
        for m in L_unsorted:
            if m < low:
                low = m
        L_sorted.append(low)
        L_unsorted.delete(m)




# Exercise 4

