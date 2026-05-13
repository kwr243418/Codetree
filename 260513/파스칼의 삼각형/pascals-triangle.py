N = int(input())
arr = [
    [1 for _ in range(i+1)]
    for i in range(N)
]

for i in range(2, N):
    for j in range(1, i):
        if arr[i-1][j-1] != 0 and arr[i-1][j] != 0:
            arr[i] [j] = arr[i-1][j-1] + arr[i-1][j]

for i in range(N):
    for j in range(i+1):
        print(arr[i][j], end=' ')
    print()