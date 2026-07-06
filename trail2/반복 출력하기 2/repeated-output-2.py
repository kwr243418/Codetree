n = int(input())

# Please write your code here.
def HW(n):
    if n == 0:
        return
    HW(n-1)
    print("HelloWorld")


HW(n)