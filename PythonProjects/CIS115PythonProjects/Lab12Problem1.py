__author__ = 'Michele'

##Write a program to do the following:

# (a)	Generate 10 random integers in the range of 1 through 4.
# Store them in a list named list1.
# Display list1.
# (b)	Create a new list named list2.
# Copy all the elements of list1 there using concatenation.
# Display list2.
# (c)	Create a new list named list3.
# Copy all the elements of list1 there using append.
# Display list3.
# (d)	Create a new list named list4.
# Copy all the elements of list1 there using list slicing.
# Display list4.

import random
randomIntegers1 =[]
randomIntegers2 =[]
randomIntegers3 =[]
for i in range (10):
    randomIntegers1.append(random.randrange(1,5,1))
print(randomIntegers1)
print()
randomIntegers2 = randomIntegers1 + randomIntegers2
print(randomIntegers2)
print()
randomIntegers3.append(randomIntegers1)
print(randomIntegers3)
print()