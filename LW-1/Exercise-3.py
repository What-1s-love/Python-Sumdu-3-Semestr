# Input value of N (1 < N < 9)
N = int(input("Enter the value of N (1 < N < 9): "))

# Ensure N is within the valid range 
if 1 <= N <= 9:
    for i in range(N, 0, -1):
        for j in range(N, N-i, -1):
            print(j, end=" ")
        print(" ")
else:
    print("N must be between 1 and 9.")