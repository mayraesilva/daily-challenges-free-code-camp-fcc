"""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on 28th, January, 2026.

----------------------------
Flatten the Array
Given an array that contains nested arrays, return a new array with all values flattened into a single, one-dimensional array. 
Retain the original order of the items in the arrays.
----------------------------
Tests

1. flatten([1, [2, 3], 4]) should return [1, 2, 3, 4].

 flatten([5, [4, [3, 2]], 1]) should return [5, 4, 3, 2, 1].

 flatten(["A", [[[["B"]]]], "C"]) should return ["A", "B", "C"].

 flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]]) 
 should return ["L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"].

 flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]]) 
 should return ["red","blue","green","yellow","purple","orange","pink","brown"].

"""

def flatten(arr):
    original_arr = arr
    to_process = []
    new_arr = []
    
    for item in original_arr:
        
        if isinstance(item,list):
            for arr_item in item:
                index = 0
                while isinstance(arr_item[index], list):
                    

                    

                else:
                    new_arr.append(arr_item)
            
        else:
            new_arr.append(item)
    
    print(new_arr)
    return new_arr

    

flatten([1, [2, 3], 4])
flatten([5, [4, [3, 2]], 1])
flatten(["A", [[[["B"]]]], "C"])
flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]])
flatten([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]])