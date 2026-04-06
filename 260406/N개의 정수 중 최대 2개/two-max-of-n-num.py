n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
for j in range(n-1):
    for i in range(n-1):
     if a[i] < a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
print(f"{a[0]} {a[1]}")