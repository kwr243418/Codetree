a, b = map(int, input().split())

# Please write your code here.
def num(a, b):
    if a > b:
        a *= 2
        b += 10
    else:
        a += 10
        b *= 2
    print(a, b, end=' ')


num(a, b)