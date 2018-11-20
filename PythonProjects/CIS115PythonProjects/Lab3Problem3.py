__author__ = 'Michele'
OrgPrc = float(input('Enter the original price of the item on sale:  '))
PctDis = float(input('Enter the discount percentage for the item:  '))
PctDis100 = PctDis / 100
Disc = OrgPrc * PctDis100
SalePrc = OrgPrc - Disc
SalTxAmt = SalePrc * 0.07
TotAmt = SalePrc + SalTxAmt
print('The original price of your item was $' + (format(OrgPrc, ',.2f')) + '.')
print('With ' + (format(PctDis100, '.0%')) + ' off...')
print('The sale price is $' + (format(SalePrc, ',.2f')) + '.')
print('The sales tax is $' + (format(SalTxAmt, ',.2f')) + '.')
print('This brings your total order to $' + (format(TotAmt, ',.2f')) + '.')