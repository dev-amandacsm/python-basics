_float = 5.48
_integer = 5
_string = "text"

print(_string)
print(_float + _integer)

_float = "5.48"
_integer = "5"

print(_float + _integer)

# False = zero (numeric values) or empty string (text values)
# True  = non-zero (numeric values) or not empty strings (text values)
print(f'{bool(0)}, {bool("")}')
''' prints False, False '''
print(f'{bool(-1)}, {bool(1)}, {bool(" ")}')
''' prints True, True, True '''

# None  = null value, it has its own data type called NoneType
_none = None
print(_none, bool(_none), type(_none))
'''prints None'''
