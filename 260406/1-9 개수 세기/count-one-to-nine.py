N = int(input())
arr = list(map(int, input().split()))
num = [0]*9
for i in arr:
    num[i - 1] += 1
for i in num:
    print(i)