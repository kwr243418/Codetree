N1, N2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
found = False
if B[0] in A:
    for i in range(len(A)):
        if A[i] == B[0]:
            if A[i : i+N2] == B:
                found = True
else :
    print("No")
if found == True:
    print("Yes")
else :
    print("No")