"""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on 3rd, February, 2026.

----------------------------
String Mirror

Given a string, return a new string that consists of the given string 
with a reversed copy of itself appended to the end of it.

---------------------------
Tests
1. mirror("freeCodeCamp") should return "freeCodeCamppmaCedoCeerf".
2. mirror("RaceCar") should return "RaceCarraCecaR".
3. mirror("helloworld") should return "helloworlddlrowolleh".
4. mirror("The quick brown fox...") should return "The quick brown fox......xof nworb kciuq ehT".
"""

def mirror(s):

    original_string = s
    mirror_string = original_string[::-1]
    
    # Slice notation takes the form [start:stop:step]. 
    # In this case, we omit the start and stop positions since we want the whole string. 
    # We also use step = -1, which means, "repeatedly step from right to left by 1 character".
    

    new_string = original_string + mirror_string
    print(new_string)
    print(mirror_string)

    return new_string


#Tests
mirror("freeCodeCamp")
mirror("RaceCar")
mirror("helloworld")
mirror("The quick brown fox...")