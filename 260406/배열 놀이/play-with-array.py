arr = []
arr.append(list(map(int, input().split())))
arr.append(list(map(int, input().split())))
for i in range(arr[0][1]):
    arr.append(list(map(int, input().split())))
for i in range(arr[0][1]):
    if arr[i + 2][0] == 1:
        print(arr[1][arr[i+2][1] - 1])
    elif arr[i + 2][0] == 2:
        if arr[i + 2][1] not in arr[1]:
            print(0)
        else :
            print(arr[1].index(arr[i + 2][1]) + 1)
    elif arr[i + 2][0] == 3:
        for j in arr[1][arr[i + 2][1] - 1 : arr[i + 2][2]]:
            print(j, end=" ")
        print("")