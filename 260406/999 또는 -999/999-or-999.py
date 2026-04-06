arr = list(map(int, input().split()))
min = arr[0]
max = arr[0]
for i in range(len(arr)):
    if arr[i] == 999 or arr[i] == -999:
        break
    if min > arr[i]:
        min = arr[i]
    if max < arr[i]:
        max = arr[i]
print(f"{max} {min}")