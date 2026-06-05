arr = list(map(str, input().split()))
print(ord(arr[0]) + ord(arr[1]), end=' ')
if ord(arr[0]) >= ord(arr[1]):
    print(ord(arr[0]) - ord(arr[1]))
else :
    print(ord(arr[1]) - ord(arr[0]))