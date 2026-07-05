n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def listdiv2(n, arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] = int(arr[i] / 2)
        print(arr[i], end=' ')


listdiv2(n, arr)