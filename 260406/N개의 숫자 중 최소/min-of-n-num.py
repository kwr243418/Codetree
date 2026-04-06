n = int(input())
a = list(map(int, input().split()))
min = a[0]
count = 0
for i in range(n):
    if min > a[i]:
        min = a[i]
for i in range(n):
    if min == a[i]:
        count += 1
print(f"{min} {count}")
# Please write your code here.
