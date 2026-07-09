N = int(input())

# Please write your code here.
def num(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    if n % 2 == 0:
        return num(n-2) + n
    else:
        return num(n-2) + n


print(num(N))