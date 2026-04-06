arr = list(map(int, input().split()))
arr2 = [0] * 10
sum = 0
while arr[0] > 1:
    arr2[arr[0] % arr[1]] += 1
    arr[0] = arr[0] // arr[1]
for i in arr2:
    sum += i ** 2
print(sum)