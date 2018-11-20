__author__ = 'Michele'

# An instructor teaches two classes this semester.
# Recently he gave the same test to both classes.
# Write a program to analyze the test scores.

# (a)	Enter the scores of students in class 1.
# Every time after a score is entered, ask whether the user wants to enter another course.
# Store the scores in a list.
# (b)	Enter the scores of students in class 2.
# Every time after a score is entered, ask whether the user wants to enter another course.
# Store the scores in a list.
# (c)	Display the number of scores in class 1 and all the scores in class 1.
# (d)	Display the number of scores in class 2 and all the scores in class 2.
# (e)	Combine the two score lists.  Display the combined list.
# (f)	Display the highest score in the combined list.
# (g)	Display the lowest score in the combined list.
# (h)	Sort the scores in the combined list in ascending order (i.e. from smallest to largest).
# Display the sorted list.
# (i)	Sort the scores in the combined list in descending order (i.e. from largest to smallest).
# Display the sorted list.

global scoresClass1
global scoresClass2

# User wants to enter new score; newScore = 1
newScore = 'N'
scoresClass1 = []
scoresClass2 = []

def getClass1Score():
    #Initiate
    score = input("Enter the student's test score:  ")
    scoresClass1.append(score)
    print()
    print("Would you like to enter another score?  ")
    newScore = input("Enter 'Y' for Yes or 'N' for No  ")
    newScore = newScore.upper()
    print()

    while newScore == 'Y':
        score = input("Enter the student's test score:  ")
        scoresClass1.append(score)
        print()
        print("Would you like to enter another score?  ")
        newScore = input("Enter 'Y' for Yes or 'N' for No  ")
        newScore = newScore.upper()
        print()

def getClass2Score():
    #Initiate
    score = input("Enter the student's test score:  ")
    scoresClass2.append(score)
    print()
    print("Would you like to enter another score?  ")
    newScore = input("Enter 'Y' for Yes or 'N' for No  ")
    newScore = newScore.upper()
    print()

    while newScore == 'Y':
        score = input("Enter the student's test score:  ")
        scoresClass2.append(score)
        print()
        print("Would you like to enter another score?  ")
        newScore = input("Enter 'Y' for Yes or 'N' for No  ")
        newScore = newScore.upper()
        print()

def main():
    getClass1Score()
    getClass2Score()
    print("There were", len(scoresClass1), "scores in the first class:")
    print("The first class scores were:", scoresClass1)
    print()
    print("There were", len(scoresClass2), "scores in the first class:")
    print("The first class scores were:", scoresClass2)
    print()
    combinedClassScores = scoresClass1 + scoresClass2
    print("The combined scores from both classes were:", combinedClassScores)
    print()
    combinedClassScores.sort()
    highest = combinedClassScores[0]
    print("The highest score amongst both classes was", highest)
    print()
    combinedClassScores.reverse()
    lowest = combinedClassScores[0]
    print("The highest score amongst both classes was", lowest)
    print()
    combinedClassScores.sort()
    print("The scores from least to greatest are as follows:", combinedClassScores)
    print()
    combinedClassScores.reverse()
    print("The scores from greatest to least are as follows:", combinedClassScores)
    print()

main()


