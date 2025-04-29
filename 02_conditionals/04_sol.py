fruit = input("Enter fruite name: ")
color = input("Enter fruite color: ")

if color.lower() == "green":
    print("The fruite is unripe.")
elif color.lower() == "brown":
    print("The fruite is Overripe.")
else:
    print("The fruite is ripe.")