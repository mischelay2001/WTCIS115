__author__ = 'Michele'
NumCups = int(input('Enter the number of cups of drink ordered:  '))
NumSlice = int(input('Enter the number of slices of ordered:  '))
SodaPrc = NumCups * 1.25
PizzaPrc = NumSlice * 3.50
TotAmt = SodaPrc + PizzaPrc
print('Drink total:  $' + (format(SodaPrc, ',.2f')))
print('Pizza slices total:  $' + (format(PizzaPrc, ',.2f')))
print('Order total:  $' + (format(TotAmt, ',.2f')))
