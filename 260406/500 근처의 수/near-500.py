arr = list(map(int, input().split()))
max = 0
min = 1000
for i in arr:
    if max < i and i < 500:
        max = i
    if min > i and i > 500:
        min = i
print(f"{max} {min}")