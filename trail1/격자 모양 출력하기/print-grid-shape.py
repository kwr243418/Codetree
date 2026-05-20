n, m = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))
res = [
    [0 for _ in range(n)]
    for _ in range(n)
]
for i in range(m):
    res[arr[i][0]-1][arr[i][1]-1] = arr[i][0] * arr[i][1]
for i in range(n):
    for j in range(n):
        print(res[i][j], end=' ')
    print()