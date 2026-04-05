arr = list(map(int, input().split()))
for i in range(10):
    if i >= 2:
        arr.append(arr[i - 1] + 2 * arr[i - 2])
    print(arr[i], end=" ")