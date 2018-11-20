__author__ = 'Michele Johnson'
# Write a program to strip all occurrences of these characters: '(', ')' and '-'.
# Also, strip all the leading and trailing whitespace characters.
# Display the stripped phone number.

phone = input('Enter a phone number: ')
phone = phone.replace(' ','')
phone = phone.replace('.','')
phone = phone.replace('-','')
phone = phone.replace('(','')
phone = phone.replace(')','')
phone = phone.lstrip()
phone = phone.rstrip()
print(phone)
print()