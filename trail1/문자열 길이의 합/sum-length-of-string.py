n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
count = 0
sum = 0
for i in range(n):
    sum += len(arr[i])
    if arr[i][0] == 'a':
        count += 1
print(sum, count)