N = int(input())
sum = 0
for _ in range(N):
    txt = int(input())
    sum += txt
sum = str(sum)
sum = sum[1:] + sum[0]
print(sum)