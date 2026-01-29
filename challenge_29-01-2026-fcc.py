"""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on 29th, January, 2026.

----------------------------
Letters-Numbers
Given a string containing only letters and numbers, 
return a new string where a hyphen (-) is inserted every time the string switches from a letter to a number, 
or a number to a letter.
----------------------------
Tests:
1. separate_letters_and_numbers("ABC123") should return "ABC-123".

2. separate_letters_and_numbers("Route66") should return "Route-66.

3. separate_letters_and_numbers("H3LL0W0RLD") should return "H-3-LL-0-W-0-RLD".

4. separate_letters_and_numbers("a1b2c3d4") should return "a-1-b-2-c-3-d-4".

"""


def separate_letters_and_numbers(s):

    new_string = ''
    elements_of_string = []
    processed_string = []
    
    for index, element in enumerate(s):
        try:
            number = int(element)    

            if type(elements_of_string[index - 1]) == type(number):
                elements_of_string.append(number)
            
            else:
                elements_of_string.append('-')
                elements_of_string.append(number)


        except ValueError:

            if len(elements_of_string) == 0:
                elements_of_string.append(element)

            elif type(elements_of_string[index - 1]) == type(element):
                elements_of_string.append(element)
            
            else:
                elements_of_string.append('-')
                elements_of_string.append(element)
    
    for item in elements_of_string:
        processed_string.append(str(item))

    new_string = ''.join(processed_string)
    print(new_string)


    return new_string


#Tests

separate_letters_and_numbers("ABC123")
separate_letters_and_numbers("Route66")
separate_letters_and_numbers("H3LL0W0RLD")
separate_letters_and_numbers("a1b2c3d4")