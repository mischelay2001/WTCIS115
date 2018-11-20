__author__ = 'Michele'

#Information to the user
print('This program calculates new salary for every employee after a 4% raise.')
print('After each employee, the user will be asked whether he wants to calculate')
print('the new salary for the next employee.')

# Do this until keep_going is "n"
KeepGoing = 'Y'
print(KeepGoing)
while KeepGoing == 'Y':
    Salary = float(input('Enter current salary: '))
    print(Salary)
    NewSalary = Salary * 1.04
    print(NewSalary)
    print('Your new salary is $', NewSalary)

