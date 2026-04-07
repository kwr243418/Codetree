arr = [
    list(map(str, input().split()))
    for _ in range(5)
]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr[i][j] = chr(ord(arr[i][j]) + ord('A') - ord('a'))
        print(arr[i][j], end=" ")
    print()