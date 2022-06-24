# variable name conventions
''' lowercase with underscore '''
student_name = 'Mary'
student_email_address = 'mary@gmail.com'
student_age = 10

'''camelCase without underscore'''
studentName = 'John'
studentEmailAddress = 'john@gmail.com'
studentAge = 10

# notice that python is a case-sensitive language.

''' concatenating ways '''
print('%s, %s, %s' % (student_name, student_email_address, student_age))
print(studentName + ', ' + studentEmailAddress + ', ' + str(studentAge))
print('{}, {}, {}'.format(student_name, student_email_address, student_age))
print(f'{studentName}, {studentEmailAddress}, {studentAge}')

# backslash
text = 'Your path name is c:\\users\\Mary'
print(text)

text = r'Your path name is c:\users\Mary'
print(text)

# text = 'Your path name is c:\users\Mary'
''' print(text) -> produces an error because 
backslash is an escape character and expects 
another backslash or quotations marks '''

