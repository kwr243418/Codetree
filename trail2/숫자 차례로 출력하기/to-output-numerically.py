n = int(input())

# Please write your code here.
def oneton(n):
    if n == 0:
        return
    oneton(n-1)
    print(n, end=' ')

def ntoone(n):
    if n == 0:
        return
    print(n, end=' ')
    ntoone(n-1)


oneton(n)
print()
ntoone(n)