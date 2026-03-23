""""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on 19th, February, 2026.

----------------------------
2026 Winter Games Day 14: Ski Mountaineering

Given the snow depth and slope of a mountain, 
determine if there's an avalanche risk.

The snow depth values are "Shallow", "Moderate", or "Deep".
Slope values are "Gentle", "Steep", or "Very Steep".
Return "Safe" or "Risky" based on this table:

                "Shallow"	"Moderate"	"Deep"
"Gentle"	    "Safe"	    "Safe"	    "Safe"
"Steep"	        "Safe"	    "Risky"	    "Risky"
"Very Steep"	"Safe"	    "Risky"	    "Risky"
----------------------------
Tests
1. avalanche_risk("Shallow", "Gentle") should return "Safe".
2. avalanche_risk("Shallow", "Steep") should return "Safe".
3. avalanche_risk("Shallow", "Very Steep") should return "Safe".
4. avalanche_risk("Moderate", "Gentle") should return "Safe".
5. avalanche_risk("Moderate", "Steep") should return "Risky".
6. avalanche_risk("Moderate", "Very Steep") should return "Risky".
7. avalanche_risk("Deep", "Gentle") should return "Safe".
8. avalanche_risk("Deep", "Steep") should return "Risky".
9. avalanche_risk("Deep", "Very Steep") should return "Risky".
"""
def avalanche_risk(snow_depth, slope):
    SAFE = "Safe"
    RISKY = "Risky"

    if snow_depth == 'Shallow':
        avalanche_risk = SAFE
        return avalanche_risk

    

    return ''

#Tests
avalanche_risk("Shallow", "Gentle")
avalanche_risk("Shallow", "Steep")
avalanche_risk("Shallow", "Very Steep")
avalanche_risk("Moderate", "Gentle")
avalanche_risk("Moderate", "Steep")
avalanche_risk("Moderate", "Very Steep")
avalanche_risk("Deep", "Gentle")
avalanche_risk("Deep", "Steep")
avalanche_risk("Deep", "Very Steep")
