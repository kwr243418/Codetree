n = int(input())

# Please write your code here.
def num(n, c = 0):
    if n == 1:
        return c
    
    if n % 2 == 0:
        return num(n//2, c+1)
    else:
        return num(n*3+1, c+1)


print(num(n))