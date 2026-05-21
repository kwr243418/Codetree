arr = []
for _ in range(10):
    arr.append(input())
t = input()
count = 0
for i in range(10):
    if arr[i][-1] == t:
        count += 1
        print(arr[i])
if count == 0:
    print("None")