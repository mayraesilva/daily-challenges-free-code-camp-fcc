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
    to_process = list(arr)
    new_arr = []

    while to_process:
        current = to_process.pop(0)  # take from the front

        if isinstance(current, list):
            # replace the current list with its contents, preserving order
            to_process = current + to_process
        else:
            new_arr.append(current)
    print(new_arr)
    return new_arr

    
def flattenV2(arr):
    new_arr = []

    for current in arr:
        if isinstance(current, list):
            for x in flattenV2(current):
                new_arr.append(x)
        else:
            new_arr.append(current)

    return new_arr


def main():
    print(flattenV2([1, [2, 3], 4]))
    print(flattenV2([5, [4, [3, 2]], 1]))
    flattenV2(["A", [[[["B"]]]], "C"])
    flattenV2([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]])
    flattenV2([["red", ["blue", ["green", ["yellow", ["purple"]]]]], "orange", ["pink", ["brown"]]])

main()

"""
As in my firsts commits I had forgotten the method pop, so it was hard for me
"""