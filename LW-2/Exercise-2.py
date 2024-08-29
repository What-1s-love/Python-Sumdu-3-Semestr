# Importing the module 
from factorial_module import factorial 

# Input the value of n
n = int(input("Enter the value of n: "))

# Using the imported  function to calculate the factorial
factorial_of_n = factorial(n)
print(f"The factorial of {n} is: {factorial_of_n}")