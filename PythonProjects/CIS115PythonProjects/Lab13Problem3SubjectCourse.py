__author__ = 'Michele Johnson'
# Write a program to do the following: 

# (a)	Ask the user to enter a course code.
# (b)	Strip all the leading and trailing whitespace characters from the code.  
# Display the stripped code.
# (c)	Test whether the course code is valid.  
# If the course code does not follow the rules described above, display an error message.  
# Otherwise, separate subject from course number and display them separately.

print()
print()
print("This program display the course subject code and the course number code.")
print("Please note:  ")
print("              Course codes must be a six character alphanumeric.")
print("              Subject codes should be the first three characters of the course code and alpha characters.")
print("              Course number should be the last three characters of the course code and numeric characters.")
print()
userCode = input("Please enter a course code:  ")
userCode = userCode.lstrip()
userCode = userCode.rstrip()
print()
if userCode.isalnum() != True:
    print("1The input is invalid.  Course codes must be a six character alphanumeric.")
    print()
lenUserCode = len(userCode)
if lenUserCode != 6:
    print("The input is invalid.  Course codes must be a six character alphanumeric.")
    print()
subjectCode = userCode[:3].upper()
if subjectCode.isalpha() != True:
    print("The input is invalid.  Subject codes are three alpha characters.")
    print()
courseCode = userCode[3:]
if courseCode.isdigit() != True:
    print("The input is invalid.  Course number are three numeric characters.")
    print()
if subjectCode.isalpha() == True and courseCode.isdigit() == True:
    print(subjectCode, courseCode)
