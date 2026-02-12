"""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on 12th, February, 2026.

----------------------------
2026 Winter Games Day 7: Speed Skating
Given two arrays representing the lap times (in seconds) 
for two speed skaters, return the lap number 
where the difference in lap times is the largest.

The first element of each array corresponds to lap 1, 
the second to lap 2, and so on.

-----------------------------
Tests

1. largest_difference([26.11, 25.80, 25.92, 26.23, 26.07], [25.93, 25.74, 26.53, 26.11, 26.30]) should return 3.
2. largest_difference([27.04, 25.94, 26.22, 26.07, 26.18], [25.59, 25.80, 26.11, 26.01, 26.23]) should return 1.
3. largest_difference([25.82, 25.90, 26.05, 26.00, 26.48], [25.85, 25.92, 26.07, 25.98, 25.95]) should return 5.
4. largest_difference([25.88, 26.10, 25.95, 26.05, 26.00], [25.90, 26.55, 25.92, 26.03, 26.01]) should return 2.
5. largest_difference([25.92, 26.01, 26.05, 25.88, 26.12], [25.95, 26.00, 26.03, 26.45, 26.10]) should return 4.
"""


def largest_difference(skater1, skater2):
    largest_gap = 0
    differences = []
    biggest_was_in = 0

    for index, lap in enumerate(skater1):
        difference = abs(skater1[index] - skater2[index])
        differences.append(difference)                 

    largest_gap = max(differences)
    biggest_was_in = differences.index(largest_gap)

    return biggest_was_in



#tests

largest_difference([26.11, 25.80, 25.92, 26.23, 26.07], [25.93, 25.74, 26.53, 26.11, 26.30])
largest_difference([27.04, 25.94, 26.22, 26.07, 26.18], [25.59, 25.80, 26.11, 26.01, 26.23])
largest_difference([25.82, 25.90, 26.05, 26.00, 26.48], [25.85, 25.92, 26.07, 25.98, 25.95])
largest_difference([25.88, 26.10, 25.95, 26.05, 26.00], [25.90, 26.55, 25.92, 26.03, 26.01])
largest_difference([25.92, 26.01, 26.05, 25.88, 26.12], [25.95, 26.00, 26.03, 26.45, 26.10])
