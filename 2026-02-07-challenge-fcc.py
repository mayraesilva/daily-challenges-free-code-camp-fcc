"""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on 7th, February, 2026.

----------------------------
2026 Winter Games Day 2: Snowboarding
Given a snowboarder's starting stance and a rotation in degrees, 
determine their landing stance.

- A snowboarder's stance is either "Regular" or "Goofy".
- Trick rotations are multiples of 90 degrees. 
- Positive indicates clockwise rotation, 
and negative indicate counter-clockwise rotation.
- The landing stance flips every 180 degrees of rotation.

For example, given "Regular" and 90, return "Regular". 
Given "Regular" and 180 degrees, return "Goofy".
-----------------------------
1. get_landing_stance("Regular", 90) should return "Regular".
2. get_landing_stance("Regular", 180) should return "Goofy".
3. get_landing_stance("Goofy", -270) should return "Regular".
4. get_landing_stance("Regular", 2340) should return "Goofy".
5. get_landing_stance("Goofy", 2160) should return "Goofy".
6. get_landing_stance("Goofy", -540) should return "Regular".

"""

def get_landing_stance(start_stance, rotation):

    landing_stance = ''
    how_many_rot = abs(rotation / 90) #get the absolute value

    if (how_many_rot % 2) == 0:
        landing_stance = 'Goofy'
        print(landing_stance)
        return landing_stance
    else:
        landing_stance = 'Regular'
        print(landing_stance)
        return landing_stance



#Tests
get_landing_stance("Regular", 90)
get_landing_stance("Regular", 180) 
get_landing_stance("Goofy", -270)
get_landing_stance("Regular", 2340)
get_landing_stance("Goofy", 2160)
get_landing_stance("Goofy", -540)