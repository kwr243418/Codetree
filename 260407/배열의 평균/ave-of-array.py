arr = [
    list(map(int, input().split()))
    for _ in range(2)
]
num = 0
for i in range(len(arr)):
    print(f"{sum(arr[i]) / len(arr[i]):.1f}", end=" ")
print()
for i in range(len(arr[0])):
    for j in range(len(arr)):
        num += arr[j][i]
    print(f"{num / len(arr):.1f}", end=" ")
    num = 0
print()
num = 0
for i in range(len(arr)):
    num += sum(arr[i])
print(f"{num / (len(arr) * len(arr[0])):.1f}")