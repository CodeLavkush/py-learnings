coffee = input("Enter coffie size(Small, Medium, Large): ")
extraShot = input("Do you want an extra shot(yes or no): ")

if extraShot.lower() == "yes":
    print(f"{coffee} coffee with an extra shot")
else:
    print(f"{coffee} coffee")