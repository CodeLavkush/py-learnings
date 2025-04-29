distance = int(input("Enter Distance(ex. 3): "))

if distance < 3:
    print("Walk")
elif distance <= 15:
    print("Bike")
else:
    print("Car")