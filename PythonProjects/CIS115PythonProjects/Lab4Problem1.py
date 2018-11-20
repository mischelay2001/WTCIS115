__author__ = 'Michele'
Midterm = int(input('Enter student\'s midterm score:  '))
Final = int(input('Enter student\'s final exam score:  '))
Difference = Final - Midterm
BonusTotalScore = Midterm + Final + 5
if Difference < 20:
    TotalScore = Midterm + Final
    print('Your total score for the course is ', TotalScore, '.')
else:
#Question:  Why does the following statement fail?
#It seems to have something to do with BonusTotalScore as a integer.
# print('Great job!  You earned a 5 point bonus.  Your total score for the course is ' + BonusTotalScore + '.')
    print('Great job!  You earned a 5 point bonus.  Your total score for the course is ',  BonusTotalScore,  '.')