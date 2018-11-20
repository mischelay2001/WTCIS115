__author__ = 'Michele'
EmpMonSalary = float(input('Enter the employee\'s monthly salary:  '))
EmployeeCont = EmpMonSalary * 0.06
EmployerCont = EmpMonSalary * 0.03
ComCont = EmployeeCont + EmployerCont
print('The employee\'s monthly salary is $' + (format(EmpMonSalary, '.2f')) + '.')
print('The employee\'s monthly contribution at 6% is $' + (format(EmployeeCont, '.2f')) + '.')
print('The employer\'s monthly contribution at 3% is $' + (format(EmployerCont, '.2f')) + '.')
print('The combined monthly contribution from the employee and employer is $'+ (format(ComCont,'.2f')) + '.')