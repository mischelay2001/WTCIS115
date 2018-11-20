__author__ = 'Michele Johnson'

# Write a program to calculate tuition for students of a community college.
# In-state students pay $60 per credit hour, and will pay for only 12 credit hours even if they register for more hours.
# Out-of-state students pay $200 per credit hour, and will pay for 15 credit hours as the maximum.
# In the main function, ask the user whether he is in-state or out-of-state.
# Then ask the user how many credit hours he is taking.
# Pass number of credit hours to two functions.


def InstateTuition():
    if CreditHours < 12:
        Tuition = 60 * CreditHours
    else:
        Tuition = 60 * 12
    print('Your in-state tuition is $' + (format(Tuition, ',.2f')) + '.')


def OutOfStateTuition():
    if CreditHours < 15:
        Tuition = 200 * CreditHours
    else:
        Tuition = 200 * 15
    print('Your out-of-state tuition is $' + (format(Tuition, ',.2f')) + '.')

def main():
    global Instate
    global CreditHours
    global Tuition
    print('Enter 1 if you are in-state student.')
    print('Enter 2 if you are an out-of-state student.')
    Instate = int(input('Please enter 1 or 2 per the instructions above.'))
    print()
    if Instate == 1 or Instate == 2:
        CreditHours = float(input('Please the number of credit hours taken.'))
        print()
        if Instate == 1:
            InstateTuition()
        elif Instate == 2:
            OutOfStateTuition()
    else:
        print('You did not select a valid option.')

main()
