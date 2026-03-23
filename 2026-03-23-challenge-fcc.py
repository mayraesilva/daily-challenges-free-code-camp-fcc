"""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on 23th, March, 2026.

----------------------------
No Consecutive Repeats

Given a string, determine if it has no repeating characters.

A string has no repeats if it does not have the same character two or more times in a row.

------------------------------
Tests:
1. has_no_repeats("hi world") should return True.
2. has_no_repeats("hello world") should return False.
3. has_no_repeats("abcdefghijklmnopqrstuvwxyz") should return True.
4. has_no_repeats("freeCodeCamp") should return False.
5. has_no_repeats("The quick brown fox jumped over the lazy dog.") should return True.
6. has_no_repeats("Mississippi") should return False.

"""

def has_no_repeats(string_to_be_analyzed):
    
    for index, char in enumerate(string_to_be_analyzed):

        string_size = len(string_to_be_analyzed)
        if index == string_size - 1:
            break

        if char == string_to_be_analized[index + 1]:
            print(" There is at least a repetition, so its False")
            return False
    
    
    print(" There is no repetition, so its True")   
    return True

    


has_no_repeats("hi world")
has_no_repeats("hello world")
has_no_repeats("abcdefghijklmnopqrstuvwxyz")
has_no_repeats("freeCodeCamp")
has_no_repeats("The quick brown fox jumped over the lazy dog.")
has_no_repeats("Mississippi")