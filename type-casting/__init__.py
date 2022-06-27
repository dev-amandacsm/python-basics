# typecasting -> data type conversion

# string -> int
text = "2"
text_int = int(text)
print(f'Value: {text_int}\nType: {type(text_int)}')

# string -> float
number1 = 5.10
number2 = float("5.40")
print(number1 + number2)

# float -> int
number1 = 5.48766
print(f'Value: {int(number1)}\nType: {type(number1)}')

# int -> string
number1 = 4
number2 = 1
number1_text = str(number1)
number2_text = str(number2)
print(number1 + number2)
''' this command doesn't print 5, but 41, because they are string values '''
print(f'Type number1: {type(number1_text)}\nType number2: {number2_text}')

# float -> string
number1 = 4.587
print(type(str(number1)))
