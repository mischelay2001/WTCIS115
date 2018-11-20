__author__ = 'Michele'

# Write a program to do the following:

# (a)	Generate 10 random integers in the range of 1 through 4.
# Store them in a list named list1.
# Display list1.
# (b)	Create a new list named list2.
# Copy the last 5 elements in list1 there.
# Display list2.
# (c)	Remove all occurrences of 2 from list2.
# Display the list.
# There should be no 2s in there anymore.

import random
randomIntegers1 =[]
randomIntegers2 =[]
for i in range (10):
    randomIntegers1.append(random.randrange(1,5,1))
print(randomIntegers1)
print()
randomIntegers2 = randomIntegers1[5:]
print(randomIntegers2)
print()
removeVal = 2
while removeVal in randomIntegers2:
    #find the first instance
    position = randomIntegers2.index(removeVal)
    del randomIntegers2[position]
print(randomIntegers2)