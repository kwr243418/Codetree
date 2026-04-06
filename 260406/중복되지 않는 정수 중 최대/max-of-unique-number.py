n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
arr = [0] * n
for i in range(n):
    for j in range(n):
        if i != j:
            if a[i] == a[j]:
                arr[i] = 1
                arr[j] = 1
max = a[arr.index(0)]
for i in range(n):
    if max < a[i] and arr[i] == 0:
        max = a[i]
print(max)