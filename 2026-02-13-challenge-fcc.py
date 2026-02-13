"""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on 13th, February, 2026.

----------------------------

2026 Winter Games Day 8: Luge
Given an array of five numbers, 
each representing the time (in seconds) 
it took a luger to complete a segment of a track, 
determine which segment had the fastest speed and what that speed was.

The track is divided into the following segments:

Segment 1: 320 meters
Segment 2: 280 meters
Segment 3: 350 meters
Segment 4: 300 meters
Segment 5: 250 meters

The first value in the given array corresponds to the time for segment 1,
 the second value to segment 2, and so on.

To calculate the speed (in meters per second) for a segment,
divide the distance by the time.

Return "The luger's fastest speed was X m/s on segment Y.". 
Where X is the fastest speed, rounded to two decimal places,
and Y is the segment number where the fastest speed occurred.

 -------------------------
Tests
1. get_fastest_speed([9.523, 8.234, 10.012, 9.001, 7.128]) 
should return "The luger's fastest speed was 35.07 m/s on segment 5."

2. get_fastest_speed([9.381, 7.417, 9.912, 8.815, 7.284])
 should return "The luger's fastest speed was 37.75 m/s on segment 2."

3. get_fastest_speed([8.890, 7.601, 9.093, 8.392, 6.912])
 should return "The luger's fastest speed was 38.49 m/s on segment 3."

4. get_fastest_speed([8.490, 7.732, 10.103, 8.489, 6.840])
 should return "The luger's fastest speed was 37.69 m/s on segment 1."

5. get_fastest_speed([8.204, 7.230, 9.673, 7.645, 6.508])
 should return "The luger's fastest speed was 39.24 m/s on segment 4."
"""


def get_fastest_speed(times):
    segments = {"segment 1": 320,
                "segment 2": 280,
                "segment 3": 350,
                "segment 4": 300,
                "segment 5": 250}
    
    segment_speed = []

    for index, (key, value) in enumerate(segments.items()):
        speed = value / times[index]
        segment_speed.append(speed)
    
    fastest_speed = max(segment_speed)
    fastest_segment = segment_speed.index(fastest_speed) + 1
    fastest_string = f"The luger's fastest speed was {fastest_speed:.2f} m/s on segment {fastest_segment}."
    print(fastest_string)

    return fastest_string
    


#Tests
get_fastest_speed([9.523, 8.234, 10.012, 9.001, 7.128])
# get_fastest_speed([9.381, 7.417, 9.912, 8.815, 7.284])
# get_fastest_speed([8.890, 7.601, 9.093, 8.392, 6.912])
# get_fastest_speed([8.490, 7.732, 10.103, 8.489, 6.840])
# get_fastest_speed([8.204, 7.230, 9.673, 7.645, 6.508])


