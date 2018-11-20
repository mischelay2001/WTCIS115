__author__ = 'Michele'
print('It is time to select your health plan for the year.')
print('You will need to select from the table below:')
print('')
print('Health Plan Code         Coverage                    Premium')
print('E                        Employee Only               $40')
print('S                        Employee & Spouse           $160')
print('C                        Employee & Children         $200')
print('F                        Whole Family                $250')
print('')

#User entry; 1st pass
Choice = str(input('Please enter your health plan choice code from the table above:  '))
Choice = Choice.upper()
UserEntryValid = Choice == 'E' or Choice == 'S' or Choice == 'C' or Choice == 'F'

#Test valid user entry
while UserEntryValid == False:
    print('Your entry is invalid.  Please select a valid code from the table above.')
    Choice = str(input('Please enter your health plan choice code from the table above:  '))
    Choice = Choice.upper()
    UserEntryValid = Choice == 'E' or Choice == 'S' or Choice == 'C' or Choice == 'F'
    #print(Choice)
    #print(UserEntryValid)

#Begin program
if Choice == 'E':
    print('You have selected the Employee Only health plan.  Your premium is $40.')
elif Choice == 'S':
    print('You have selected the Employee & Spouse health plan.  Your premium is $160.')
elif Choice == 'C':
    print('You have selected the Employee & Children health plan.  Your premium is $200.')
else:
    print('You have selected the Whole Family health plan.  Your premium is $250.')
