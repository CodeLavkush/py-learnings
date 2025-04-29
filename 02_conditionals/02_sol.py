age = int(input("Enter your age: "))
day = input("Enter Day(monday-sunday): ")

price = 12 if age > 18 else 8
discout = 2


if age > 18:
    if day.lower() == "wed" or day.lower() == "wednesday":
        print(f"Movie Ticket Price: {price - discout}")
    else:
        print(f"Movie Ticket Price: {price}")
else:
    if day.lower() == "wed" or day.lower() == "wednesday":
        print(f"Movie Ticket Price: {price - discout}")
    else:
        print(f"Movie Ticket Price: {price}")