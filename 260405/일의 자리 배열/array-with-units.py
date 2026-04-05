N = list(map(int, input().split()))
arr = [0]*10
for i in range(10):
    if i < 2:
        arr[i] = N[i]
    else :
        arr[i] = arr[i-1] + arr[i-2]
        if arr[i] >= 10:
            arr[i] = arr[i] % 10
    print(f"{arr[i]}", end=" ")