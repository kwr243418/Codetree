N = int(input())
arr = [
    [0 for _ in range(N)]
    for _ in range(N)
]
num = 1
for i in range(N):
    for j in range(N):
        arr[j][i] = num
        num += 1
for i in arr:
    for j in i:
        print(j, end=" ")
    print()
