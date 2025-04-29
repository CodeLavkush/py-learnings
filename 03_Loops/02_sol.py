number = int(input("Enter a number: "))
even_number_sum = 0

for num in range(1, number + 1):
    if num % 2 == 0:
        even_number_sum += num

print("The sum of Even Number is", even_number_sum)