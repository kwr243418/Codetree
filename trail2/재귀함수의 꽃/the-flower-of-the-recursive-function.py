N = int(input())

# Please write your code here.
def mines(n):
    if n == 0:
        return
    print(n, end=' ')
    mines(n-1)
    print(n, end=' ')


mines(N)