text = 'Hello world'

print('What do you want to test?\n1 - Slicing texts\n2 - lower() and upper() methods\n'
      '3 - len() and count() methods\n4 - Verifications\nInsert your choice here: ', end='')
choice = int(input())

if choice == 1:
    # slicing texts
    print(text[0])
    ''' prints H '''

    print(text[-1])
    ''' prints d '''

    print(text[-11:-6])
    ''' prints Hello -> starting index is inclusive while ending index is exclusive '''

    print(text[6:11])
    ''' prints world -> starting index is inclusive while ending index is exclusive '''

    print(text[-9:-2])
    ''' prints llo wor -> starting index is inclusive while ending index is exclusive '''

    print(text[2:9])
    ''' prints llo wor -> starting index is inclusive while ending index is exclusive '''

    print(text[-5:])
    ''' prints world '''

    print(text[:5])
    ''' prints Hello '''

    print(text[:5], text[-5:])
    ''' prints Hello world '''

if choice == 2:
    # upper() and lower() methods
    print(text.upper())
    ''' prints HELLO WORLD '''

    print(text.lower())
    ''' prints hello world '''

if choice == 3:
    # count, len and replace methods

    print(text.count('l'))
    ''' prints the number of characters equal to the character provided '''

    print(len(f'{text}{"     "}'))
    ''' prints the amount of characters in the variable '''

    print(len(f'{text}{"     "}'.strip()))
    ''' prints the amount of characters in the text variable excluding whitespaces '''

    print(text.replace('world', 'friend'))
    ''' prints Hello friend '''

if choice == 4:
    # verifications
    print(text.islower())
    ''' prints False because not all characters are in lowercase '''

    print(text.isupper())
    ''' prints False because not all characters are in uppercase '''

    print(text.isalpha())
    ''' prints True because all characters are alphabetic '''

    print(text.isalnum())
    ''' prints True because all characters are alphanumeric '''

    print(text.isdigit())
    ''' prints False because none of the characters is a digit '''

    print(text.isnumeric())
    ''' prints False because none of the characters is a number '''

