N = int(input())
arr = [1, N]
count = 2
while True:
    if arr[count - 1] > 100:
        break
    else :
        arr.append(arr[count - 1] + arr[count - 2])
        count += 1
for i in arr:
    print(i, end=" ")