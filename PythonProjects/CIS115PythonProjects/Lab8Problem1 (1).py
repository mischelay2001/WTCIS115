__author__ = 'Michele'

#An instructor wants to create a short computer quiz for his students.
#There are only two questions in the quiz.
#Write a program to implement this quiz.

def Question1():
    print('The physical devices that a computer is made of are referred to as ______')
    print('a. hardware')
    print('b. software')
    print('c. the operation system')
    print('d. tools')
    global Answer1
    Answer1 = str(input('Enter your answer:'))
    print()

def Question2():
    print('The part of a computer that runs programs is called ______')
    print('a. RAM')
    print('b. secondary storage')
    print('c. main memory')
    print('d. the CPU')
    global Answer2
    Answer2 = str(input('Enter your answer:'))
    print()

def main():
    Question1()
    Question2()

main()