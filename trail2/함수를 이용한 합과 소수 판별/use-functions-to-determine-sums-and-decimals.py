a, b = map(int, input().split())

# Please write your code here.
def is_magic_num(n):
    is_sosu = True
    for i in range(2, n):
        if n % i == 0:
            is_sosu = False
            return False
    if is_sosu == True:
        arr = str(n)
        sum = 0
        for i in arr:
            sum += int(i)
        if sum % 2 == 0:
            return True
        else:
            return False


count = 0
for i in range(a, b+1):
    if is_magic_num(i):
        count += 1

print(count)