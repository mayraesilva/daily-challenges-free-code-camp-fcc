"""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on 4th, February, 2026.

----------------------------
Truncate the Text

If it's longer than 20 characters, truncate it to the first 17 characters 
and append "..." to the end of it (so it's 20 characters total) and return the result.
----------------------------
Tests
1. truncate_text("Hello, world!") should return "Hello, world!".
2. truncate_text("This string should get truncated.") should return "This string shoul...".
3. truncate_text("Exactly twenty chars") should return "Exactly twenty chars".
4. truncate_text(".....................") should return "....................".
"""

def truncate_text(text):

    return text





#Tests
truncate_text("Hello, world!")
truncate_text("This string should get truncated.")
truncate_text("Exactly twenty chars")
truncate_text(".....................")