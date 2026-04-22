""""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on 22nd, April, 2026.

----------------------------
Earth Day Cleanup Crew

Today is Earth Day. 
Given an array of items you cleaned up, 
return your total cleanup score based on the rules below.

Given items will be one of:

Item	Base Value
"bottle"	10
"can"	    6
"bag"	    8
"tire"	    35
"straw"	    4
"cardboard"	3
"newspaper"	3
"shoe"	    12
"electronics"	25
"battery"	18
"mattress"	38

A Rare item is represented as ["rare", value]. 
For example, ["rare", 80]. 
Rare items do not get a streak bonus.

Streak bonus: If the same item appears consecutively, 
it gets increasing bonus points.

First consecutive occurrence: base value
Second: base value + 1
Third: base value + 2
etc.

Fifth Item Multiplier: Every fifth item collected gets a multiplier.

Fifth item: *2
Tenth item: *3
etc.
Apply the multiplier after calculating any bonuses.
-------------------------------------
1. get_cleanup_score(["bottle", "straw", "shoe", "battery"])
should return 44.

2. get_cleanup_score(["electronics", "straw", "newspaper", "bottle", "bag"]) 
should return 58.

3. get_cleanup_score(["shoe", "can", "can", "can", "bottle", "bottle", "straw", "straw", "straw"])
should return 79.

4. get_cleanup_score(["mattress", ["rare", 80], "tire", "tire", "tire", ["rare", 95]])
should return 358.

5. get_cleanup_score(["bottle", "can", "can", "shoe", "shoe", ["rare", 56], "bottle", "bottle", "can", "can", "electronics", "bottle", ["rare", 48], "bottle", "can", "can", "can", "can", "can", "can", "can"])
should return 383.
"""

def get_cleanup_score(items):

    return items


# Tests
get_cleanup_score(["bottle", "straw", "shoe", "battery"])
get_cleanup_score(["electronics", "straw", "newspaper", "bottle", "bag"]) 
get_cleanup_score(["shoe", "can", "can", "can", "bottle", "bottle", "straw", "straw", "straw"])
get_cleanup_score(["mattress", ["rare", 80], "tire", "tire", "tire", ["rare", 95]])
get_cleanup_score(["bottle", "can", "can", "shoe", "shoe", ["rare", 56], "bottle", "bottle", "can", "can", "electronics", "bottle", ["rare", 48], "bottle", "can", "can", "can", "can", "can", "can", "can"])
