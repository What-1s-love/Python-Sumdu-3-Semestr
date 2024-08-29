a = int(input("Enter the value of a (from 1 to 100): "))
b = int(input("Enter the value of b (from 1 to 100): "))

# Checking if the entered values are correct
if not (1 <= a <= 100) or not (1 <= b <= 100):
    print("Values of a and b must be in the range from 1 to 100.")
    X = None # To avoid errors if X is not defined
else:
    # Calculating the value of X
    if a < b:
        X = (a * 3 - 5) / b
        condition = "a < b"
    elif a == b:
        X = -4
        condition = "a = b"
    else:
        X = (a**4 + b) / a
        condition = "a > b"

# Outputting the result
if X is not None:
    print("The value of X: ", X) 
    print("Condition used:", condition)