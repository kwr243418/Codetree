A = input()

# Please write your code here.
B = []
count = 1
B.append(A[0])
if len(A) == 1:
    B.append(1)
else:
    for i in range(1, len(A)):
        if A[i] == A[i-1]:
            count += 1
            if i == len(A)-1:
                B.extend(map(int, str(count)))
        else :
            B.extend(map(int, str(count)))
            count = 1
            B.append(A[i])
            if i == len(A)-1:
                B.extend(map(int, str(count)))
print(len(B))
for elem in B:
    print(elem, end='')