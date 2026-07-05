n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def gdg(n, arr):
    for i in range(n):
        if arr[i] < 0:
            temp = str(arr[i])
            arr[i] = int(temp[1:])
        print(arr[i], end=' ')


gdg(n, arr)