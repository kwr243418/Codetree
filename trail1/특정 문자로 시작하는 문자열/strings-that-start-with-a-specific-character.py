n = int(input())
arr = []
for _ in range(n):
    arr.append(input())
t = input()
count = 0
strlen = 0
for i in range(n):
    if arr[i][0] == t:
        count += 1
        strlen += len(arr[i])
avl = strlen / count
print(f"{count} {avl:.2f}")