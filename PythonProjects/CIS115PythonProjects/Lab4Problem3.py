__author__ = 'Michele'
length = int(input('Enter length of tank in inches: '))
width = int(input('Enter width of tank in inches: '))
height = int(input('Enter height of tank in inches: '))
BTU = length * width * height * 3.5

#Initial question and valid entry test
ExtraSunlight = str(input('Does the room have extra sunlight?  Please type "1" for YES or "2" for NO.  '))
BooleanValidEntry = ExtraSunlight == '1' or ExtraSunlight == '2'

#Is the entry valid
#repeat until entry is valid
#how to unrestrict entry to not be case sensitive?
#how can the following expression be simplified?
while BooleanValidEntry == False:
    print('Invalid entry.  Please type "1" for yes or "2" for no.')
    #How to advance cursor to the end of the line when user enters retry input
    ExtraSunlight = str(input('Does the room have extra sunlight?  Please type "1" for YES or "2" for NO.'))
    BooleanValidEntry = ExtraSunlight == '1' or ExtraSunlight == '2'
#end valid entry loop
#is there a control to end a while loop

#If there is no extra sunlight
if ExtraSunlight == '2':
    print('A ' + format(BTU, ',.0f') + ' BTU capacity air conditioner is needed for this room.')
#There is extra sunlight
else:
    NeedBTU = BTU + (BTU * 0.20)
    print('A ' + format(NeedBTU, ',.0f') + ' BTU capacity air conditioner is needed for this room due to the extra sunlight. ')
