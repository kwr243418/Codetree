n = int(input())
arr = list(map(int, input().split()))
for i in range(1, n+1):
    arr2 = arr[0:i]
    if i % 2 != 0:
        arr2.sort()
        print(arr2[i//2], end=' ')