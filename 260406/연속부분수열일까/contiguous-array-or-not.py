N1, N2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
count = 0
if B[0] in A:
    idx = A.index(B[0])
    for i in range(1, N2):
        if A[idx + i] == B[i]:
            count += 1
        else :
            break
else :
    print("No")
if count == N2 - 1:
    print("Yes")
else :
    print("No")