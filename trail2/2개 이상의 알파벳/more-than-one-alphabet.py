A = input()

# Please write your code here.
def dfalpha(A):
    temp = A[0]
    for i in A:
        if i != temp:
            return True
    return False


if dfalpha(A):
    print("Yes")
else:
    print("No")