A, B = input().split()
A2, B2 = '', ''
for i in A:
    if i.isdigit():
        A2 += i
    else :
        break

for i in B:
    if i.isdigit():
        B2 += i
    else :
        break

sum = int(A2) + int(B2)
print(sum)