A, B = input().split()
sum = int(A) + int(B)
count = 0
for i in str(sum):
    if i == '1':
        count += 1
print(count)