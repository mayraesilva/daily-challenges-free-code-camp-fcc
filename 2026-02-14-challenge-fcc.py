"""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on 14th, February, 2026.

----------------------------
2026 Winter Games Day 9: Skeleton
Given a string representing the curves on a skeleton track, 
determine the difficulty of the track.

The given string will only consist of the letters:

"L" for a left turn
"R" for a right turn
"S" for a straight segment

Each direction change adds 15 points (an "L" followed by an "R" or vice versa).

All other curves add 5 points each (all other "L" or "R" characters).

Straight segments add 0 points.

The difficulty of the track is based on the total score. 

Return:

"Easy" if the total is 0 - 100
"Medium" if the total is 101-200
"Hard" if the total is over 200
----------------------------------
Tests:
1. get_difficulty("SLSLLSRRLSRLRL") should return "Easy".
2. get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS") should return "Hard".
3. get_difficulty("SRRRRLSLLRLRSSRLSRL") should return "Medium".
4. get_difficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL") should return "Hard".
5. get_difficulty("SLLSSLRLSLSLRSLSSLRL") should return "Medium".
6. get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR") should return "Easy".
"""



def get_difficulty(track):

    score = 0
    difficulty = None
    track_difficulty = {range(0,101) : "Easy", range(101,201): "Medium",range(201, 10000) : "Hard" }

    for index, path in enumerate(track):
        
        #To make sure we are not out of index
        if index + 1 < len(track):
            next_curve = track[ index + 1]
            
        else:
            next_curve = track[index]

        #If We have a straight path we skip it 
        if path == 'S':
            continue

        #Checking which score we are getting
        if path != next_curve:
            if next_curve == 'S':
                score += 5
            else:
                score += 15
        
        else:
            score += 5


    for scores in track_difficulty.keys():
        if score in scores:
            difficulty = track_difficulty[scores]
            print(difficulty)
            return difficulty
        


#Tests
get_difficulty("SLSLLSRRLSRLRL") 
get_difficulty("LLRSLRLRSLLRLRSLRRLRSRLLS")
get_difficulty("SRRRRLSLLRLRSSRLSRL")
get_difficulty("LSRLRLSRLRLSLRSLRLLRLSRLRLRSL")
get_difficulty("SLLSSLRLSLSLRSLSSLRL")
get_difficulty("SRSLSRSLSRRSLSRSRSLSRLSRSR")
