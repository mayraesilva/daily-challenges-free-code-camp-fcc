""""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on, February, 20th, 2026.

----------------------------
2026 Winter Games Day 15: Freestyle Skiing

Given a trick name consisting of two words, 
determine if it is a valid freestyle skiing trick name.

A trick is valid if the first word is in the list of valid first words,
and the second word is in the list of valid second words.

The two words will be separated by a single space.


Valid first words:

"Misty"
"Ghost"
"Thunder"
"Solar"
"Sky"
"Phantom"
"Frozen"
"Polar"


Valid second words:

"Twister"
"Icequake"
"Avalanche"
"Vortex"
"Snowstorm"
"Frostbite"
"Blizzard"
"Shadow"
-----------------------------------
Tests:
1. is_valid_trick("Polar Vortex") should return True.
2. is_valid_trick("Solar Icequake") should return True.
3. is_valid_trick("Thunder Blizzard") should return True.
4. is_valid_trick("Phantom Frostbite") should return True.
5. is_valid_trick("Ghost Avalanche") should return True.
6. is_valid_trick("Snowstorm Shadow") should return False.
7. is_valid_trick("Solar Sky") should return False.
"""

def is_valid_trick(trick_name):

    first_words = ["Misty", "Ghost", "Thunder", "Solar", "Sky", 
                   "Phantom", "Frozen", "Polar"]
    
    second_words = ["Twister", "Icequake", "Avalanche", "Vortex", 
                    "Snowstorm", "Frostbite", "Blizzard", "Shadow"]
    

    return trick_name

#Tests
is_valid_trick("Polar Vortex")
is_valid_trick("Solar Icequake")
is_valid_trick("Thunder Blizzard")
is_valid_trick("Phantom Frostbite")
is_valid_trick("Ghost Avalanche")
is_valid_trick("Snowstorm Shadow")
is_valid_trick("Solar Sky")