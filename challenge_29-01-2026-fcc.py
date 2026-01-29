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

    return s