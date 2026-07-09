n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def max(n, i, j):
    if j == n:
        return i
    if arr[i] > arr[j]:
        return max(n, i, j+1)
    else:
        return max(n, j, j+1)


print(arr[max(n, 0, 1)])