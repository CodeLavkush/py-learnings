password = input("Enter your password: ")

password_Count = len(password)

if password_Count < 6:
    print("Password is weak.")
elif password_Count <= 10:
    print("Password is medium.")
else:
    print("Password is strong.")