a, b, c = map(int, input().split())

# Please write your code here.
def mns(a, b, c):
    m = a * b * c
    if m < 10:
        return m
    return mns(m//10, 1, 1) + m % 10


print(mns(a, b, c))