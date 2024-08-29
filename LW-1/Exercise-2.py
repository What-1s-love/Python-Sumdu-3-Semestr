# List of numbers 
numbers = [1,3,5,9,17]

# Print the header of the table 
print(f"{'Number': < 10} {'Square': < 10} {'Cube': < 10}")

# Calculate squares and cubes, and output the results for num in numbers:
for num in numbers:
    square = num ** 2
    cube = num ** 3
    print(f"{num: < 10} {square: < 10} {cube: < 10}")
