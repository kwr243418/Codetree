N = int(input())
arr = list(map(int, input().split()))
idx = []
for i in range(N):
    if arr[i] == 2:
        idx.append(i)
print(idx[2]+1)