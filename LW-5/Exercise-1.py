N = int(input("Enter the number of array elements N: "))
numbers = [float(input(f"Element {i+1}: ")) for i in range(N)]

print("Non-zero elements in reverse order:")
for num in reversed(numbers):
    if num != 0:
        print(num)
