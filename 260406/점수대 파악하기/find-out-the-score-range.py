arr = list(map(int, input().split()))
num = [0] * 10
for i in arr:
    if i == 0:
        break
    if i // 10 != 0:
        num[i // 10 - 1] += 1
for i in range(9, -1, -1):
    print(f"{(i + 1) * 10} - {num[i]}")