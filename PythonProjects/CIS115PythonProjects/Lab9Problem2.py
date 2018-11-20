__author__ = 'Michele Johnson'

# Write a program to calculate target heart rate during fitness training.
# This program has two functions: main and heart_rate_calculator.  Please do the following:

# (a)	In the main function, ask the user to enter age and resting heart rate.
# (b)	In the main function, call the heart_rate_calculator function.
# Pass the age and resting heart rate as arguments.
# (c)	In the heart_rate_calculator function,
# write code to calculate target heart rate during fitness training with the following formula:

#Target hart rate = (220 - age - resting heart rate) * 0.4 + resting heart rate

# Display target heart rate.

def HeartRate(Age, Resting):
    Rate = (220 - Age - Resting) * 0.4 + Resting
    print('Your heart rate is ' + (format(Rate, ',.2f')) + '.')

def main():
    global Age
    global Resting
    Age = float(input('Enter your age.'))
    Resting = float(input('Enter your resting heart rate reading.'))
    HeartRate(Age, Resting)

main()
