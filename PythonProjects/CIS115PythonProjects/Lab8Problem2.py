__author__ = 'Michele Johnson'

#A health insurance company wants a program to promote health and fitness.
# This program can do two things: calculate BMI (Body Mass Index)
# and determine whether a person has high blood pressure.

# To calculate BMI, the user must enter his height (in inches) and weight (in pounds).
# Us the following formula to calculate BMI:
#	BMI = (703 * weight) / (height*height)

#To determine whether a person has high blood pressure, the user must
# enter his systolic pressure and diastolic pressure.
# If the systolic pressure >= 140 or the diastolic pressure is >= 90, he has high blood pressure.

print('LEARN YOUR BODY MASS INDEX (BMI) AND/OR IF YOUR BLOOD PRESSURE (BP) IS IN NORMAL RANGE')
print()

def UserChoice():
    print('Enter 1 - Learn about your BMI')
    print('Enter 2 - Learn about your BP')
    print('Enter 3 - Learn about your BMI and BP')
    global Choice
    Choice = int(input('Enter your selection from the available options above to begin.'))

def BMI():
    global BMIHeight
    global BMIWeight
    BMIHeight = int(input('Enter your height in inches.'))
    BMIWeight = int(input('Enter your weight in pounds.'))
    BMIResult = (703*BMIWeight)/(BMIHeight*BMIHeight)
    print('Your BMI is ' + format(BMIResult, ',.2f') + "%.")
    print()

def BP():
    global Systolic
    global Diastolic
    Systolic = int(input('Enter your systolic (top number) from your blood pressure reading.'))
    Diastolic = int(input('Enter your diastolic (bottom number) from your blood pressure reading.'))
    if Systolic >= 140 or Diastolic >=90:
        print('Your BP readings indicate you have high blood pressure.  Consult your doctor.')
    else:
        print('Your BP readings indicate your blood pressure is within normal range.')
    print()

def main():
    UserChoice()
    if Choice == 1:
        BMI()
    elif Choice == 2:
        BP()
    elif Choice == 3:
        BMI()
        BP()
    else:
        print('You did not select a valid option.')

main()