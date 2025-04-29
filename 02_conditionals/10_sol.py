pet_Species = input("Which pet species do you have(cat, dog): ")
pet_Age = int(input("Enter pet age: "))

if pet_Species.lower() == "dog":
    if pet_Age < 2:
        print("Puppy food")
    else:
        print("Adult food")
elif pet_Species.lower() == "cat":
    if pet_Age > 5:
        print("Senior cat food")
    else:
        print("Junior cat food")
else:
    print("Human food")