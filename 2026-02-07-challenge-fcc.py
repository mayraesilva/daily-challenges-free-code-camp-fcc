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

------------------------------

In this branch, I'll be trying to solve the same challenge,
but, without using if conditions.

"""
import math


def get_landing_stance(start_stance, rotation):

    landing_stance = ''
    possible_stances = ['Regular', 'Goofy']
    stances = []


    stances.append(start_stance)
    change_stance = abs(int(rotation / 180))

    for stance in range(change_stance):

        for possibility in possible_stances:

            if possibility != stances[-1]:
                stances.append(possibility)
            
            else:
                continue
    
    landing_stance = stances[-1]
    #print(stances)
    print(landing_stance)
    return landing_stance
            


# 'Regular', 'Goofy', Regular', 'Goofy', Regular', 'Goofy', Regular', 'Goofy', Regular', 'Goofy',
def get_landing_stance_v2(start_stance, rotation):
    stances = ['Regular', 'Goofy'] # 0, 1        
    stance_changes = abs(rotation) // 180
    start_stance_index = stances.index(start_stance)

    # 0 % 2 = 0
    # 1 % 2 = 1
    final_index = (stance_changes + start_stance_index)  % 2 

    result = stances[final_index]
    print(result)

    return result



#Tests
get_landing_stance_v2("Regular", 90)
get_landing_stance_v2("Regular", 180) 
get_landing_stance_v2("Goofy", -270)
get_landing_stance_v2("Regular", 2340)
get_landing_stance_v2("Goofy", 2160)
get_landing_stance_v2("Goofy", -540)