"""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on 2nd, February, 2026.

----------------------------
Groundhog Day
Today is Groundhog Day, in which a groundhog predicts the weather based on whether or not it sees its shadow.

Given a value representing the groundhog's appearance, return the correct prediction:

If the given value is the boolean true (the groundhog saw its shadow), return "Looks like we'll have six more weeks of winter.".
If the value is the boolean false (the groundhog did not see its shadow), return "It's going to be an early spring.".
If the value is anything else (the groundhog did not show up), return "No prediction this year.".
-----------------------------

Tests:
1. groundhog_day_prediction(True) should return "Looks like we'll have six more weeks of winter.".
2. groundhog_day_prediction(False) should return "It's going to be an early spring."
3. groundhog_day_prediction(None) should return "No prediction this year.".
4. groundhog_day_prediction(" ") should return "No prediction this year.".
5. groundhog_day_prediction("True") should return "No prediction this year.".

"""

def groundhog_day_prediction(appearance):

    if appearance == True:
        print("Looks like we'll have six more weeks of winter.")
        return "Looks like we'll have six more weeks of winter."
    
    elif appearance == False:
        print("It's going to be an early spring.")
        return "It's going to be an early spring."
    
    else:
        print("No prediction this year.")
        return "No prediction this year."

    

groundhog_day_prediction(True)
groundhog_day_prediction(False)
groundhog_day_prediction(None)
groundhog_day_prediction(" ")
groundhog_day_prediction("True")