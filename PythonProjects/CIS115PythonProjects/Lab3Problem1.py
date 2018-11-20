__author__ = 'Michele'
length = int(input('Enter length of tank in inches: '))
width = int(input('Enter length of tank in inches: '))
height = int(input('Enter length of tank in inches: '))
volume = length * width * height
cubicVolume = volume // 100
print('The volume of Mary\'s tank is', volume, 'cubic inches, so she would need to add', cubicVolume, 'teaspoons of conditioner to her tank.')