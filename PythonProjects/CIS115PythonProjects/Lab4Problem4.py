__author__ = 'Michele'
#How to test either a string or numeric
#Initial age question and valid entry test
age = int(input('Enter the child\'s age: '))
BooleanValidAge = age <= 200

#Is age entry valid
while BooleanValidAge == False:
    print('Invalid entry.  Please re-enter a valid age for the child.')
    age = int(input('Enter the child\'s age: '))
    BooleanValidAge = age <= 200
#end valid age entry loop

#Initial weight question and valid entry test
weight = int(input('Enter the child\'s weight: '))
BooleanValidWeight = weight <= 1000

#Is the entry valid
while BooleanValidWeight == False:
    print('Invalid entry.  Please re-enter a valid weight for the child.')
    weight = int(input('Enter the child\'s weight: '))
    BooleanValidWeight = weight <= 1000
#end valid weight entry loop

BooleanAgeWeight = age < 8 or weight < 70
if BooleanAgeWeight == True:
    print('The child is required to ride in a booster seat according to North Carolina state law.')
#There is extra sunlight
else:
    print('The child is no longer required to ride in a booster seat according to North Carolina state law.')