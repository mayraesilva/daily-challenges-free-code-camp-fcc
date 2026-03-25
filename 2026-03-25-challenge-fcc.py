"""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on 25th, March, 2026.

----------------------------
Cooldown Time

Given two timestamps, the first representing when a user finished an exam, 
and the second representing the current time, 
determine whether the user can take an exam again.

Both timestamps will be given the format:
 "YYYY-MM-DDTHH:MM:SS", for example "2026-03-25T14:00:00".
   Note that the time is 24-hour clock.
A user must wait at least 48 hours before retaking an exam.
----------------------------

Tests:

1. can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00") should return True.
2. can_retake("2026-03-24T14:00:00", "2026-03-25T10:00:00") should return False.
3. can_retake("2026-03-23T09:25:00", "2026-03-25T09:25:00") should return True.
4. can_retake("2026-03-25T11:50:00", "2026-03-23T11:49:59") should return False.
"""

from datetime import datetime

def can_retake(finish_time, current_time):

    minimum_hours_format = '%H'
    time_format = "%Y-%m-%dT%H:%M:%S"

    minimum_hours = "48" # minimum hours before retaking and exam.
    datetime_minimum_hours = datetime.strptime(minimum_hours, minimum_hours_format)
    datetime_finish_time = datetime.strptime(finish_time, time_format)
    datetime_current_time = datetime.strftime(current_time, time_format)

    time_difference = datetime_current_time - datetime_finish_time

    if time_difference >= datetime_minimum_hours:
        print(" You can retake the exam!")
        return True
    else:
        print(f"You have to wait at least {minimum_hours} hours to retake the exam.")
        return False




#Tests
can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00")
can_retake("2026-03-24T14:00:00", "2026-03-25T10:00:00")
can_retake("2026-03-23T09:25:00", "2026-03-25T09:25:00")
can_retake("2026-03-25T11:50:00", "2026-03-23T11:49:59")