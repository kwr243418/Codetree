arr = ["apple", "banana", "grape", "blueberry", "orange"]
count = 0
t = input()
for i in range(len(arr)):
    if arr[i][2] == t or arr[i][3] == t:
        print(arr[i])
        count += 1
print(count)