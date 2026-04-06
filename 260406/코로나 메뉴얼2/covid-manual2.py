arr = [0] * 4

for i in range(3):
    inp = list(map(str, input().split()))
    if inp[0] == 'Y' and int(inp[1]) >= 37:
        arr[0] += 1
    elif inp[0] == 'N' and int(inp[1]) >= 37:
        arr[1] += 1
    elif inp[0] == 'Y' and int(inp[1]) < 37:
        arr[2] += 1
    elif inp[0] == 'N' and int(inp[1]) < 37:
        arr[3] += 1

for i in arr:
    print(i, end=" ")

if arr[0] >= 2:
    print("E")
