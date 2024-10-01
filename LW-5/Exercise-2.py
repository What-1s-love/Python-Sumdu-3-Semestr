size = 7

array = [
    [1 if i == 0 or i == size - 1 or j == 0 or j == size - 1 else 0 for j in range(size)]
    for i in range(size)
]

for row in array:
    print(' '.join(map(str, row)))
