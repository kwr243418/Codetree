n = int(input())

# Please write your code here.
def is_magic_num(n):
    if n % 2 == 0 and (n%10 + n//10) % 5 == 0:
        print("Yes")
    else:
        print("No")


is_magic_num(n)