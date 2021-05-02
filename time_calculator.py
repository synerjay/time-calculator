# DO NOT IMPORT ANY PYTHON LIBRARIES... ARGH

# print(add_time("11:06 PM", "2:02")) Output hould be 1:07 AM

def add_time(start, duration, day_of_week=False):
    days_of_the_week_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday":3, "friday": 4, "saturday": 5, "sunday": 6}

    days_of_the_week_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    #Partition Duration Time in to Tuples
    duration_tuple = duration.partition(":")
    # print(duration_tuple)
    duration_hours = int(duration_tuple[0])
    duration_minutes = int(duration_tuple[2])

    #Partition start time into tuples
    start_tuple = start.partition(":")
    # print(start_tuple)
    start_minutes_tuple = start_tuple[2].partition(" ")

    # To separate the minutes and the AM and PM
    start_hours = int(start_tuple[0])
    start_minutes = int(start_minutes_tuple[0])
    am_or_pm = start_minutes_tuple[2] 

    am_and_pm_flip = {"AM": "PM", "PM": "AM"}

    amount_of_days = int(duration_hours / 24)

    end_minutes = start_minutes + duration_minutes
    if(end_minutes >= 60):
      start_hours += 1 # hours added to the starting hourse
      end_minutes = end_minutes % 60 #minutes go back to zero if its greater than 60
    amount_of_am_pm_flips = int((start_hours + duration_hours) / 12)
    
    end_hours = (start_hours + duration_hours) % 12

    end_minutes = end_minutes if end_minutes > 9 else "0" + str(end_minutes) # put 0 in front of single digits
    end_hours = end_hours = 12 if end_hours == 0 else end_hours

    if(am_or_pm == "PM" and start_hours + (duration_hours % 12) >= 12):
      amount_of_days += 1

    # Flip the time if AM or PM changes or stay the smae
    # This is what a Ternery Python looks like
    # Kind of the same as Javascript ternery condition statement
    am_or_pm = am_and_pm_flip[am_or_pm] if amount_of_am_pm_flips % 2 == 1 else am_or_pm

    returnTime = str(end_hours) + ":" + str(end_minutes) + " " + am_or_pm

    # How to calculate days of the week from duration
    #https://www.quickanddirtytips.com/education/math/how-to-calculate-the-day-of-the-week-of-any-date?page=1

    if(day_of_week):
      day_of_week = day_of_week.lower()
      index = int((days_of_the_week_index[day_of_week]) + amount_of_days) % 7
      new_day = days_of_the_week_array[index]
      returnTime += ", " + new_day

    if(amount_of_days == 1):
      return returnTime + " " + "(next day)"
    elif(amount_of_days > 1 ):
      return returnTime + " (" + str(amount_of_days) + " days later)"

    print(returnTime)
    return returnTime