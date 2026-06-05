A = input()
B = input()

# Please write your code here.
while B in A:
    index = A.find(B)
    A = list(A)
    for _ in range(len(B)):
        A.pop(index)
    A = ''.join(A)
print(A)