__author__ = 'Michele'
NumEmpPartA = int(input('Enter the number of employees taking part A of the course:  '))
NumEmpPartB = int(input('Enter the number of employees taking part B of the course:  '))
NumEmpPartAB = int(input('Enter the number of employees taking both parts A and B of the course:  '))
PartAExps = NumEmpPartA * 100
PartBExps = NumEmpPartB * 150
PartABChrg = 100 + 150
DscPartABChrg = PartABChrg * ((100 - 20)/100)
PartABExps = NumEmpPartAB * DscPartABChrg
TotExpAmt = PartAExps + PartBExps + PartABExps
print('The cost for', NumEmpPartA, 'employees taking only part A:  $' + (format(PartAExps, ',.2f')))
print('The cost for', NumEmpPartB, 'employees taking only part A:  $' + (format(PartBExps, ',.2f')))
print('The cost for', NumEmpPartAB, 'employees taking both parts A and B:  $' + (format(PartABExps, ',.2f')))
print('The total training expense for the company:  $', (format(TotExpAmt, ',.2f')))