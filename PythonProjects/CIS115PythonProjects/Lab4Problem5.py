__author__ = 'Michele'

#Initial age question and valid entry test
age = int(input('Enter the child\'s age: '))
BooleanValidAge = age <= 200

#Is age entry valid
while BooleanValidAge == False:
    print('Invalid entry.  Please re-enter a valid age for the child.')
    age = int(input('Enter the child\'s age: '))
    BooleanValidAge = age <= 200
#end valid age entry loop

#Initial military question and valid entry test
military = str(input('Are you a member of the military forces?  Please type "1" for YES or "2" for NO.  '))
BooleanValidmilitary = military == '1' or military == '2'

#Is the entry valid
while BooleanValidmilitary == False:
    print('Invalid entry.  Please type "1" for YES or "2" for NO.  ')
    military = str(input('Are you a member of the military forces?  Please type "1" for YES or "2" for NO.  '))
    BooleanValidmilitary = military == '1' or military == '2'
#end valid military entry loop

BooleanAgeMilitary = age < 12 or military == '1'
if BooleanAgeMilitary == True:
    Admission = 10
    print('Please pay $' + format(Admission, ',.0f') + ' for admission.')
#There is extra sunlight
else:
    print('Please pay $20 for admission.')