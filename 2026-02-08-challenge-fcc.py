"""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on 8th, February, 2026.

----------------------------

2026 Winter Games Day 3: Biathlon
Given an array of integers, 
where each value represents the number of targets hit in a single round
 of a biathlon, return the total penalty distance the athlete must ski.

Each round consists of 5 targets.
Each missed target results in a 150 meter penalty loop
---------------------------
Tests:

1. calculate_penalty_distance([4, 4]) should return 300.
2. calculate_penalty_distance([5, 5]) should return 0.
3. calculate_penalty_distance([4, 5, 3, 5]) should return 450.
4. calculate_penalty_distance([5, 4, 5, 5]) should return 150.
5. calculate_penalty_distance([4, 3, 0, 3]) should return 1500.
"""

from functools import reduce

# [(caio, 10), (mayra,20)]
def calculate_penalty_distanceV2(rounds):

    #This version I'll be trying to solve it without for.

    # failed_rounds = filter(lambda x: x < 5, rounds)
    # rouns_penalty = map(lambda x: 150*(5-x), failed_rounds)
    # total_penalty = reduce(lambda x,y: x+y, rouns_penalty, 0)

    points = reduce(lambda x, y: x + y, rounds)
    rounds_played = len(rounds)
    max_points = rounds_played * 5
    targets_missed = max_points - points
    penalty = targets_missed * 150

    print(penalty)
    return penalty


calculate_penalty_distanceV2([4, 4])
calculate_penalty_distanceV2([5, 5])
calculate_penalty_distanceV2([4, 5, 3, 5])
calculate_penalty_distanceV2([5, 4, 5, 5])
calculate_penalty_distanceV2([4, 3, 0, 3])