a, b = map(int, input().split())

# Please write your code here.
def is_in_369(n):
    if '3' in str(n):
        return True
    elif '6' in str(n):
        return True
    elif '9' in str(n):
        return True
    else:
        return False

def is_magic_num(n):
    return n % 3 == 0 or is_in_369(n)


cnt = 0
for i in range(a, b+1):
    if is_magic_num(i):
        cnt += 1
print(cnt)