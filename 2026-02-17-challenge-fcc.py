"""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on 17th, February, 2026.

----------------------------
2026 Winter Games Day 12: Bobsled

Given an array representing the weights of the athletes on a bobsled team 
and a number representing the weight of the bobsled, 
determine whether the team is eligible to race.

The length of the array determines the team size: 1, 2 or 4 person teams.
All given weight values are in kilograms (kg).
The bobsled (sled by itself) must have a minimum weight of:

162 kg for a 1-person team
170 kg for a 2-person team
210 kg for a 4-person team
The total weight of the bobsled 
(athletes plus sled) must not exceed:

- 247 kg for a 1-person team
- 390 kg for a 2-person team
- 630 kg for a 4-person team

Return "Eligible" if the team meets all the requirements, 
or "Not Eligible" if the team fails to meet one or more of the requirements.

--------------------------
Tests

1. check_eligibility([78], 165) should return "Eligible".
2. check_eligibility([80], 160) should return "Not Eligible".
3. check_eligibility([80], 170) should return "Not Eligible".
4. check_eligibility([85, 90], 170) should return "Eligible".
5. check_eligibility([85, 95], 168) should return "Not Eligible".
6. check_eligibility([112, 97], 185) should return "Not Eligible".
7. check_eligibility([110, 102, 90, 106], 222) should return "Eligible".
8. check_eligibility([106, 99, 90, 88], 205) should return "Not Eligible".
9. check_eligibility([106, 99, 103, 96], 227) should return "Not Eligible".


"""


def check_eligibility(athlete_weights, sled_weight):

    #All weights are in kilograms

    minimum_sled_weight_1_person_team = 162
    minimum_sled_weight_2_people_team = 170
    minimum_sled_weight_4_people_team = 210

    # Maximum weight of bobsled (person + sled)
    maximum_bobsled_1_person_team = 247
    maximum_bobsled_2_people_team = 390
    maximum_bobsled_4_people_team = 630

    team_size = len(athlete_weights)

    if team_size == 1:
        if sled_weight < minimum_sled_weight_1_person_team:
            return "Not Eligible"
  
    if team_size == 2:
        if sled_weight < minimum_sled_weight_2_people_team:
            return "Not Eligible"
        
    if team_size == 4:
        if sled_weight < minimum_sled_weight_4_people_team:
            return "Not Eligible"
    
    return athlete_weights

# Tests
check_eligibility([78], 165)
#check_eligibility([80], 160)
#check_eligibility([80], 170)
#check_eligibility([85, 90], 170)
#check_eligibility([85, 95], 168)
#check_eligibility([110, 102, 90, 106], 222)
#check_eligibility([106, 99, 90, 88], 205)
#check_eligibility([106, 99, 103, 96], 227)