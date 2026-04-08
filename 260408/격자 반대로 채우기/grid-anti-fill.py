N = int(input())
arr = [
    [0 for _ in range(N)]
    for _ in range(N)
]
count = 1
for col in range(N - 1, -1, -1):
    for row in range(N - 1, -1, -1):
        if col % 2 == (N - 1) % 2:
            arr[row][col] = count
        else :
            arr[N - 1 - row][col] = count
        count += 1
for row in range(N):
    for col in range(N):
        print(arr[row][col], end=" ")
    print()