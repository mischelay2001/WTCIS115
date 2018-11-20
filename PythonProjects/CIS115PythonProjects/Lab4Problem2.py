__author__ = 'Michele'
Gallons = int(input('Enter number of gallons used by customer:  '))
if Gallons >= 8000:
    Difference = Gallons - 8000
    Tier1 = (Gallons - Difference) * 0.004
    Tier2 = Difference * 0.007
    Bill = Tier1 + Tier2
    print('The customer\'s water bill is $' + (format(Bill, ',.2f')) + '.')
else:
    Bill = Gallons * 0.004
    print('The customer\'s water bill is $' + (format(Bill, ',.2f')) + '.')