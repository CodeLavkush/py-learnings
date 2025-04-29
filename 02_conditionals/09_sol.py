year = int(input("Enter current year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_LeapYear = True
        else:
            is_LeapYear = False
    else:
        is_LeapYear = True
else:
    is_LeapYear = False

if is_LeapYear:
    print(f"{year} is Leap year")
else:
    print(f"{year} is not a leap year")