n, m = map(int, input().split())

# Please write your code here.
def GCD(n, m):
    num = min(n, m)
    
    while True:
        if n % num == 0 and m % num == 0:
            print(num)
            break
        num -= 1


GCD(n, m)