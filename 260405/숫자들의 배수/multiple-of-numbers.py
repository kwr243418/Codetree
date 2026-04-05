N = int(input())
count = 0
i = 0
arr = []
while True:
    if count == 2:
        break
    else :
        i += 1
        arr.append(N*i)
        print(arr[i-1], end=" ")
        if arr[i-1] % 5 == 0:
            count += 1