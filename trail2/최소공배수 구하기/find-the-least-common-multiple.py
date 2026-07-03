n, m = map(int, input().split())

# Please write your code here.
def GCD(n, m):
    num = min(n, m)
    while True:
        if n % num == 0 and m % num == 0:
            return num
        else:
            num -= 1

def LCM(n, m):
    num = (n * m) / GCD(n, m)
    print(f"{num:.0f}")


LCM(n, m)