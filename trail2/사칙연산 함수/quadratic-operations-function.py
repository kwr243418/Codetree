a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
if o == '+':
    res = a + c
    print(f"{a} + {c} = {res}")
elif o == '-':
    res = a - c
    print(f"{a} - {c} = {res}")
elif o == '*':
    res = a * c
    print(f"{a} * {c} = {res}")
elif o == '/':
    res = int(a / c)
    print(f"{a} / {c} = {res}")
else:
    print(False)