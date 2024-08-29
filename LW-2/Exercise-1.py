def calculate_z(x, y):
    """Calculate the value of z based on the value of x and y."""
    if x > 8:
        z = 3 + y
    else:
        z = 9 * x * y 
    return z

def factorial(n):
    """Calculate the factorial of n using a loop."""
    result = 1
    for i in range(2, n + 1): 
        result *= i
    return result

# Input for x and y
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

# Calculate and display z
z = calculate_z(x, y)
print(f"The value of z is: {z}")

# Input for n
n = int(input("Enter the value of n: "))

# Calculate and display factorial of n
factorial_of_n = factorial(n)
print(f"The factorial of {n} is: {factorial_of_n}")
