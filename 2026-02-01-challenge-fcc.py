"""
Hi! My name is Mayra Silva and I'm studying to become a data scientist.
Today I'll be solving the daily challenge available on 1st, February, 2026.

----------------------------
Digital Detox

Given an array of your login logs, 
determine whether you have met your digital detox goal.

Each log is a string in the format "YYYY-MM-DD HH:mm:ss".

You have met your digital detox goal if both of the following statements are true:

You logged in no more than once within any four-hour period.
You logged in no more than 2 times on any single day.

----------------------------

Tests:
1. digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"]) should return True.
2. digital_detox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"]) should return False.
3. digital_detox(["2026-01-31 08:21:30", "2026-01-31 14:30:00", "2026-02-01 08:00:00", "2026-02-01 12:30:00"]) should return True.
4. digital_detox(["2026-01-31 10:40:21", "2026-01-31 15:19:41", "2026-01-31 21:49:50", "2026-02-01 09:30:00"]) should return False.
5. digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]) should return True.
6. digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"]) should return False.

"""


from datetime import datetime, timedelta

def digital_detox(logs):

    time_log_format = "%Y-%m-%d %H:%M:%S" 
    logs_datetime = []
    status = None #The status can be true or false, based on the conditions
    how_many_logs_registered = len(logs)

    # Make sure we have the logs in ascending order
    logs.sort()
    
    # Step 1: Make sure the data type is ready

    for log_string in logs:
        log_datetime = datetime.strptime(log_string, time_log_format)
        logs_datetime.append(log_datetime)


    # Variables we need
    minimum_time_off = timedelta(hours=4) #minimum hours to be offline before checking socials a again
    logs_a_day = 1
    max_logs_a_day = 2 

    # Step 2: Check if in the same day we have more than one login  a day

    for index, log in enumerate(logs_datetime):

        todays_log = log

        # make sure we are comparing to the next log
        if index + 1 < how_many_logs_registered:
            next_log = logs_datetime[index + 1]

        else:
            break #This log is the last one
            

        # How many time between logs?
        hours_difference = next_log - todays_log
        #print(hours_difference)

        # Step 3: Check the intervals between logs

        if hours_difference < minimum_time_off: # !!!!!!!!!!!!!!!!!!!!!!!!!!
            print("You should give more space between logs")
            status = False
            return status 
            
        # SAME DAY
        if todays_log.day == next_log.day: # Is it the same day?
            logs_a_day += 1
            #print(logs_a_day)
          
            if todays_log == next_log: # we reached the last log
                break
                
            if logs_a_day > max_logs_a_day:
                print("You should reduce the logs per day")
                status = False
                return status
            
        else:
            logs_a_day = 0

    #  Step 4: If we've been through all of the logs and none conditions are met
    print('You are on the right track!')
    status = True
    return status
        

# Tests

digital_detox(["2026-02-01 08:00:00", "2026-02-01 12:30:00"])
digital_detox(["2026-02-01 04:00:00", "2026-02-01 07:30:00"])
digital_detox(["2026-01-31 08:21:30", "2026-01-31 14:30:00", "2026-02-01 08:00:00", "2026-02-01 12:30:00"])
digital_detox(["2026-01-31 10:40:21", "2026-01-31 15:19:41", "2026-01-31 21:49:50", "2026-02-01 09:30:00"])
digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 09:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"])
digital_detox(["2026-02-05 10:00:00", "2026-02-01 09:00:00", "2026-02-03 22:15:00", "2026-02-02 12:10:00", "2026-02-02 07:15:00", "2026-02-04 01:45:00", "2026-02-01 16:50:00", "2026-02-03 09:30:00"])