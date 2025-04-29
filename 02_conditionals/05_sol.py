print("Welcome to activity suggetion tool based on weather!")
weather = input("Enter today's weather(Sunny, Rainy, snowy): ")

if weather.lower() == "sunny":
    print("Go for a walk")
elif weather.lower() == "rainy":
    print("Read a book")
elif weather.lower() == "snowy":
    print("Build a snowman")
else:
    print("Do nothing!")

