# Build a program that asks the current time to the user, and reply good morning / afternoon and evening, depending of the day time
time = input("What time is it ? (in 24-hours format - Ex: 23:59) ")

if len(time) == 4: # I can use a RegEx to filter a single digit hour (1:45)
    str_hour = time[0:1:1]
else:
    str_hour = time[0:2:1]

if str_hour.isnumeric():
    hour = int(str_hour)
    if hour >= 0 and hour <= 23:
        hour = int(str_hour)
        if hour >= 6 and hour < 12:
            print("Good morning!")
        elif hour >= 12 and hour < 18:
            print("Good afternoon!")
        elif hour >= 18 and hour <= 23:
            print("Good evening!")
        else:
            print("Good night!")
    else:
        print("Please type a real time in a 24-hour format. For example: 00:35")
else:
    print("Type the time in numeric numbers. Please try again!")