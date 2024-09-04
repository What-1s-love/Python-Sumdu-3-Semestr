# Input a six-digit number as a string 
n = input("Enter a six-digit number: ")

# Check if the number is six digits long 
if len(n) == 6 and n.isdigit():
    # Calculate the sum of the digits 
    sum_of_digits = sum(int(digit) for digit in n)

    # Output the result 
    print(f"The sum of the digits of {n} is: {sum_of_digits}")
else:
    print("Invalid input. Make sure it's a six-digit natural number.")   