n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
def sl(n):
    for i in range(n):
        if A[i] not in B:
            print("No")
            return
    print("Yes")


sl(n)