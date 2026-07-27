n = int(input())
arr = list(map(int, input().split()))

arr.sort()

arr2 = []

for i in range(n):
    arr2.append(arr[i]+arr[-1-i])

print(max(arr2))
