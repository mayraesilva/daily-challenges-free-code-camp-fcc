"""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on 19th, March, 2026.

----------------------------

nverted Matrix
Given a matrix (an array of arrays) filled with two distinct values, 
return a new matrix where all occurrences of one value are swapped with the other.

For example, given:

[
  ["a", "b"],
  ["a", "a"]
]

Return:

[
  ["b", "a"],
  ["b", "b"]
]

------------------------------
Tests:
1. invert_matrix([["a", "b"], ["a", "a"]]) 
should return [["b", "a"], ["b", "b"]].

2. invert_matrix([[1, 0, 1], [1, 1, 1], [0, 1, 0]])
should return [[0, 1, 0], [0, 0, 0], [1, 0, 1]].

3. invert_matrix([["apple", "banana", "banana", "apple"], ["banana", "apple", "apple", "banana"], ["banana", "banana", "banana", "apple"]])
should return [["banana", "apple", "apple", "banana"], ["apple", "banana", "banana", "apple"], ["apple", "apple", "apple", "banana"]].

4. invert_matrix([[6, 7, 7, 7, 6], [7, 6, 7, 6, 7], [7, 7, 6, 7, 7], [7, 6, 7, 6, 7], [6, 7, 7, 7, 6]])
should return [[7, 6, 6, 6, 7], [6, 7, 6, 7, 6], [6, 6, 7, 6, 6], [6, 7, 6, 7, 6], [7, 6, 6, 6, 7]].

5. invert_matrix([[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]])
should return [[2.1, 1.2, 1.2, 1.2], [1.2, 2.1, 1.2, 2.1], [2.1, 2.1, 1.2, 1.2]].

"""

def invert_matrix(matrix):

    first_value = ''
    second_value = ''
    values_obtained = False # We still don't have both values

    for line in matrix: 

        for element in line:
            if first_value == '': # Find the first value
                first_value = element
                print(first_value)
                continue

            if element == first_value: # Check if the next one is equal
                #print('teste')
                continue

            else:
                second_value = element # Get second value
                values_obtained = True
                print(second_value)
                break

        if values_obtained:
            break

    
    new_matrix = []

    for line in matrix:
        new_line = []
        for element in line:
            if element == first_value:
                new_line.append(second_value) # swap places
            else:
                new_line.append(first_value) # swap places

            new_matrix.append(new_line) # Add new line
    
    print(new_matrix)


    return new_matrix


#Tests
invert_matrix([["a", "b"], ["a", "a"]])
#invert_matrix([[1, 0, 1], [1, 1, 1], [0, 1, 0]])
#invert_matrix([["apple", "banana", "banana", "apple"], ["banana", "apple", "apple", "banana"], ["banana", "banana", "banana", "apple"]])
#invert_matrix([[6, 7, 7, 7, 6], [7, 6, 7, 6, 7], [7, 7, 6, 7, 7], [7, 6, 7, 6, 7], [6, 7, 7, 7, 6]])
#invert_matrix([[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]])