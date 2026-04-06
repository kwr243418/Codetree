arr = list(map(int, input().split()))
num = [0] * 6
for i in arr:
    num[i - 1] += 1
for i in range(len(num)):
    print(f"{i + 1} - {num[i]}")