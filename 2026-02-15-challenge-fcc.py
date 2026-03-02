"""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on 15th, February, 2026.

----------------------------
2026 Winter Games Day 10: Alpine Skiing
Given a ski hill's vertical drop, 
horizontal distance, and type, 
determine the difficulty rating of the hill.

To determine the rating:

Calculate the steepness of the hill 
by taking the drop divided by the distance.

Then, calculate the adjusted steepness based on the hill type:
"Downhill" multiply steepness by 1.2
"Slalom": multiply steepness by 0.9
"Giant Slalom": multiply steepness by 1.0
Return:

"Green" if the adjusted steepness is less than or equal to 0.1
"Blue" if the adjusted steepness is greater 
than 0.1 and less than or equal to 0.25
"Black" if the adjusted steepness is greater than 0.25

----------------------------------
Tests

1. get_hill_rating(95, 900, "Slalom") should return "Green".
2. get_hill_rating(620, 2800, "Downhill") should return "Black".
3. get_hill_rating(420, 1680, "Giant Slalom") should return "Blue".
4. get_hill_rating(250, 3000, "Downhill") should return "Green".
5. get_hill_rating(110, 900, "Slalom") should return "Blue".
6. get_hill_rating(380, 1500, "Giant Slalom") should return "Black".
"""


def get_hill_rating(drop, distance, hill_type):

    steepness = drop / distance
    adjusted_steepness = 0

    if hill_type == 'Downhill':
        adjusted_steepness = steepness * 1.2
    
    elif hill_type == 'Slalom':
        adjusted_steepness = steepness * 0.9
    
    elif hill_type == "Giant Slalom": 
        adjusted_steepness = steepness

    if adjusted_steepness <= 0.1:
        print("Green")
        return "Green"
    
    if 0.1 < adjusted_steepness <= 0.25:
        print ('Blue')
        return "Blue"
    
    if adjusted_steepness > 0.25:
        print('Black')
        return "Black"



#Tests
get_hill_rating(95, 900, "Slalom")
get_hill_rating(620, 2800, "Downhill")
get_hill_rating(420, 1680, "Giant Slalom")
get_hill_rating(250, 3000, "Downhill")
get_hill_rating(110, 900, "Slalom")
get_hill_rating(380, 1500, "Giant Slalom")
