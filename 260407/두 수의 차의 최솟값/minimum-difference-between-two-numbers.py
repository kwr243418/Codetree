N = int(input())
arr = list(map(int, input().split()))
min = arr[1] - arr[0]
for i in range(N-1):
    if min > arr[i+1] - arr[i]:
        min = arr[i+1] - arr[i]
print(min)