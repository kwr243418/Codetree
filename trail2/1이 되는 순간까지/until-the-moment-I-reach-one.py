N = int(input())

# Please write your code here.
count = 0
def num(n):
    global count
    if n == 1:
        print(count)
        return
    if n % 2 == 0:
        count += 1
        return num(n//2)
    else:
        count += 1
        return num(n//3)


num(N)