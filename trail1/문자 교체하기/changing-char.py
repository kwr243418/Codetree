A, B = map(str, input().split())
B = list(B)
B[0:2] = A[0:2]
B = ''.join(B)
print(B)