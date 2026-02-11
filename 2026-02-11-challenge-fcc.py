"""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on 11th, February, 2026.

----------------------------
2026 Winter Games Day 6: Figure Skating
Given an array of judge scores and optional penalties, 
calculate the final score for a figure skating routine.

The first argument is an array of 10 judge scores, 
each a number from 0 to 10. 
Remove the highest and lowest judge scores 
and sum the remaining 8 scores to get the base score.

Any additional arguments passed to the function are penalties. 
Subtract all penalties from the base score to get the final score.

--------------------------
Tests

1. compute_score([10, 8, 9, 6, 9, 8, 8, 9, 7, 7], 1) should return 64.
2. compute_score([10, 10, 10, 10, 10, 10, 10, 10, 10, 10]) should return 80.
3. compute_score([10, 8, 9, 10, 9, 8, 8, 9, 10, 7], 1, 2, 1) should return 67.
4. compute_score([8.0, 8.5, 9.0, 8.5, 9.0, 8.0, 9.0, 8.5, 9.0, 8.5], 0.5, 1.0) should return 67.5.
5. compute_score([6.0, 8.5, 7.0, 9.0, 7.5, 8.0, 6.5, 9.5, 7.0, 8.0], 1.5, 0.5, 0.5) should return 59.
"""

def compute_score(judge_scores, *penalties):
    final_score = 0
    no_penalty_score = 0
    penalties = 0

    # Get the values to be desconsidered
    highest_desconsidered = max(judge_scores)
    lowest_desconsidered = min(judge_scores)


    # Remove the values to be desconsidered from list
    judge_scores.remove(highest_desconsidered)
    judge_scores.remove(lowest_desconsidered)

    no_penalty_score = sum(judge_scores) # we have not applied the penalties
    
    


    return final_score



# Tests
compute_score([10, 8, 9, 6, 9, 8, 8, 9, 7, 7], 1)