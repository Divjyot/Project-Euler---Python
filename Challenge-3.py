'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

import operator

X = 600851475143
primeList = []
start = 2

while True:

    if X % start != 0:
        start += 1
    else:
        if start == X:
                primeList.append(start)
                break
        else:
                primeList.append(start)
                X = int(X/start)
                start = 2

# To print the prime list items
print("Prime Factors of ", X, ": ")

for x in primeList:
    print(x)

print("Largest Prime factor")

print("Getting Last item from list. Assumes list is sorted in ascending order", primeList[-1])
# or

print(max(primeList))

print("Using Max unction and operator.itemgetter, from what I understand is max(iterableThing,key= someFunction)",
      "the key is applied to each element of the iterable then the max value after applying the key or we can say",
      "running each element in iterable through the someFunction and then getting item in iterable who has",
      "largest value of someFunction(iterableItem)")
print("not sure why it throw TypeError")
print(max(primeList, key=operator.itemgetter(1)))

