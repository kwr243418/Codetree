y = int(input())

# Please write your code here.
def is_yoonyear(n):
    if n % 4 != 0:
        return False
    if n % 100 == 0 and n % 400 != 0:
        return False
    return True


if is_yoonyear(y):
    print("true")
else:
    print("false")